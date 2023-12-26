# openapi-client
# Introduction

<div class=\"status-info\">
<p class=\"status-info-title\">Note</p>
This documents the collection of Confluent Cloud APIs. Each API documents its
<a href=\"#section/Versioning/API-Lifecycle-Policy\">lifecycle phase</a>. APIs
marked as Early Access or Preview are not ready for production usage. We're currently
working with a select group of customers to get feedback and iterate on these APIs.
</div>

Confluent Cloud APIs are a core building block of Confluent Cloud. You can use the APIs to
manage your own account or to integrate Confluent into your product.

Most of the APIs are organized around
<a href=\"http://en.wikipedia.org/wiki/Representational_State_Transfer\" target=\"_blank\">REST</a>
and the resources which make up Confluent Cloud. The APIs have predictable
resource-oriented URLs, transport data using JSON, and use standard HTTP verbs,
response codes, authentication, and design principles.

# Object Model

<div class=\"status-info\">
<p class=\"status-info-title\">Note</p>
This section describes the object model for many Confluent Cloud APIs, but not all.
The Connect v1 API group has a different object model. You can review the example
request and response bodies in <a href=\"#tag/Connectors-(v1)\">Connect v1 API</a>
to see its object model.
</div>

Confluent Cloud APIs are primarily designed to be declarative and intent-oriented. In other words, 
tell the API what you want (for example, throughput or SLOs) and it will figure out how to make it happen 
(for example, cluster sizing). A Confluent object acts as a \"record of intent\" — after you create the
object, Confluent Cloud will work tirelessly in the background to ensure that the object exists
as specified.

Confluent APIs represent objects in JSON with media-type `application/json`.

Many objects follow a model consisting of `spec` and `status`. An object's `spec` tells
Confluent the _desired state_ (specification) of the resource. The object may not be
immediately available or changes may not be immediately applied. For this reason,
many objects also have a `status` property that provides info about the
_current state_ of the resource. Confluent Cloud is continuously and actively managing
each resource's current state to match it's desired state.

All Confluent objects share a set of common properties:

* **api_version** – API objects have an `api_version` field indicating their API version.
* **kind** – API objects have a `kind` field indicating the kind of object it is.
* **id** – Each object in the API will have an identifier, indicated via its `id` field,
  and should be treated as an opaque string unless otherwise specified.

There are a number of other [standard properties](#standard-properties) and that you'll encounter
used by many API objects. And of course, objects have plenty of non-standard fields that are
specific to each object _kind_... this is what makes them interesting!

# Authentication

Confluent uses API keys and Java Web Tokens (JWTs) to integrate your applications
and workflows to your Confluent Cloud resources using the Confluent Cloud REST APIs.
Your applications and workflows must be authenticated and authorized in order to
access and manage Confluent Cloud resources.

## API keys

You can create and manage your API keys using the Confluent Cloud Console or
Confluent CLI. For more information, see [Use API Keys to Control Access in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html).

Confluent Cloud uses the following two categories of API keys:

* A **Cloud API key** grants access to the Confluent Cloud Management APIs,
  such as for Provisioning and Metrics integrations.
* A **resource-specific API key** grants access to a Confluent Kafka cluster
  (Kafka API key), a Confluent Cloud Schema Registry (Schema Registry API key),
  Flink (Flink API key scoped to an Environment + Region pair), or a ksqlDB application.

Each Confluent Cloud API key is associated with a principal (specific user or
service account) and inherits the permissions granted to the owner.

* For example, if service account `Armageddon` is granted ACLs on Kafka cluster
  `neptune`, then a Kafka API Key for `neptune` owned by `Armageddon` will have
  these ACLs enforced.
* **Note:** API keys are automatically deleted when the associated user or service
  account is deleted (for example, when an employee leaves the company or moves to
  a new department and an SSO integration removes the Confluent Cloud user as they
  no longer require access).
* Confluent **strongly recommends** that you use service accounts for all
  production-critical access.

Confluent Cloud API keys grant access to Confluent Cloud resources, so **keep them secure**!
Do not share your API keys and secrets in publicly-accessible locations, such as 
GitHub or client-side code.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail.
API requests without authentication will also fail.

To use an API key, you must send it in an `Authorization: Basic {credentials}` header.
Remember that HTTP Basic authentication requires you to provide your credentials as
the API key ID and associated API secret separated by a colon and encoded using Base64
format. For example, if your API key ID is `ABCDEFGH123456789` and the API key Secret 
is `XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO`, then the authorization header is:

```text​
Authorization: Basic QUJDREVGR0gxMjM0NTY3ODk6WE5DSVc5M0kyTDFTUVBKU0o4MjNLMUxTOTAyS0xERk1DWlBXRU8=
```

You can generate this header example from the API key:

macOS:

```shell
$ echo -n \"ABCDEFGH123456789:XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO\" | base64

```

Linux:

```shell
$ echo -n \"ABCDEFGH123456789:XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO\" | base64 -w 0
```

To find out if an API operation supports Cloud API Keys, look in the **AUTHORIZATIONS**
listing for `cloud-api-key`.

To find out if an API operation supports resource-specific API Keys, look in the **AUTHORIZATIONS**
listing for `resource-api-key`.

## External OAuth

You can use [OAuth/OIDC support for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html)
to authenticate and authorize access to applications and workloads for the
following Confluent Cloud REST APIs:

* **Kafka REST API**: [Kafka REST API for Clusters(V3)](https://docs.confluent.io/cloud/current/api.html#tag/Cluster-(v3)).
  For an API overview and examples, see [Cluster Management with Kafka REST API](https://docs.confluent.io/cloud/current/kafka-rest/kafka-rest-cc.html).
* **Schema Registry REST API**: [Schema Registry REST API for Schemas(V1)](https://docs.confluent.io/cloud/current/api.html#tag/Schemas-(v1))
  and [Subjects](https://docs.confluent.io/cloud/current/api.html#tag/Subjects-(v1)).
  For an API overview and examples, see [Schema Registry REST API for Confluent Cloud](https://docs.confluent.io/cloud/current/sr/sr-rest-apis.html).

Alternatively, to find out if an API operation supports external tokens, look in the **AUTHORIZATIONS**
listing for `external-access-token`.

## Confluent STS tokens

Confluent Security Token Service (STS) issues access tokens (`confluent-sts-access-token`)
by exchanging an external token (`external-access-token`) for a `confluent-sts-access-token`. You can use
Confluent STS tokens to authenticate to Confluent Cloud APIs that support the
`confluent-sts-access-token` notation.

To find out if an API operation supports Confluent STS tokens, look in the **AUTHORIZATIONS**
listing for `confluent-sts-access-token`.

## Partner OAuth

Approved partners can fetch Partner tokens (`confluent-partner-access-token`) that validate their identity
and grant access to the Partner API (`partner/v2`), which lets them sign up
an organization on behalf of a customer, manage entitlements (create, read, and list),
and read or list organizations they have signed up.

To find out an API operation supports Partner tokens, look in the **AUTHORIZATIONS**
listing for `confluent-partner-access-token`.

<!-- TODO: port this back to the Confluent API Design Guide -->

<SecurityDefinitions />

# Errors

<div class=\"status-info\">
<p class=\"status-info-title\">Note</p>
This section describes the structure of error responses for many Confluent Cloud APIs, but not all.
The Connect v1 API group has a different set of structures for error responses. Please review the example
request and response bodies in the Connect v1 API documentation <a href=\"#tag/Connectors-(v1)\">below</a>
to see its error behaviour.
</div>

Confluent uses conventional [HTTP status codes](#section/HTTP-Guidelines/Status-Codes) to
indicate the success or failure of an API request.

Failures follow a standard model to tell you about what went wrong. They may include
one or more error objects with the following fields:

| Field      | Type    | Description
|------------|---------|--------------------------------------
| id*        | UUID    | A unique identifier for this particular occurrence of the problem.
| status     | String  | The HTTP status code applicable to this problem.
| code       | String  | An application-specific error code.
| title      | String  | A short, human-readable summary of the problem that **should not** change from occurrence to occurrence of the problem, except for purposes of localization.
| detail*    | String  | A human-readable explanation specific to this occurrence of the problem. Like title, this field’s value can be localized.
| source     | Object  | An object that references the source of the error, and optionally includes any of the following members:
| &nbsp;&nbsp;pointer   | String  | A <a href=\"https://tools.ietf.org/html/rfc6901\" target=\"_blank\">JSON Pointer</a> to the associated entity in the request document (e.g. `\"/spec/title\"` for a specific attribute).
| &nbsp;&nbsp;parameter | String  | A string indicating which URI query parameter caused the error.
| meta       | Object  | A meta object that contains non-standard meta-information about the error.
| resolution | String  | Instructions for the end-user for correcting the error.

\\* indicates a required field

All errors include an `id` and some `detail` message. The `id` is a unique identifier — use it
when you're working with Confluent support to debug a problem with a specific API call. The
`detail` describes what went wrong.

Some errors that could be handled programmatically (e.g., a Kafka cluster config is invalid)
may include an error `code` that briefly explains the error reported.

Validation issues and similar errors include a `source` which tells you exactly
what in the request was responsible for the error.

For example, a failure may look like

    {
      \"errors\": [{
        \"status\": \"422\",
        \"code\": \"invalid_configuration\",
        \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\",
        \"title\": \"The Kafka cluster configuration is invalid\",
        \"detail\": \"The property '/cluster/storage_size' of type string did not match the following type: integer\",
        \"source\": {
          \"pointer\": \"/cluster/storage_size\"
        }
      }]
    }

If a request fails validation, it will return an HTTP `422 Unprocessable Entity`
with a list of fields that failed validation.

# Pagination

<div class=\"status-info\">
<p class=\"status-info-title\">Note</p>
This section describes the pagination behavior of “list” operations for many Confluent Cloud APIs, but not all.
The Connect v1 API list operations do not support pagination.
</div>

All API resources have support for bulk reads via \"list\" API operations. For example,
you can \"list Kafka clusters\", \"list api keys\", and \"list environments\". These \"list\"
operations require pagination; by requesting smaller subsets of data, API clients
receive a response much faster than requesting the entire, potentially large, data set.

All \"list\" operations follow the same pattern with the following parameters:

* `page_size` –  client-provided max number of items per page, only valid on the first request.
* `page_token` –  server-generated token used for traversing through the result set.

A paginated response may include any of the following pagination links. API clients may
follow the respective link to page forward or backward through the result set as desired.

| [Link Relation](https://www.iana.org/assignments/link-relations/link-relations.xml) | Description
|---------|---------------------------------------
| `next`  | A link to the next page of results. A response that does not contain a next link does not have further data to fetch.
| `prev`  | A link to the previous page of results. A response that does not contain a prev link has no previous data. This link is **optional** for collections that cannot be traversed backward.
| `first` | A link to the first page of results. This link is **optional** for collections that cannot be indexed directly to a given page.
| `last`  | A link to the last page of results. This link is **optional** for collections that cannot be indexed directly to a given page.

API clients must treat pagination links and the `page_token` parameter in particular as an opaque string. 

An example paginated list response may look like
```
{
    \"api_version\": \"v2\",
    \"kind\": \"KafkaClusterList\",
    \"metadata\": {
        \"next\": \"https://api.confluent.cloud/kafka-clusters?page_token=ABCDEFGHIJKLMNOP1234567890\"
    }
    \"data\": [
        {
            \"metadata\": {
                \"id\": \"lkc-abc123\",
                \"self\": \"https://api.confluent.cloud/kafka-clusters/lkc-abc123\",
                \"resource_name\": \"crn://confluent.cloud/kafka=lkc-abc123\",
            }
            \"spec\": {
                \"display_name\": \"My Kafka Cluster\",
                <snip>
            },
            \"status\": {
                \"phase\": \"RUNNING\",
                <snip>
            }
        },
        <snip>
    ]
}
```

# Rate Limiting

To protect the stability of the API and keep it available to all users, Confluent employs
multiple safeguards. If you send too many requests in quick succession or perform too many
concurrent operations, you may be throttled or have your request rejected with an error.

When a rate limit is breached, an HTTP `429 Too Many Requests` error is
returned. The following headers are sent back to provide assistance in dealing
with rate limits. Note that headers are not returned for a `429` error response with 
[Kafka REST API (v3)](https://docs.confluent.io/cloud/current/api.html#tag/Cluster-(v3)).

| Header                  | Description
|-------------------------|----------------------------------------
| `X-RateLimit-Limit`     | The maximum number of requests you're permitted to make per time period.
| `X-RateLimit-Reset`     | The relative time in seconds until the current rate limit window resets.
| `Retry-After`           | The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached.
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate-limit window. **Important:** This differs from Github and Twitter\\'s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues.


Confluent enforces multiple kinds of limits, including request-rate and concurrency limits, both per user and organization-wide. Unauthenticated requests are associated with the originating IP address, not the user making requests.


Integrations should gracefully handle these limits by watching for `429` error responses and
building in a retry mechanism. This mechanism should follow a capped exponential backoff policy to
prevent [retry amplification](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/)
(\"retry storms\") and also introduce some randomness (\"jitter\") to avoid the
[thundering herd effect](https://en.wikipedia.org/wiki/Thundering_herd_problem).


If you’re running into this error and think you need a higher rate limit, contact Confluent at
[support@confluent.io](mailto:support@confluent.io).

# Identifiers and URLs

Most resources have multiple identifiers:
* `id` is the \"natural identifier\" for an object. It is only unique within its parent resource.
  The `id` is unique across time: the ID will not be reclaimed and reused after an object is deleted.
* `resource_name` is a Uniform Resource Identifier (URI) that is globally unique across all resources.
  This encompasses all parent resource `kind`s and `id`s necessary to uniquely identify a particular
  instance of this object `kind`. Because it uses object `id`s, the CRN will not be reclaimed and
  reused after an object is deleted. It is represented as a Confluent Resource Name (see below). 
* `self` is a Uniform Resource Locator (URL) at which an object can be addressed.
  This URL encodes the service location, API version, and other particulars necessary to
  locate the resource at a point in time.

To see how these relate to each other, consider `KafkaBroker` with `broker.id=2` in a `KafkaCluster`
in Confluent Cloud identified as `lkc-xsi8201`. In such an example, the `KafkaBroker` has `id=2`,
the `resource_name` is `crn://confluent.cloud/kafka=lkc-xsi8201/broker=2` and the `self` URL may be
something like `https://pkc-8wlk2n.us-west-2.aws.confluent.cloud`. Note that different identifiers
carry different information for different purposes, but the `resource_name` is the most complete
and canonical identifier.

## Confluent Resource Names (CRNs)

*Confluent Resource Names* (CRNs) are used to uniquely identify all Confluent resources.

A CRN is a valid URI having an \"authority\" of `confluent.cloud` or a self-managed
<a href=\"https://docs.confluent.io/current/security/rbac/configure-mds/index.html\" target=\"_blank\">
metadata service URL</a>, followed by the minimal hierarchical set of key-value
pairs necessary to uniquely identify a resource.

Here are some examples for basic resources in Confluent Cloud:

| Resource                   | Example CRN                                                                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Organization               | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a                                                                                                  |
| Environment                | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy                                                                            |
| User                       | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/user=u-rst9876                                                                                   |
| API Key                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/user=u-zyx98/api-key=ABCDEFG9876543210                                                           |
| Service Account            | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/service-account=sa-abc1234                                                                       |
| Kafka Cluster              | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc                                  |
| Kafka Topic                | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc/topic=my_kafka_topic             |
| Consumer Group             | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc/group=confluent_cli_consumer_123 |
| Network                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc                                                           |
| Peering                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/peering=p-123abc                                          |
| Private Link Access        | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/private-link-access=pla-123abc                            |
| Transit Gateway Attachment | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/transit-gateway-attachment=tgwa-123abc                    |
| Schema Registry Cluster    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/schema-registry=lsrc-789qw                                                 |
| Schema Subject             | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/schema-registry=lsrc-789qw/subject=test                                    |

# Data Types

## Primitive Types

| Data Type  | Representation
|------------|---------------------
| Integers   | Each API may specify the type as `int32` or `int64`. Note that many languages, including JavaScript, are limited to a max size of approx `2**53` and don't correctly handle large `int64` values with their default JSON parser.
| Dates      | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given.
| Times      | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given.
| Durations  | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string.
| Periods    | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given.
| Ranges     | All ranges are represented using half-open intervals with naming conventions like `[start_XXX, end_XXX)` such as `[start_time, end_time)`.
| Enums      | Most APIs use <a href=\"https://opensource.zalando.com/restful-api-guidelines/#112\" target=\"_blank\">`x-extensible-enum`</a> as an open-ended list of values. This improves compatibility compared with a standard `enum` which by definition represents a closed set. All enums have a `0`-valued entry which either serves as the default for common cases, or represents `UNSPECIFIED` when no default exists and results in an error.

<!-- TODO
### Standard Objects

| Money Object | https://schema.org/MonetaryAmount or https://opensource.zalando.com/restful-api-guidelines/#173
| Price Specification | https://schema.org/PriceSpecification -> https://schema.org/UnitPriceSpecification and https://schema.org/PaymentChargeSpecification
-->

### Standard Properties

Confluent uses this set of standard properties to ensure common concepts use
the same name and semantics across different APIs.

| Name             | Description
|------------------|------------------------------------------
| **api_version**  | Many API objects have an `api_version` field indicating their API version. See the [Object Model](#section/Object-Model).
| **kind**         | Many API objects have a `kind` field indicating the kind of object it is. See the [Object Model](#section/Object-Model).
| **id**           | Many objects in the API will have an identifier, indicated via its `id` field, and should be treated as an opaque string unless otherwise specified. See the [Object Model](#section/Object-Model).
| **name**         | Objects which support a client-provided unique identifier instead of a generated `id` will indicate this identifier via its `name` field.
| **display_name** | The human-readable display name of an API object.
| **title**        | The official name of an API object, such as a company name. It should be treated as the formal version of `display_name`.
| **description**  | One or more paragraphs of text description of an entity.
| **created_at**   | The date and time the object was created, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format.
| **updated_at**   | The date and time the object was last modified, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format.
| **deleted_at**   | If present, the date and time after which the object was/will be deleted, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format.
| **page_token**   | The pagination token in the List request. See [Pagination](#section/Pagination).
| **page_size**    | The pagination size in the List request. See [Pagination](#section/Pagination).
| **total_size**   | The total count of items in the list irrespective of pagination. See [Pagination](#section/Pagination).
| **spec**         | The _desired state_ specification of the resource, as observed by Confluent Cloud.
| **status**       | The _current state_ of the resource, as observed by Confluent Cloud.

# Versioning

Confluent APIs ensure stability for your integrations by avoiding the introduction
of breaking changes to customers unexpectedly. Confluent will make non-breaking
API changes without advance notice. Thus, API clients **must**  follow the
[Compatibility Policy](#section/Versioning/Compatibility-Policy) below to ensure your
ingtegration remains stable. All APIs follow the API Lifecycle Policy described below,
which describes the guarantees API clients can rely on.

Breaking changes will be [widely communicated](#communication) in advance in accordance
with the Confluent [Deprecation Policy](#section/Versioning/Deprecation-Policy). Confluent will provide 
timelines and a migration path for all API changes, where available. Be sure to subscribe
to one or more [communication channels](#communication) so you don't miss any updates!

One exception to these guidelines is for critical security issues. Confluent will take any necessary
actions to mitigate any critical security issue as soon as possible, which may include disabling
the vulnerable functionality until a proper solution is available.

Do not consume any Confluent API unless it is documented in the API Reference. All undocumented
endpoints should be considered private, subject to change without notice, and not covered by any
agreements.

> Note: The version in the URL (e.g. \"v1\" or \"v2\") is not a \"major version\" in the
[Semantic Versioning](https://semver.org/) sense. It is a \"generational version\" or \"meta version\", as seen in
APIs like <a href=\"https://developer.github.com/v3/versions/\" target=\"_blank\">Github API</a> or the
<a href=\"https://stripe.com/docs/api/versioning\" target=\"_blank\">Stripe API</a>.

## API Groups

Confluent APIs are divided into API Groups, such as the Cluster Management for Apache Kafka (CMK) API group,
the Connect API group, and the Data Catalog API group. Each group has its own set of endpoints and resources,
as well as its own API group version.

Because different API groups have different versions, there is no single version for the \"Confluent Cloud API\".
The latest version of the Connect API group may be `connect/v1`, while the latest version of the CMK API group
may be `cmk/v2`.

When a breaking change is introduced into one API group, Confluent will increase the API version for that API group
only, leaving the other API groups' versions unchanged. This makes it easier for you to understand whether a given
breaking change impacts your usage of the APIs.

## Known Issues

During the Early Access and Preview periods, we have a few known issues.

| Issue          | Description                                                                   | Proposed Resolution
|----------------|-------------------------------------------------------------------------------|-----------------------------------------------------
| Quota Exceeded | Some \"Quota Exceeded\" errors will be returned as HTTP 400 instead of HTTP 402 | Return 402 consistently for \"Quota Exceeded\" errors 

## API Lifecycle Policy

The following status labels are applicable to APIs, features, and SDK versions, based on
the current support status of each:

* **Early Access** – May change at any time. Not recommended for production usage. Not officially supported by
  Confluent. Intended for user feedback only. Users must be granted explicit access to the API by Confluent.
* **Preview** – Unlikely to change between Preview and General Availability. Not recommended for production usage.
  Officially supported by Confluent for non-production usage. Accessible to all users.
* **Limited Availability (LA)** - Available to key select customers in a subset of regions/providers/networks and recommended for production usage.  
* **Generally Available (GA)** – Will not change at short notice. Recommended for production usage.
  Officially supported by Confluent for non-production and production usage.
* **Deprecated** – Still supported, but no longer under active development. Existing usage will continue to function
  but migration following the upgrade guide is strongly recommended. New use cases should be built against the new
  version. Deprecated feature or version will be removed in the future at the announced date.
* **Sunset** – Removed, and no longer supported or available.

An API is \"Generally Available\" unless explicitly marked otherwise.

## Compatibility Policy

Confluent Cloud APIs are governed by
<a href=\"https://docs.confluent.io/cloud/current/clusters/upgrade-policy.html\" target=\"_blank\">
Confluent Cloud Upgrade Policy</a>, which means that backward incompatible changes and
deprecations will be made approximately once per year, and 180 days notice will be provided via email to all
registered Confluent Cloud users.

### Backward Compatibility

> _An API version is backward compatible if a program written against the previous version of the API will continue to work the same way, without modification, against this version of the API._

Confluent considers the following changes to be backward compatible:

* Adding new API resources.
* Adding new optional parameters to existing API requests (e.g., query string).
* Adding new properties to existing API resources (e.g., request body).
* Changing the order of properties in existing API responses.
* Changing the length or format of object IDs or other opaque strings.
  * Unless otherwise documented, you can safely assume object IDs generated by Confluent will never exceed 255
    characters, but you should be able to handle IDs of up to that length. If you're using MySQL,
    for example, you should store IDs in a `VARCHAR(255) COLLATE utf8_bin` column.
  * This includes adding or removing fixed prefixes (such as `lkc-` on Kafka cluster IDs).
  * This includes API keys, API tokens, and similar authentication mechanisms.
  * This includes all strings described as \"opaque\" in the docs, such as pagination cursors.
* Adding new API event types.
* Adding new properties to existing API event types.
* Omitting properties with null values from existing API responses.

### Forward Compatibility

> _An API version is forward compatible if a program written against the next version of the API
> will continue to work the same way, without modification, against this version of the API._

In other words, a forward compatible API will accept input intended for a later version of itself.

Confluent does not guarantee the forward compatibility of the APIs, but Confluent does generally follow the guidelines
given by the [Robustness principle](https://en.wikipedia.org/wiki/Robustness_principle).
This means that the API determines what to do with a request based only on the parts that it recognizes.

This is often referred to as the MUST IGNORE rule.

* Request parameters that are not recognized will be ignored (e.g., query string).
* Request properties that are not recognized will be ignored (e.g., request body).
* Request metadata that are not recognized will be ignored (e.g., request headers).

API clients must also follow the MUST IGNORE rule.

* Response properties that are not recognized must be ignored (e.g., response body).
* Response metadata that are not recognized must be ignored (e.g., response headers).

Additionally, there is a more subtle related rule called the MUST FORWARD rule. Any parts of
a request that an API doesn't recognize must be forwarded unchanged.

* Response properties that are not recognized must be included in any input subsequent updates (e.g., request body)
  * This includes future `PUT` requests in a read/modify/write operation.
    (This isn't required for `PATCH` partial updates, which is why Confluent APIs use `PATCH`.)
* Event processors must not strip unknown properties before forwarding messages.

### Client Responsibilities

* Resource and rate limits, and the default and maximum sizes of paginated data **are not**
  considered part of the API contract and may change (possibly dynamically). It is the client's
  responsibility to read the road signs and obey the speed limit.
* If a property has a primitive type and the API documentation does not explicitly limit its
  possible values, clients **must not** assume the values are constrained to a particular set
  of possible responses.
* If a property of an object is not explicitly declared as mandatory in the API, clients
  **must not** assume it will be present.
* A resource **may** be modified to return a \"redirection\" response (e.g. `301`, `307`) instead of
  directly returning the resource. Clients **must** handle HTTP-level redirects, and respect HTTP
  headers (e.g. `Location`).

## Deprecation Policy

Confluent will announce deprecations at least 180 days in advance of a breaking change
and will continue to maintain the deprecated APIs in their original form during this time.

Exceptions to this policy apply in case of critical security vulnerabilities or functional defects.

### Communication

When a deprecation is announced, the details and any relevant migration
information will be available on one or more of the following channels:

* Announcements on the <a href=\"https://www.confluent.io/blog/\" target=\"_blank\">Developer Blog</a>,
  <a href=\"https://confluentcommunity.slack.com\" target=\"_blank\">Community Slack</a>
  (<a href=\"https://slackpass.io/confluentcommunity\" target=\"_blank\">join!</a>),
  <a href=\"https://groups.google.com/forum/#!forum/confluent-platform\" target=\"_blank\">Google Group</a>,
  the <a href=\"https://twitter.com/ConfluentInc\" target=\"_blank\">@ConfluentInc twitter</a>
  account, and similar channels
* Enterprise customers may receive information by email to their specified Confluent contact, if applicable.

<!-- TODO:
### Discoverability
-->

# HTTP Guidelines

## Status Codes

Confluent respects the meanings and behavior of HTTP status codes as defined
in <a href=\"https://tools.ietf.org/html/rfc2616\">RFC2616</a> and elsewhere.

* Codes in the `2xx` range indicate success
* Codes in the `3xx` range indicate redirection
* Codes in the `4xx` range indicate an error caused by the client request
  (e.g., a required parameter was omitted, an invalid cluster configuration was provided, etc.)
* Codes in the `5xx` range indicate an error with Confluent's servers (these are rare)

The various HTTP status codes that might be returned are listed below.

| Code | Title                  | Description
|------|------------------------|--------------------------------
| 200  | OK                     | Everything worked as expected.
| 201  | Created                | The resource was created. Follow the `Location` header.
| 204  | No Content             | Everything worked and there is no content to return.
| 400  | Bad Request         | The request was unacceptable, often due to malformed syntax, or a missing or malformed parameter.
| 401  | Unauthorized           | No valid credentials provided. or the credentials are unsuitable, invalid, or unauthorized.
| 402  | Over Quota             | The request was valid, but you've exceeded your plan quota or limits.
| 404  | Not Found              | The requested resource doesn't exist or you're unauthorized to know it exists.
| 409  | Conflict               | The request conflicts with another request (perhaps it already exists or was based on a stale version of data).
| 422  | Validation Failed      | The request was parsed correctly but failed some sort of validation.
| 429  | Too Many Requests      | Too many requests hit the API too quickly. Confluent recommends an exponential backoff of your requests.
| 500, 502, 503, 504 | Server Errors | Something went wrong on Confluent's end. (These are rare.)

This list is not exhaustive; other standard HTTP error codes may be used,
including `304`, `307`, `308`, `405`, `406`, `408`, `410`, and `415`.

For more details, see https://httpstatuses.com.

<!--

## Method Overriding

Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those
environments, Confluent API operations that require `PUT`, `PATCH`, and `DELETE` verbs will be inaccessible.

To avoid this issue, Confluent APIs support the `X-HTTP-Method-Override` header, allowing clients to
\"tunnel\" `PUT`, `PATCH`, and `DELETE` requests via a `POST` request.

For example, to call a Confluent `PATCH` resource via a `POST` request, you can
include `X-HTTP-Method-Override: PATCH` as a header.

## User Agent Required

Confluent API requests **should** include a valid `User-Agent` header. Requests with no `User-Agent`
header may be rejected. You should use the name of your integration for the `User-Agent`
header value and include contact information so that Confluent can contact you if there are problems.

> If your integration is acting as a proxy or gateway, you **should** forward the User-Agent
> of the originating client with your API requests.

Here's a complete example:

    User-Agent: CoolToolName/1.2.3 (https://example.org/CoolTool/; CoolTool@example.org) UsedBaseLibrary/2.1.0

The minimum user agent string is the integration name and version: `name/version`.
You can string together multiple values in a space-separated list. The full syntax is:

    name/version [(comments)] [name/version [(comments)]] [...]​

For the integration name, use a string (without whitespace) that clearly and meaningfully
identifies your integration.

* Avoid ambiguous names: `Confluent-Integration`, `Kafka-Sink`
* Use clear and meaningful names: `ABCTools-ToolName`, `StackStorm-Confluent-Plugin`

For the version, use a semantic version, build ID, commit hash, or other identifier
that is updated automatically when you release a new version.

Wrap comments in parentheses `()` as a semi-colon separated list. Helpful comments to include:

* A public URL for your integration, such as a GitHub link or a page in your
  docs site that describes the integration.
* Contact information so that Confluent can easily reach the integration publisher. This
  information from the user agent string will never be shared nor used by Confluent for
  any purpose other than discussing the integration with its publisher.

If you provide an invalid `User-Agent` header, you may receive a `403 Forbidden` response.

-->

# Metrics APIs

For Metrics APIs, see <a href=\"https://api.telemetry.confluent.cloud/docs\">Confluent Cloud Metrics API</a>.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.confluent.io/cloud-contact-us/](https://www.confluent.io/cloud-contact-us/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import acl__v3_api
from openapi_client.model.acl_data_list import AclDataList
from openapi_client.model.acl_resource_type import AclResourceType
from openapi_client.model.create_acl_request_data import CreateAclRequestData
from openapi_client.model.create_acl_request_data_list import CreateAclRequestDataList
from openapi_client.model.error import Error
from openapi_client.model.inline_response2004 import InlineResponse2004
# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: external-access-token
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acl__v3_api.ACLV3Api(api_client)
    cluster_id = "cluster-1" # str | The Kafka cluster ID.
create_acl_request_data_list = CreateAclRequestDataList(None) # CreateAclRequestDataList | The batch ACL creation request. (optional)

    try:
        # Batch Create ACLs
        api_instance.batch_create_kafka_acls(cluster_id, create_acl_request_data_list=create_acl_request_data_list)
    except openapi_client.ApiException as e:
        print("Exception when calling ACLV3Api->batch_create_kafka_acls: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.confluent.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ACLV3Api* | [**batch_create_kafka_acls**](docs/ACLV3Api.md#batch_create_kafka_acls) | **POST** /kafka/v3/clusters/{cluster_id}/acls:batch | Batch Create ACLs
*ACLV3Api* | [**create_kafka_acls**](docs/ACLV3Api.md#create_kafka_acls) | **POST** /kafka/v3/clusters/{cluster_id}/acls | Create an ACL
*ACLV3Api* | [**delete_kafka_acls**](docs/ACLV3Api.md#delete_kafka_acls) | **DELETE** /kafka/v3/clusters/{cluster_id}/acls | Delete ACLs
*ACLV3Api* | [**get_kafka_acls**](docs/ACLV3Api.md#get_kafka_acls) | **GET** /kafka/v3/clusters/{cluster_id}/acls | List ACLs
*APIKeysIamV2Api* | [**create_iam_v2_api_key**](docs/APIKeysIamV2Api.md#create_iam_v2_api_key) | **POST** /iam/v2/api-keys | Create an API Key
*APIKeysIamV2Api* | [**delete_iam_v2_api_key**](docs/APIKeysIamV2Api.md#delete_iam_v2_api_key) | **DELETE** /iam/v2/api-keys/{id} | Delete an API Key
*APIKeysIamV2Api* | [**get_iam_v2_api_key**](docs/APIKeysIamV2Api.md#get_iam_v2_api_key) | **GET** /iam/v2/api-keys/{id} | Read an API Key
*APIKeysIamV2Api* | [**list_iam_v2_api_keys**](docs/APIKeysIamV2Api.md#list_iam_v2_api_keys) | **GET** /iam/v2/api-keys | List of API Keys
*APIKeysIamV2Api* | [**update_iam_v2_api_key**](docs/APIKeysIamV2Api.md#update_iam_v2_api_key) | **PATCH** /iam/v2/api-keys/{id} | Update an API Key
*AppliedQuotasServiceQuotaV1Api* | [**get_service_quota_v1_applied_quota**](docs/AppliedQuotasServiceQuotaV1Api.md#get_service_quota_v1_applied_quota) | **GET** /service-quota/v1/applied-quotas/{id} | Read an Applied Quota
*AppliedQuotasServiceQuotaV1Api* | [**list_service_quota_v1_applied_quotas**](docs/AppliedQuotasServiceQuotaV1Api.md#list_service_quota_v1_applied_quotas) | **GET** /service-quota/v1/applied-quotas | List of Applied Quotas
*ClientQuotasKafkaQuotasV1Api* | [**create_kafka_quotas_v1_client_quota**](docs/ClientQuotasKafkaQuotasV1Api.md#create_kafka_quotas_v1_client_quota) | **POST** /kafka-quotas/v1/client-quotas | Create a Client Quota
*ClientQuotasKafkaQuotasV1Api* | [**delete_kafka_quotas_v1_client_quota**](docs/ClientQuotasKafkaQuotasV1Api.md#delete_kafka_quotas_v1_client_quota) | **DELETE** /kafka-quotas/v1/client-quotas/{id} | Delete a Client Quota
*ClientQuotasKafkaQuotasV1Api* | [**get_kafka_quotas_v1_client_quota**](docs/ClientQuotasKafkaQuotasV1Api.md#get_kafka_quotas_v1_client_quota) | **GET** /kafka-quotas/v1/client-quotas/{id} | Read a Client Quota
*ClientQuotasKafkaQuotasV1Api* | [**list_kafka_quotas_v1_client_quotas**](docs/ClientQuotasKafkaQuotasV1Api.md#list_kafka_quotas_v1_client_quotas) | **GET** /kafka-quotas/v1/client-quotas | List of Client Quotas
*ClientQuotasKafkaQuotasV1Api* | [**update_kafka_quotas_v1_client_quota**](docs/ClientQuotasKafkaQuotasV1Api.md#update_kafka_quotas_v1_client_quota) | **PATCH** /kafka-quotas/v1/client-quotas/{id} | Update a Client Quota
*ClusterLinkingV3Api* | [**create_kafka_link**](docs/ClusterLinkingV3Api.md#create_kafka_link) | **POST** /kafka/v3/clusters/{cluster_id}/links | Create a cluster link
*ClusterLinkingV3Api* | [**create_kafka_mirror_topic**](docs/ClusterLinkingV3Api.md#create_kafka_mirror_topic) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | Create a mirror topic
*ClusterLinkingV3Api* | [**delete_kafka_link**](docs/ClusterLinkingV3Api.md#delete_kafka_link) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Delete the cluster link
*ClusterLinkingV3Api* | [**delete_kafka_link_config**](docs/ClusterLinkingV3Api.md#delete_kafka_link_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Reset the given config to default value
*ClusterLinkingV3Api* | [**get_kafka_link**](docs/ClusterLinkingV3Api.md#get_kafka_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Describe the cluster link
*ClusterLinkingV3Api* | [**get_kafka_link_configs**](docs/ClusterLinkingV3Api.md#get_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Describe the config under the cluster link
*ClusterLinkingV3Api* | [**list_kafka_link_configs**](docs/ClusterLinkingV3Api.md#list_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs | List all configs of the cluster link
*ClusterLinkingV3Api* | [**list_kafka_links**](docs/ClusterLinkingV3Api.md#list_kafka_links) | **GET** /kafka/v3/clusters/{cluster_id}/links | List all cluster links in the dest cluster
*ClusterLinkingV3Api* | [**list_kafka_mirror_topics**](docs/ClusterLinkingV3Api.md#list_kafka_mirror_topics) | **GET** /kafka/v3/clusters/{cluster_id}/links/-/mirrors | List mirror topics
*ClusterLinkingV3Api* | [**list_kafka_mirror_topics_under_link**](docs/ClusterLinkingV3Api.md#list_kafka_mirror_topics_under_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | List mirror topics
*ClusterLinkingV3Api* | [**read_kafka_mirror_topic**](docs/ClusterLinkingV3Api.md#read_kafka_mirror_topic) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors/{mirror_topic_name} | Describe the mirror topic
*ClusterLinkingV3Api* | [**update_kafka_link_config**](docs/ClusterLinkingV3Api.md#update_kafka_link_config) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Alter the config under the cluster link
*ClusterLinkingV3Api* | [**update_kafka_link_config_batch**](docs/ClusterLinkingV3Api.md#update_kafka_link_config_batch) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs:alter | Batch Alter Cluster Link Configs
*ClusterLinkingV3Api* | [**update_kafka_mirror_topics_failover**](docs/ClusterLinkingV3Api.md#update_kafka_mirror_topics_failover) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:failover | Failover the mirror topics
*ClusterLinkingV3Api* | [**update_kafka_mirror_topics_pause**](docs/ClusterLinkingV3Api.md#update_kafka_mirror_topics_pause) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:pause | Pause the mirror topics
*ClusterLinkingV3Api* | [**update_kafka_mirror_topics_promote**](docs/ClusterLinkingV3Api.md#update_kafka_mirror_topics_promote) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:promote | Promote the mirror topics
*ClusterLinkingV3Api* | [**update_kafka_mirror_topics_resume**](docs/ClusterLinkingV3Api.md#update_kafka_mirror_topics_resume) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:resume | Resume the mirror topics
*ClusterV3Api* | [**get_kafka_cluster**](docs/ClusterV3Api.md#get_kafka_cluster) | **GET** /kafka/v3/clusters/{cluster_id} | Get Cluster
*ClustersCmkV2Api* | [**create_cmk_v2_cluster**](docs/ClustersCmkV2Api.md#create_cmk_v2_cluster) | **POST** /cmk/v2/clusters | Create a Cluster
*ClustersCmkV2Api* | [**delete_cmk_v2_cluster**](docs/ClustersCmkV2Api.md#delete_cmk_v2_cluster) | **DELETE** /cmk/v2/clusters/{id} | Delete a Cluster
*ClustersCmkV2Api* | [**get_cmk_v2_cluster**](docs/ClustersCmkV2Api.md#get_cmk_v2_cluster) | **GET** /cmk/v2/clusters/{id} | Read a Cluster
*ClustersCmkV2Api* | [**list_cmk_v2_clusters**](docs/ClustersCmkV2Api.md#list_cmk_v2_clusters) | **GET** /cmk/v2/clusters | List of Clusters
*ClustersCmkV2Api* | [**update_cmk_v2_cluster**](docs/ClustersCmkV2Api.md#update_cmk_v2_cluster) | **PATCH** /cmk/v2/clusters/{id} | Update a Cluster
*ClustersKsqldbcmV2Api* | [**create_ksqldbcm_v2_cluster**](docs/ClustersKsqldbcmV2Api.md#create_ksqldbcm_v2_cluster) | **POST** /ksqldbcm/v2/clusters | Create a Cluster
*ClustersKsqldbcmV2Api* | [**delete_ksqldbcm_v2_cluster**](docs/ClustersKsqldbcmV2Api.md#delete_ksqldbcm_v2_cluster) | **DELETE** /ksqldbcm/v2/clusters/{id} | Delete a Cluster
*ClustersKsqldbcmV2Api* | [**get_ksqldbcm_v2_cluster**](docs/ClustersKsqldbcmV2Api.md#get_ksqldbcm_v2_cluster) | **GET** /ksqldbcm/v2/clusters/{id} | Read a Cluster
*ClustersKsqldbcmV2Api* | [**list_ksqldbcm_v2_clusters**](docs/ClustersKsqldbcmV2Api.md#list_ksqldbcm_v2_clusters) | **GET** /ksqldbcm/v2/clusters | List of Clusters
*ClustersSrcmV2Api* | [**create_srcm_v2_cluster**](docs/ClustersSrcmV2Api.md#create_srcm_v2_cluster) | **POST** /srcm/v2/clusters | Create a Cluster
*ClustersSrcmV2Api* | [**delete_srcm_v2_cluster**](docs/ClustersSrcmV2Api.md#delete_srcm_v2_cluster) | **DELETE** /srcm/v2/clusters/{id} | Delete a Cluster
*ClustersSrcmV2Api* | [**get_srcm_v2_cluster**](docs/ClustersSrcmV2Api.md#get_srcm_v2_cluster) | **GET** /srcm/v2/clusters/{id} | Read a Cluster
*ClustersSrcmV2Api* | [**list_srcm_v2_clusters**](docs/ClustersSrcmV2Api.md#list_srcm_v2_clusters) | **GET** /srcm/v2/clusters | List of Clusters
*ClustersSrcmV2Api* | [**update_srcm_v2_cluster**](docs/ClustersSrcmV2Api.md#update_srcm_v2_cluster) | **PATCH** /srcm/v2/clusters/{id} | Update a Cluster
*ClustersSrcmV3Api* | [**get_srcm_v3_cluster**](docs/ClustersSrcmV3Api.md#get_srcm_v3_cluster) | **GET** /srcm/v3/clusters/{id} | Read a Cluster
*ClustersSrcmV3Api* | [**list_srcm_v3_clusters**](docs/ClustersSrcmV3Api.md#list_srcm_v3_clusters) | **GET** /srcm/v3/clusters | List of Clusters
*CompatibilityV1Api* | [**test_compatibility_by_subject_name**](docs/CompatibilityV1Api.md#test_compatibility_by_subject_name) | **POST** /compatibility/subjects/{subject}/versions/{version} | Test schema compatibility against a particular schema subject-version
*CompatibilityV1Api* | [**test_compatibility_for_subject**](docs/CompatibilityV1Api.md#test_compatibility_for_subject) | **POST** /compatibility/subjects/{subject}/versions | Test schema compatibility against all schemas under a subject
*ComputePoolsFcpmV2Api* | [**create_fcpm_v2_compute_pool**](docs/ComputePoolsFcpmV2Api.md#create_fcpm_v2_compute_pool) | **POST** /fcpm/v2/compute-pools | Create a Compute Pool
*ComputePoolsFcpmV2Api* | [**delete_fcpm_v2_compute_pool**](docs/ComputePoolsFcpmV2Api.md#delete_fcpm_v2_compute_pool) | **DELETE** /fcpm/v2/compute-pools/{id} | Delete a Compute Pool
*ComputePoolsFcpmV2Api* | [**get_fcpm_v2_compute_pool**](docs/ComputePoolsFcpmV2Api.md#get_fcpm_v2_compute_pool) | **GET** /fcpm/v2/compute-pools/{id} | Read a Compute Pool
*ComputePoolsFcpmV2Api* | [**list_fcpm_v2_compute_pools**](docs/ComputePoolsFcpmV2Api.md#list_fcpm_v2_compute_pools) | **GET** /fcpm/v2/compute-pools | List of Compute Pools
*ComputePoolsFcpmV2Api* | [**update_fcpm_v2_compute_pool**](docs/ComputePoolsFcpmV2Api.md#update_fcpm_v2_compute_pool) | **PATCH** /fcpm/v2/compute-pools/{id} | Update a Compute Pool
*ConfigV1Api* | [**delete_subject_config**](docs/ConfigV1Api.md#delete_subject_config) | **DELETE** /config/{subject} | Delete subject compatibility level
*ConfigV1Api* | [**delete_top_level_config**](docs/ConfigV1Api.md#delete_top_level_config) | **DELETE** /config | Delete global compatibility level
*ConfigV1Api* | [**get_cluster_config**](docs/ConfigV1Api.md#get_cluster_config) | **GET** /clusterconfig | Get cluster config
*ConfigV1Api* | [**get_subject_level_config**](docs/ConfigV1Api.md#get_subject_level_config) | **GET** /config/{subject} | Get subject compatibility level
*ConfigV1Api* | [**get_top_level_config**](docs/ConfigV1Api.md#get_top_level_config) | **GET** /config | Get global compatibility level
*ConfigV1Api* | [**update_subject_level_config**](docs/ConfigV1Api.md#update_subject_level_config) | **PUT** /config/{subject} | Update subject compatibility level
*ConfigV1Api* | [**update_top_level_config**](docs/ConfigV1Api.md#update_top_level_config) | **PUT** /config | Update global compatibility level
*ConfigsV3Api* | [**delete_kafka_cluster_config**](docs/ConfigsV3Api.md#delete_kafka_cluster_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Reset Dynamic Broker Config
*ConfigsV3Api* | [**delete_kafka_topic_config**](docs/ConfigsV3Api.md#delete_kafka_topic_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Reset Topic Config
*ConfigsV3Api* | [**get_kafka_cluster_config**](docs/ConfigsV3Api.md#get_kafka_cluster_config) | **GET** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Get Dynamic Broker Config
*ConfigsV3Api* | [**get_kafka_topic_config**](docs/ConfigsV3Api.md#get_kafka_topic_config) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Get Topic Config
*ConfigsV3Api* | [**list_kafka_all_topic_configs**](docs/ConfigsV3Api.md#list_kafka_all_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/-/configs | List All Topic Configs
*ConfigsV3Api* | [**list_kafka_cluster_configs**](docs/ConfigsV3Api.md#list_kafka_cluster_configs) | **GET** /kafka/v3/clusters/{cluster_id}/broker-configs | List Dynamic Broker Configs
*ConfigsV3Api* | [**list_kafka_default_topic_configs**](docs/ConfigsV3Api.md#list_kafka_default_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/default-configs | List New Topic Default Configs
*ConfigsV3Api* | [**list_kafka_topic_configs**](docs/ConfigsV3Api.md#list_kafka_topic_configs) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs | List Topic Configs
*ConfigsV3Api* | [**update_kafka_cluster_config**](docs/ConfigsV3Api.md#update_kafka_cluster_config) | **PUT** /kafka/v3/clusters/{cluster_id}/broker-configs/{name} | Update Dynamic Broker Config
*ConfigsV3Api* | [**update_kafka_cluster_configs**](docs/ConfigsV3Api.md#update_kafka_cluster_configs) | **POST** /kafka/v3/clusters/{cluster_id}/broker-configs:alter | Batch Alter Dynamic Broker Configs
*ConfigsV3Api* | [**update_kafka_topic_config**](docs/ConfigsV3Api.md#update_kafka_topic_config) | **PUT** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs/{name} | Update Topic Config
*ConfigsV3Api* | [**update_kafka_topic_config_batch**](docs/ConfigsV3Api.md#update_kafka_topic_config_batch) | **POST** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/configs:alter | Batch Alter Topic Configs
*ConnectorsConnectV1Api* | [**create_connectv1_connector**](docs/ConnectorsConnectV1Api.md#create_connectv1_connector) | **POST** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | Create a Connector
*ConnectorsConnectV1Api* | [**create_or_update_connectv1_connector_config**](docs/ConnectorsConnectV1Api.md#create_or_update_connectv1_connector_config) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Create or Update a Connector Configuration
*ConnectorsConnectV1Api* | [**delete_connectv1_connector**](docs/ConnectorsConnectV1Api.md#delete_connectv1_connector) | **DELETE** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Delete a Connector
*ConnectorsConnectV1Api* | [**get_connectv1_connector_config**](docs/ConnectorsConnectV1Api.md#get_connectv1_connector_config) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Read a Connector Configuration
*ConnectorsConnectV1Api* | [**list_connectv1_connectors**](docs/ConnectorsConnectV1Api.md#list_connectv1_connectors) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | List of Connectors
*ConnectorsConnectV1Api* | [**list_connectv1_connectors_with_expansions**](docs/ConnectorsConnectV1Api.md#list_connectv1_connectors_with_expansions) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors?expand&#x3D;info,status,id | List of Connectors with Expansions
*ConnectorsConnectV1Api* | [**read_connectv1_connector**](docs/ConnectorsConnectV1Api.md#read_connectv1_connector) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Read a Connector
*ConsumerGroupV3Api* | [**get_kafka_consumer**](docs/ConsumerGroupV3Api.md#get_kafka_consumer) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/consumers/{consumer_id} | Get Consumer
*ConsumerGroupV3Api* | [**get_kafka_consumer_group**](docs/ConsumerGroupV3Api.md#get_kafka_consumer_group) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id} | Get Consumer Group
*ConsumerGroupV3Api* | [**get_kafka_consumer_group_lag_summary**](docs/ConsumerGroupV3Api.md#get_kafka_consumer_group_lag_summary) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lag-summary | Get Consumer Group Lag Summary
*ConsumerGroupV3Api* | [**get_kafka_consumer_lag**](docs/ConsumerGroupV3Api.md#get_kafka_consumer_lag) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lags/{topic_name}/partitions/{partition_id} | Get Consumer Lag
*ConsumerGroupV3Api* | [**list_kafka_consumer_groups**](docs/ConsumerGroupV3Api.md#list_kafka_consumer_groups) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups | List Consumer Groups
*ConsumerGroupV3Api* | [**list_kafka_consumer_lags**](docs/ConsumerGroupV3Api.md#list_kafka_consumer_lags) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/lags | List Consumer Lags
*ConsumerGroupV3Api* | [**list_kafka_consumers**](docs/ConsumerGroupV3Api.md#list_kafka_consumers) | **GET** /kafka/v3/clusters/{cluster_id}/consumer-groups/{consumer_group_id}/consumers | List Consumers
*ConsumerSharedResourcesCdxV1Api* | [**get_cdx_v1_consumer_shared_resource**](docs/ConsumerSharedResourcesCdxV1Api.md#get_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id} | Read a Consumer Shared Resource
*ConsumerSharedResourcesCdxV1Api* | [**image_cdx_v1_consumer_shared_resource**](docs/ConsumerSharedResourcesCdxV1Api.md#image_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id}/images/{file_name} | Get image for shared resource
*ConsumerSharedResourcesCdxV1Api* | [**list_cdx_v1_consumer_shared_resources**](docs/ConsumerSharedResourcesCdxV1Api.md#list_cdx_v1_consumer_shared_resources) | **GET** /cdx/v1/consumer-shared-resources | List of Consumer Shared Resources
*ConsumerSharedResourcesCdxV1Api* | [**network_cdx_v1_consumer_shared_resource**](docs/ConsumerSharedResourcesCdxV1Api.md#network_cdx_v1_consumer_shared_resource) | **GET** /cdx/v1/consumer-shared-resources/{id}:network | Get shared resource&#39;s network configuration
*ConsumerSharesCdxV1Api* | [**delete_cdx_v1_consumer_share**](docs/ConsumerSharesCdxV1Api.md#delete_cdx_v1_consumer_share) | **DELETE** /cdx/v1/consumer-shares/{id} | Delete a Consumer Share
*ConsumerSharesCdxV1Api* | [**get_cdx_v1_consumer_share**](docs/ConsumerSharesCdxV1Api.md#get_cdx_v1_consumer_share) | **GET** /cdx/v1/consumer-shares/{id} | Read a Consumer Share
*ConsumerSharesCdxV1Api* | [**list_cdx_v1_consumer_shares**](docs/ConsumerSharesCdxV1Api.md#list_cdx_v1_consumer_shares) | **GET** /cdx/v1/consumer-shares | List of Consumer Shares
*ContextsV1Api* | [**list_contexts**](docs/ContextsV1Api.md#list_contexts) | **GET** /contexts | List contexts
*CostsBillingV1Api* | [**list_billing_v1_costs**](docs/CostsBillingV1Api.md#list_billing_v1_costs) | **GET** /billing/v1/costs | List of Costs
*CustomConnectorPluginsConnectV1Api* | [**create_connect_v1_custom_connector_plugin**](docs/CustomConnectorPluginsConnectV1Api.md#create_connect_v1_custom_connector_plugin) | **POST** /connect/v1/custom-connector-plugins | Create a Custom Connector Plugin
*CustomConnectorPluginsConnectV1Api* | [**delete_connect_v1_custom_connector_plugin**](docs/CustomConnectorPluginsConnectV1Api.md#delete_connect_v1_custom_connector_plugin) | **DELETE** /connect/v1/custom-connector-plugins/{id} | Delete a Custom Connector Plugin
*CustomConnectorPluginsConnectV1Api* | [**get_connect_v1_custom_connector_plugin**](docs/CustomConnectorPluginsConnectV1Api.md#get_connect_v1_custom_connector_plugin) | **GET** /connect/v1/custom-connector-plugins/{id} | Read a Custom Connector Plugin
*CustomConnectorPluginsConnectV1Api* | [**list_connect_v1_custom_connector_plugins**](docs/CustomConnectorPluginsConnectV1Api.md#list_connect_v1_custom_connector_plugins) | **GET** /connect/v1/custom-connector-plugins | List of Custom Connector Plugins
*CustomConnectorPluginsConnectV1Api* | [**update_connect_v1_custom_connector_plugin**](docs/CustomConnectorPluginsConnectV1Api.md#update_connect_v1_custom_connector_plugin) | **PATCH** /connect/v1/custom-connector-plugins/{id} | Update a Custom Connector Plugin
*EntitlementsPartnerV2Api* | [**create_partner_v2_entitlement**](docs/EntitlementsPartnerV2Api.md#create_partner_v2_entitlement) | **POST** /partner/v2/entitlements | Create an Entitlement
*EntitlementsPartnerV2Api* | [**get_partner_v2_entitlement**](docs/EntitlementsPartnerV2Api.md#get_partner_v2_entitlement) | **GET** /partner/v2/entitlements/{id} | Read an Entitlement
*EntitlementsPartnerV2Api* | [**list_partner_v2_entitlements**](docs/EntitlementsPartnerV2Api.md#list_partner_v2_entitlements) | **GET** /partner/v2/entitlements | List of Entitlements
*EntityV1Api* | [**create_business_metadata**](docs/EntityV1Api.md#create_business_metadata) | **POST** /catalog/v1/entity/businessmetadata | Bulk Create Business Metadata
*EntityV1Api* | [**create_tags**](docs/EntityV1Api.md#create_tags) | **POST** /catalog/v1/entity/tags | Bulk Create Tags
*EntityV1Api* | [**delete_business_metadata**](docs/EntityV1Api.md#delete_business_metadata) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata/{bmName} | Delete a Business Metadata for an Entity
*EntityV1Api* | [**delete_tag**](docs/EntityV1Api.md#delete_tag) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags/{tagName} | Delete a Tag for an Entity
*EntityV1Api* | [**get_business_metadata**](docs/EntityV1Api.md#get_business_metadata) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata | Read Business Metadata for an Entity
*EntityV1Api* | [**get_by_unique_attributes**](docs/EntityV1Api.md#get_by_unique_attributes) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName} | Read an Entity
*EntityV1Api* | [**get_tags**](docs/EntityV1Api.md#get_tags) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags | Read Tags for an Entity
*EntityV1Api* | [**partial_entity_update**](docs/EntityV1Api.md#partial_entity_update) | **PUT** /catalog/v1/entity | Update an Entity Attribute
*EntityV1Api* | [**update_business_metadata**](docs/EntityV1Api.md#update_business_metadata) | **PUT** /catalog/v1/entity/businessmetadata | Bulk Update Business Metadata
*EntityV1Api* | [**update_tags**](docs/EntityV1Api.md#update_tags) | **PUT** /catalog/v1/entity/tags | Bulk Update Tags
*EnvironmentsOrgV2Api* | [**create_org_v2_environment**](docs/EnvironmentsOrgV2Api.md#create_org_v2_environment) | **POST** /org/v2/environments | Create an Environment
*EnvironmentsOrgV2Api* | [**delete_org_v2_environment**](docs/EnvironmentsOrgV2Api.md#delete_org_v2_environment) | **DELETE** /org/v2/environments/{id} | Delete an Environment
*EnvironmentsOrgV2Api* | [**get_org_v2_environment**](docs/EnvironmentsOrgV2Api.md#get_org_v2_environment) | **GET** /org/v2/environments/{id} | Read an Environment
*EnvironmentsOrgV2Api* | [**list_org_v2_environments**](docs/EnvironmentsOrgV2Api.md#list_org_v2_environments) | **GET** /org/v2/environments | List of Environments
*EnvironmentsOrgV2Api* | [**update_org_v2_environment**](docs/EnvironmentsOrgV2Api.md#update_org_v2_environment) | **PATCH** /org/v2/environments/{id} | Update an Environment
*ExportersV1Api* | [**delete_exporter**](docs/ExportersV1Api.md#delete_exporter) | **DELETE** /exporters/{name} | Delete schema exporter by name.
*ExportersV1Api* | [**get_exporter_config_by_name**](docs/ExportersV1Api.md#get_exporter_config_by_name) | **GET** /exporters/{name}/config | Gets schema exporter config by name.
*ExportersV1Api* | [**get_exporter_info_by_name**](docs/ExportersV1Api.md#get_exporter_info_by_name) | **GET** /exporters/{name} | Gets schema exporter by name.
*ExportersV1Api* | [**get_exporter_status_by_name**](docs/ExportersV1Api.md#get_exporter_status_by_name) | **GET** /exporters/{name}/status | Gets schema exporter status by name.
*ExportersV1Api* | [**list_exporters**](docs/ExportersV1Api.md#list_exporters) | **GET** /exporters | Gets all schema exporters.
*ExportersV1Api* | [**pause_exporter_by_name**](docs/ExportersV1Api.md#pause_exporter_by_name) | **PUT** /exporters/{name}/pause | Pause schema exporter by name.
*ExportersV1Api* | [**register_exporter**](docs/ExportersV1Api.md#register_exporter) | **POST** /exporters | Creates a new schema exporter.
*ExportersV1Api* | [**reset_exporter_by_name**](docs/ExportersV1Api.md#reset_exporter_by_name) | **PUT** /exporters/{name}/reset | Reset schema exporter by name.
*ExportersV1Api* | [**resume_exporter_by_name**](docs/ExportersV1Api.md#resume_exporter_by_name) | **PUT** /exporters/{name}/resume | Resume schema exporter by name.
*ExportersV1Api* | [**update_exporter_config_by_name**](docs/ExportersV1Api.md#update_exporter_config_by_name) | **PUT** /exporters/{name}/config | Update schema exporter config by name.
*ExportersV1Api* | [**update_exporter_info**](docs/ExportersV1Api.md#update_exporter_info) | **PUT** /exporters/{name} | Update schema exporter by name.
*GroupMappingsIamV2SsoApi* | [**create_iam_v2_sso_group_mapping**](docs/GroupMappingsIamV2SsoApi.md#create_iam_v2_sso_group_mapping) | **POST** /iam/v2/sso/group-mappings | Create a Group Mapping
*GroupMappingsIamV2SsoApi* | [**delete_iam_v2_sso_group_mapping**](docs/GroupMappingsIamV2SsoApi.md#delete_iam_v2_sso_group_mapping) | **DELETE** /iam/v2/sso/group-mappings/{id} | Delete a Group Mapping
*GroupMappingsIamV2SsoApi* | [**get_iam_v2_sso_group_mapping**](docs/GroupMappingsIamV2SsoApi.md#get_iam_v2_sso_group_mapping) | **GET** /iam/v2/sso/group-mappings/{id} | Read a Group Mapping
*GroupMappingsIamV2SsoApi* | [**list_iam_v2_sso_group_mappings**](docs/GroupMappingsIamV2SsoApi.md#list_iam_v2_sso_group_mappings) | **GET** /iam/v2/sso/group-mappings | List of Group Mappings
*GroupMappingsIamV2SsoApi* | [**update_iam_v2_sso_group_mapping**](docs/GroupMappingsIamV2SsoApi.md#update_iam_v2_sso_group_mapping) | **PATCH** /iam/v2/sso/group-mappings/{id} | Update a Group Mapping
*IPAddressesNetworkingV1Api* | [**list_networking_v1_ip_addresses**](docs/IPAddressesNetworkingV1Api.md#list_networking_v1_ip_addresses) | **GET** /networking/v1/ip-addresses | List of IP Addresses
*IPFiltersIamV2Api* | [**create_iam_v2_ip_filter**](docs/IPFiltersIamV2Api.md#create_iam_v2_ip_filter) | **POST** /iam/v2/ip-filters | Create an IP Filter
*IPFiltersIamV2Api* | [**delete_iam_v2_ip_filter**](docs/IPFiltersIamV2Api.md#delete_iam_v2_ip_filter) | **DELETE** /iam/v2/ip-filters/{id} | Delete an IP Filter
*IPFiltersIamV2Api* | [**get_iam_v2_ip_filter**](docs/IPFiltersIamV2Api.md#get_iam_v2_ip_filter) | **GET** /iam/v2/ip-filters/{id} | Read an IP Filter
*IPFiltersIamV2Api* | [**list_iam_v2_ip_filters**](docs/IPFiltersIamV2Api.md#list_iam_v2_ip_filters) | **GET** /iam/v2/ip-filters | List of IP Filters
*IPFiltersIamV2Api* | [**update_iam_v2_ip_filter**](docs/IPFiltersIamV2Api.md#update_iam_v2_ip_filter) | **PATCH** /iam/v2/ip-filters/{id} | Update an IP Filter
*IPGroupsIamV2Api* | [**create_iam_v2_ip_group**](docs/IPGroupsIamV2Api.md#create_iam_v2_ip_group) | **POST** /iam/v2/ip-groups | Create an IP Group
*IPGroupsIamV2Api* | [**delete_iam_v2_ip_group**](docs/IPGroupsIamV2Api.md#delete_iam_v2_ip_group) | **DELETE** /iam/v2/ip-groups/{id} | Delete an IP Group
*IPGroupsIamV2Api* | [**get_iam_v2_ip_group**](docs/IPGroupsIamV2Api.md#get_iam_v2_ip_group) | **GET** /iam/v2/ip-groups/{id} | Read an IP Group
*IPGroupsIamV2Api* | [**list_iam_v2_ip_groups**](docs/IPGroupsIamV2Api.md#list_iam_v2_ip_groups) | **GET** /iam/v2/ip-groups | List of IP Groups
*IPGroupsIamV2Api* | [**update_iam_v2_ip_group**](docs/IPGroupsIamV2Api.md#update_iam_v2_ip_group) | **PATCH** /iam/v2/ip-groups/{id} | Update an IP Group
*IdentityPoolsIamV2Api* | [**create_iam_v2_identity_pool**](docs/IdentityPoolsIamV2Api.md#create_iam_v2_identity_pool) | **POST** /iam/v2/identity-providers/{provider_id}/identity-pools | Create an Identity Pool
*IdentityPoolsIamV2Api* | [**delete_iam_v2_identity_pool**](docs/IdentityPoolsIamV2Api.md#delete_iam_v2_identity_pool) | **DELETE** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Delete an Identity Pool
*IdentityPoolsIamV2Api* | [**get_iam_v2_identity_pool**](docs/IdentityPoolsIamV2Api.md#get_iam_v2_identity_pool) | **GET** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Read an Identity Pool
*IdentityPoolsIamV2Api* | [**list_iam_v2_identity_pools**](docs/IdentityPoolsIamV2Api.md#list_iam_v2_identity_pools) | **GET** /iam/v2/identity-providers/{provider_id}/identity-pools | List of Identity Pools
*IdentityPoolsIamV2Api* | [**update_iam_v2_identity_pool**](docs/IdentityPoolsIamV2Api.md#update_iam_v2_identity_pool) | **PATCH** /iam/v2/identity-providers/{provider_id}/identity-pools/{id} | Update an Identity Pool
*IdentityProvidersIamV2Api* | [**create_iam_v2_identity_provider**](docs/IdentityProvidersIamV2Api.md#create_iam_v2_identity_provider) | **POST** /iam/v2/identity-providers | Create an Identity Provider
*IdentityProvidersIamV2Api* | [**delete_iam_v2_identity_provider**](docs/IdentityProvidersIamV2Api.md#delete_iam_v2_identity_provider) | **DELETE** /iam/v2/identity-providers/{id} | Delete an Identity Provider
*IdentityProvidersIamV2Api* | [**get_iam_v2_identity_provider**](docs/IdentityProvidersIamV2Api.md#get_iam_v2_identity_provider) | **GET** /iam/v2/identity-providers/{id} | Read an Identity Provider
*IdentityProvidersIamV2Api* | [**list_iam_v2_identity_providers**](docs/IdentityProvidersIamV2Api.md#list_iam_v2_identity_providers) | **GET** /iam/v2/identity-providers | List of Identity Providers
*IdentityProvidersIamV2Api* | [**update_iam_v2_identity_provider**](docs/IdentityProvidersIamV2Api.md#update_iam_v2_identity_provider) | **PATCH** /iam/v2/identity-providers/{id} | Update an Identity Provider
*IntegrationsNotificationsV1Api* | [**create_notifications_v1_integration**](docs/IntegrationsNotificationsV1Api.md#create_notifications_v1_integration) | **POST** /notifications/v1/integrations | Create an Integration
*IntegrationsNotificationsV1Api* | [**delete_notifications_v1_integration**](docs/IntegrationsNotificationsV1Api.md#delete_notifications_v1_integration) | **DELETE** /notifications/v1/integrations/{id} | Delete an Integration
*IntegrationsNotificationsV1Api* | [**get_notifications_v1_integration**](docs/IntegrationsNotificationsV1Api.md#get_notifications_v1_integration) | **GET** /notifications/v1/integrations/{id} | Read an Integration
*IntegrationsNotificationsV1Api* | [**list_notifications_v1_integrations**](docs/IntegrationsNotificationsV1Api.md#list_notifications_v1_integrations) | **GET** /notifications/v1/integrations | List of Integrations
*IntegrationsNotificationsV1Api* | [**test_notifications_v1_integration**](docs/IntegrationsNotificationsV1Api.md#test_notifications_v1_integration) | **POST** /notifications/v1/integrations:test | Test a Webhook, Slack or Microsoft Teams integration
*IntegrationsNotificationsV1Api* | [**update_notifications_v1_integration**](docs/IntegrationsNotificationsV1Api.md#update_notifications_v1_integration) | **PATCH** /notifications/v1/integrations/{id} | Update an Integration
*InvitationsIamV2Api* | [**create_iam_v2_invitation**](docs/InvitationsIamV2Api.md#create_iam_v2_invitation) | **POST** /iam/v2/invitations | Create an Invitation
*InvitationsIamV2Api* | [**delete_iam_v2_invitation**](docs/InvitationsIamV2Api.md#delete_iam_v2_invitation) | **DELETE** /iam/v2/invitations/{id} | Delete an Invitation
*InvitationsIamV2Api* | [**get_iam_v2_invitation**](docs/InvitationsIamV2Api.md#get_iam_v2_invitation) | **GET** /iam/v2/invitations/{id} | Read an Invitation
*InvitationsIamV2Api* | [**list_iam_v2_invitations**](docs/InvitationsIamV2Api.md#list_iam_v2_invitations) | **GET** /iam/v2/invitations | List of Invitations
*JwksIamV2Api* | [**refresh_iam_v2_json_web_key_set**](docs/JwksIamV2Api.md#refresh_iam_v2_json_web_key_set) | **PATCH** /iam/v2/identity-providers/{provider_id}/jwks | Refresh a provider&#39;s JWKS
*KeysByokV1Api* | [**create_byok_v1_key**](docs/KeysByokV1Api.md#create_byok_v1_key) | **POST** /byok/v1/keys | Create a Key
*KeysByokV1Api* | [**delete_byok_v1_key**](docs/KeysByokV1Api.md#delete_byok_v1_key) | **DELETE** /byok/v1/keys/{id} | Delete a Key
*KeysByokV1Api* | [**get_byok_v1_key**](docs/KeysByokV1Api.md#get_byok_v1_key) | **GET** /byok/v1/keys/{id} | Read a Key
*KeysByokV1Api* | [**list_byok_v1_keys**](docs/KeysByokV1Api.md#list_byok_v1_keys) | **GET** /byok/v1/keys | List of Keys
*LifecycleConnectV1Api* | [**pause_connectv1_connector**](docs/LifecycleConnectV1Api.md#pause_connectv1_connector) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/pause | Pause a Connector
*LifecycleConnectV1Api* | [**resume_connectv1_connector**](docs/LifecycleConnectV1Api.md#resume_connectv1_connector) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/resume | Resume a Connector
*ManagedConnectorPluginsConnectV1Api* | [**list_connectv1_connector_plugins**](docs/ManagedConnectorPluginsConnectV1Api.md#list_connectv1_connector_plugins) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connector-plugins | List of Managed Connector plugins
*ManagedConnectorPluginsConnectV1Api* | [**validate_connectv1_connector_plugin**](docs/ManagedConnectorPluginsConnectV1Api.md#validate_connectv1_connector_plugin) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connector-plugins/{plugin_name}/config/validate | Validate a Managed Connector Plugin
*ModesV1Api* | [**delete_subject_mode**](docs/ModesV1Api.md#delete_subject_mode) | **DELETE** /mode/{subject} | Delete subject mode
*ModesV1Api* | [**get_mode**](docs/ModesV1Api.md#get_mode) | **GET** /mode/{subject} | Get subject mode
*ModesV1Api* | [**get_top_level_mode**](docs/ModesV1Api.md#get_top_level_mode) | **GET** /mode | Get global mode
*ModesV1Api* | [**update_mode**](docs/ModesV1Api.md#update_mode) | **PUT** /mode/{subject} | Update subject mode
*ModesV1Api* | [**update_top_level_mode**](docs/ModesV1Api.md#update_top_level_mode) | **PUT** /mode | Update global mode
*NetworkLinkEndpointsNetworkingV1Api* | [**create_networking_v1_network_link_endpoint**](docs/NetworkLinkEndpointsNetworkingV1Api.md#create_networking_v1_network_link_endpoint) | **POST** /networking/v1/network-link-endpoints | Create a Network Link Endpoint
*NetworkLinkEndpointsNetworkingV1Api* | [**delete_networking_v1_network_link_endpoint**](docs/NetworkLinkEndpointsNetworkingV1Api.md#delete_networking_v1_network_link_endpoint) | **DELETE** /networking/v1/network-link-endpoints/{id} | Delete a Network Link Endpoint
*NetworkLinkEndpointsNetworkingV1Api* | [**get_networking_v1_network_link_endpoint**](docs/NetworkLinkEndpointsNetworkingV1Api.md#get_networking_v1_network_link_endpoint) | **GET** /networking/v1/network-link-endpoints/{id} | Read a Network Link Endpoint
*NetworkLinkEndpointsNetworkingV1Api* | [**list_networking_v1_network_link_endpoints**](docs/NetworkLinkEndpointsNetworkingV1Api.md#list_networking_v1_network_link_endpoints) | **GET** /networking/v1/network-link-endpoints | List of Network Link Endpoints
*NetworkLinkEndpointsNetworkingV1Api* | [**update_networking_v1_network_link_endpoint**](docs/NetworkLinkEndpointsNetworkingV1Api.md#update_networking_v1_network_link_endpoint) | **PATCH** /networking/v1/network-link-endpoints/{id} | Update a Network Link Endpoint
*NetworkLinkServiceAssociationsNetworkingV1Api* | [**get_networking_v1_network_link_service_association**](docs/NetworkLinkServiceAssociationsNetworkingV1Api.md#get_networking_v1_network_link_service_association) | **GET** /networking/v1/network-link-service-associations/{id} | Read a Network Link Service Association
*NetworkLinkServiceAssociationsNetworkingV1Api* | [**list_networking_v1_network_link_service_associations**](docs/NetworkLinkServiceAssociationsNetworkingV1Api.md#list_networking_v1_network_link_service_associations) | **GET** /networking/v1/network-link-service-associations | List of Network Link Service Associations
*NetworkLinkServicesNetworkingV1Api* | [**create_networking_v1_network_link_service**](docs/NetworkLinkServicesNetworkingV1Api.md#create_networking_v1_network_link_service) | **POST** /networking/v1/network-link-services | Create a Network Link Service
*NetworkLinkServicesNetworkingV1Api* | [**delete_networking_v1_network_link_service**](docs/NetworkLinkServicesNetworkingV1Api.md#delete_networking_v1_network_link_service) | **DELETE** /networking/v1/network-link-services/{id} | Delete a Network Link Service
*NetworkLinkServicesNetworkingV1Api* | [**get_networking_v1_network_link_service**](docs/NetworkLinkServicesNetworkingV1Api.md#get_networking_v1_network_link_service) | **GET** /networking/v1/network-link-services/{id} | Read a Network Link Service
*NetworkLinkServicesNetworkingV1Api* | [**list_networking_v1_network_link_services**](docs/NetworkLinkServicesNetworkingV1Api.md#list_networking_v1_network_link_services) | **GET** /networking/v1/network-link-services | List of Network Link Services
*NetworkLinkServicesNetworkingV1Api* | [**update_networking_v1_network_link_service**](docs/NetworkLinkServicesNetworkingV1Api.md#update_networking_v1_network_link_service) | **PATCH** /networking/v1/network-link-services/{id} | Update a Network Link Service
*NetworksNetworkingV1Api* | [**create_networking_v1_network**](docs/NetworksNetworkingV1Api.md#create_networking_v1_network) | **POST** /networking/v1/networks | Create a Network
*NetworksNetworkingV1Api* | [**delete_networking_v1_network**](docs/NetworksNetworkingV1Api.md#delete_networking_v1_network) | **DELETE** /networking/v1/networks/{id} | Delete a Network
*NetworksNetworkingV1Api* | [**get_networking_v1_network**](docs/NetworksNetworkingV1Api.md#get_networking_v1_network) | **GET** /networking/v1/networks/{id} | Read a Network
*NetworksNetworkingV1Api* | [**list_networking_v1_networks**](docs/NetworksNetworkingV1Api.md#list_networking_v1_networks) | **GET** /networking/v1/networks | List of Networks
*NetworksNetworkingV1Api* | [**update_networking_v1_network**](docs/NetworksNetworkingV1Api.md#update_networking_v1_network) | **PATCH** /networking/v1/networks/{id} | Update a Network
*NotificationTypesNotificationsV1Api* | [**get_notifications_v1_notification_type**](docs/NotificationTypesNotificationsV1Api.md#get_notifications_v1_notification_type) | **GET** /notifications/v1/notification-types/{id} | Read a Notification Type
*NotificationTypesNotificationsV1Api* | [**list_notifications_v1_notification_types**](docs/NotificationTypesNotificationsV1Api.md#list_notifications_v1_notification_types) | **GET** /notifications/v1/notification-types | List of Notification Types
*OAuthTokensStsV1Api* | [**exchange_sts_v1_oauth_token**](docs/OAuthTokensStsV1Api.md#exchange_sts_v1_oauth_token) | **POST** /sts/v1/oauth2/token | Exchange an OAuth Token
*OptInsCdxV1Api* | [**get_cdx_v1_opt_in**](docs/OptInsCdxV1Api.md#get_cdx_v1_opt_in) | **GET** /cdx/v1/opt-in | Read the organization&#39;s stream sharing opt-in settings
*OptInsCdxV1Api* | [**update_cdx_v1_opt_in**](docs/OptInsCdxV1Api.md#update_cdx_v1_opt_in) | **PATCH** /cdx/v1/opt-in | Set the organization&#39;s stream sharing opt-in settings
*OrganizationsOrgV2Api* | [**get_org_v2_organization**](docs/OrganizationsOrgV2Api.md#get_org_v2_organization) | **GET** /org/v2/organizations/{id} | Read an Organization
*OrganizationsOrgV2Api* | [**list_org_v2_organizations**](docs/OrganizationsOrgV2Api.md#list_org_v2_organizations) | **GET** /org/v2/organizations | List of Organizations
*OrganizationsOrgV2Api* | [**update_org_v2_organization**](docs/OrganizationsOrgV2Api.md#update_org_v2_organization) | **PATCH** /org/v2/organizations/{id} | Update an Organization
*OrganizationsPartnerV2Api* | [**get_partner_v2_organization**](docs/OrganizationsPartnerV2Api.md#get_partner_v2_organization) | **GET** /partner/v2/organizations/{id} | Read an Organization
*OrganizationsPartnerV2Api* | [**list_partner_v2_organizations**](docs/OrganizationsPartnerV2Api.md#list_partner_v2_organizations) | **GET** /partner/v2/organizations | List of Organizations
*PartitionV3Api* | [**get_kafka_partition**](docs/PartitionV3Api.md#get_kafka_partition) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/partitions/{partition_id} | Get Partition
*PartitionV3Api* | [**list_kafka_partitions**](docs/PartitionV3Api.md#list_kafka_partitions) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/partitions | List Partitions
*PeeringsNetworkingV1Api* | [**create_networking_v1_peering**](docs/PeeringsNetworkingV1Api.md#create_networking_v1_peering) | **POST** /networking/v1/peerings | Create a Peering
*PeeringsNetworkingV1Api* | [**delete_networking_v1_peering**](docs/PeeringsNetworkingV1Api.md#delete_networking_v1_peering) | **DELETE** /networking/v1/peerings/{id} | Delete a Peering
*PeeringsNetworkingV1Api* | [**get_networking_v1_peering**](docs/PeeringsNetworkingV1Api.md#get_networking_v1_peering) | **GET** /networking/v1/peerings/{id} | Read a Peering
*PeeringsNetworkingV1Api* | [**list_networking_v1_peerings**](docs/PeeringsNetworkingV1Api.md#list_networking_v1_peerings) | **GET** /networking/v1/peerings | List of Peerings
*PeeringsNetworkingV1Api* | [**update_networking_v1_peering**](docs/PeeringsNetworkingV1Api.md#update_networking_v1_peering) | **PATCH** /networking/v1/peerings/{id} | Update a Peering
*PipelinesSdV1Api* | [**create_sd_v1_pipeline**](docs/PipelinesSdV1Api.md#create_sd_v1_pipeline) | **POST** /sd/v1/pipelines | Create a Pipeline
*PipelinesSdV1Api* | [**delete_sd_v1_pipeline**](docs/PipelinesSdV1Api.md#delete_sd_v1_pipeline) | **DELETE** /sd/v1/pipelines/{id} | Delete a Pipeline
*PipelinesSdV1Api* | [**get_sd_v1_pipeline**](docs/PipelinesSdV1Api.md#get_sd_v1_pipeline) | **GET** /sd/v1/pipelines/{id} | Read a Pipeline
*PipelinesSdV1Api* | [**list_sd_v1_pipelines**](docs/PipelinesSdV1Api.md#list_sd_v1_pipelines) | **GET** /sd/v1/pipelines | List of Pipelines
*PipelinesSdV1Api* | [**update_sd_v1_pipeline**](docs/PipelinesSdV1Api.md#update_sd_v1_pipeline) | **PATCH** /sd/v1/pipelines/{id} | Update a Pipeline
*PresignedUrlsConnectV1Api* | [**presigned_upload_url_connect_v1_presigned_url**](docs/PresignedUrlsConnectV1Api.md#presigned_upload_url_connect_v1_presigned_url) | **POST** /connect/v1/presigned-upload-url | Request a presigned upload URL for a new Custom Connector Plugin.
*PrivateLinkAccessesNetworkingV1Api* | [**create_networking_v1_private_link_access**](docs/PrivateLinkAccessesNetworkingV1Api.md#create_networking_v1_private_link_access) | **POST** /networking/v1/private-link-accesses | Create a Private Link Access
*PrivateLinkAccessesNetworkingV1Api* | [**delete_networking_v1_private_link_access**](docs/PrivateLinkAccessesNetworkingV1Api.md#delete_networking_v1_private_link_access) | **DELETE** /networking/v1/private-link-accesses/{id} | Delete a Private Link Access
*PrivateLinkAccessesNetworkingV1Api* | [**get_networking_v1_private_link_access**](docs/PrivateLinkAccessesNetworkingV1Api.md#get_networking_v1_private_link_access) | **GET** /networking/v1/private-link-accesses/{id} | Read a Private Link Access
*PrivateLinkAccessesNetworkingV1Api* | [**list_networking_v1_private_link_accesses**](docs/PrivateLinkAccessesNetworkingV1Api.md#list_networking_v1_private_link_accesses) | **GET** /networking/v1/private-link-accesses | List of Private Link Accesses
*PrivateLinkAccessesNetworkingV1Api* | [**update_networking_v1_private_link_access**](docs/PrivateLinkAccessesNetworkingV1Api.md#update_networking_v1_private_link_access) | **PATCH** /networking/v1/private-link-accesses/{id} | Update a Private Link Access
*PrivateLinkAttachmentConnectionsNetworkingV1Api* | [**create_networking_v1_private_link_attachment_connection**](docs/PrivateLinkAttachmentConnectionsNetworkingV1Api.md#create_networking_v1_private_link_attachment_connection) | **POST** /networking/v1/private-link-attachment-connections | Create a Private Link Attachment Connection
*PrivateLinkAttachmentConnectionsNetworkingV1Api* | [**delete_networking_v1_private_link_attachment_connection**](docs/PrivateLinkAttachmentConnectionsNetworkingV1Api.md#delete_networking_v1_private_link_attachment_connection) | **DELETE** /networking/v1/private-link-attachment-connections/{id} | Delete a Private Link Attachment Connection
*PrivateLinkAttachmentConnectionsNetworkingV1Api* | [**get_networking_v1_private_link_attachment_connection**](docs/PrivateLinkAttachmentConnectionsNetworkingV1Api.md#get_networking_v1_private_link_attachment_connection) | **GET** /networking/v1/private-link-attachment-connections/{id} | Read a Private Link Attachment Connection
*PrivateLinkAttachmentConnectionsNetworkingV1Api* | [**list_networking_v1_private_link_attachment_connections**](docs/PrivateLinkAttachmentConnectionsNetworkingV1Api.md#list_networking_v1_private_link_attachment_connections) | **GET** /networking/v1/private-link-attachment-connections | List of Private Link Attachment Connections
*PrivateLinkAttachmentConnectionsNetworkingV1Api* | [**update_networking_v1_private_link_attachment_connection**](docs/PrivateLinkAttachmentConnectionsNetworkingV1Api.md#update_networking_v1_private_link_attachment_connection) | **PATCH** /networking/v1/private-link-attachment-connections/{id} | Update a Private Link Attachment Connection
*PrivateLinkAttachmentsNetworkingV1Api* | [**create_networking_v1_private_link_attachment**](docs/PrivateLinkAttachmentsNetworkingV1Api.md#create_networking_v1_private_link_attachment) | **POST** /networking/v1/private-link-attachments | Create a Private Link Attachment
*PrivateLinkAttachmentsNetworkingV1Api* | [**delete_networking_v1_private_link_attachment**](docs/PrivateLinkAttachmentsNetworkingV1Api.md#delete_networking_v1_private_link_attachment) | **DELETE** /networking/v1/private-link-attachments/{id} | Delete a Private Link Attachment
*PrivateLinkAttachmentsNetworkingV1Api* | [**get_networking_v1_private_link_attachment**](docs/PrivateLinkAttachmentsNetworkingV1Api.md#get_networking_v1_private_link_attachment) | **GET** /networking/v1/private-link-attachments/{id} | Read a Private Link Attachment
*PrivateLinkAttachmentsNetworkingV1Api* | [**list_networking_v1_private_link_attachments**](docs/PrivateLinkAttachmentsNetworkingV1Api.md#list_networking_v1_private_link_attachments) | **GET** /networking/v1/private-link-attachments | List of Private Link Attachments
*PrivateLinkAttachmentsNetworkingV1Api* | [**update_networking_v1_private_link_attachment**](docs/PrivateLinkAttachmentsNetworkingV1Api.md#update_networking_v1_private_link_attachment) | **PATCH** /networking/v1/private-link-attachments/{id} | Update a Private Link Attachment
*ProviderSharedResourcesCdxV1Api* | [**delete_image_cdx_v1_provider_shared_resource**](docs/ProviderSharedResourcesCdxV1Api.md#delete_image_cdx_v1_provider_shared_resource) | **DELETE** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Delete the shared resource&#39;s image
*ProviderSharedResourcesCdxV1Api* | [**get_cdx_v1_provider_shared_resource**](docs/ProviderSharedResourcesCdxV1Api.md#get_cdx_v1_provider_shared_resource) | **GET** /cdx/v1/provider-shared-resources/{id} | Read a Provider Shared Resource
*ProviderSharedResourcesCdxV1Api* | [**list_cdx_v1_provider_shared_resources**](docs/ProviderSharedResourcesCdxV1Api.md#list_cdx_v1_provider_shared_resources) | **GET** /cdx/v1/provider-shared-resources | List of Provider Shared Resources
*ProviderSharedResourcesCdxV1Api* | [**update_cdx_v1_provider_shared_resource**](docs/ProviderSharedResourcesCdxV1Api.md#update_cdx_v1_provider_shared_resource) | **PATCH** /cdx/v1/provider-shared-resources/{id} | Update a Provider Shared Resource
*ProviderSharedResourcesCdxV1Api* | [**upload_image_cdx_v1_provider_shared_resource**](docs/ProviderSharedResourcesCdxV1Api.md#upload_image_cdx_v1_provider_shared_resource) | **POST** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Upload image for shared resource
*ProviderSharedResourcesCdxV1Api* | [**view_image_cdx_v1_provider_shared_resource**](docs/ProviderSharedResourcesCdxV1Api.md#view_image_cdx_v1_provider_shared_resource) | **GET** /cdx/v1/provider-shared-resources/{id}/images/{file_name} | Get image for shared resource
*ProviderSharesCdxV1Api* | [**create_cdx_v1_provider_share**](docs/ProviderSharesCdxV1Api.md#create_cdx_v1_provider_share) | **POST** /cdx/v1/provider-shares | Create a provider share
*ProviderSharesCdxV1Api* | [**delete_cdx_v1_provider_share**](docs/ProviderSharesCdxV1Api.md#delete_cdx_v1_provider_share) | **DELETE** /cdx/v1/provider-shares/{id} | Delete a Provider Share
*ProviderSharesCdxV1Api* | [**get_cdx_v1_provider_share**](docs/ProviderSharesCdxV1Api.md#get_cdx_v1_provider_share) | **GET** /cdx/v1/provider-shares/{id} | Read a Provider Share
*ProviderSharesCdxV1Api* | [**list_cdx_v1_provider_shares**](docs/ProviderSharesCdxV1Api.md#list_cdx_v1_provider_shares) | **GET** /cdx/v1/provider-shares | List of Provider Shares
*ProviderSharesCdxV1Api* | [**resend_cdx_v1_provider_share**](docs/ProviderSharesCdxV1Api.md#resend_cdx_v1_provider_share) | **POST** /cdx/v1/provider-shares/{id}:resend | Resend
*RecordsV3Api* | [**produce_record**](docs/RecordsV3Api.md#produce_record) | **POST** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/records | Produce Records
*RegionsFcpmV2Api* | [**list_fcpm_v2_regions**](docs/RegionsFcpmV2Api.md#list_fcpm_v2_regions) | **GET** /fcpm/v2/regions | List of Regions
*RegionsSrcmV2Api* | [**get_srcm_v2_region**](docs/RegionsSrcmV2Api.md#get_srcm_v2_region) | **GET** /srcm/v2/regions/{id} | Read a Region
*RegionsSrcmV2Api* | [**list_srcm_v2_regions**](docs/RegionsSrcmV2Api.md#list_srcm_v2_regions) | **GET** /srcm/v2/regions | List of Regions
*RoleBindingsIamV2Api* | [**create_iam_v2_role_binding**](docs/RoleBindingsIamV2Api.md#create_iam_v2_role_binding) | **POST** /iam/v2/role-bindings | Create a Role Binding
*RoleBindingsIamV2Api* | [**delete_iam_v2_role_binding**](docs/RoleBindingsIamV2Api.md#delete_iam_v2_role_binding) | **DELETE** /iam/v2/role-bindings/{id} | Delete a Role Binding
*RoleBindingsIamV2Api* | [**get_iam_v2_role_binding**](docs/RoleBindingsIamV2Api.md#get_iam_v2_role_binding) | **GET** /iam/v2/role-bindings/{id} | Read a Role Binding
*RoleBindingsIamV2Api* | [**list_iam_v2_role_bindings**](docs/RoleBindingsIamV2Api.md#list_iam_v2_role_bindings) | **GET** /iam/v2/role-bindings | List of Role Bindings
*SchemasV1Api* | [**get_schema**](docs/SchemasV1Api.md#get_schema) | **GET** /schemas/ids/{id} | Get schema string by ID
*SchemasV1Api* | [**get_schema_only**](docs/SchemasV1Api.md#get_schema_only) | **GET** /schemas/ids/{id}/schema | Get schema by ID
*SchemasV1Api* | [**get_schema_types**](docs/SchemasV1Api.md#get_schema_types) | **GET** /schemas/types | List supported schema types
*SchemasV1Api* | [**get_schemas**](docs/SchemasV1Api.md#get_schemas) | **GET** /schemas | List schemas
*SchemasV1Api* | [**get_subjects**](docs/SchemasV1Api.md#get_subjects) | **GET** /schemas/ids/{id}/subjects | List subjects associated to schema ID
*SchemasV1Api* | [**get_versions**](docs/SchemasV1Api.md#get_versions) | **GET** /schemas/ids/{id}/versions | List subject-versions associated to schema ID
*ScopesServiceQuotaV1Api* | [**get_service_quota_v1_scope**](docs/ScopesServiceQuotaV1Api.md#get_service_quota_v1_scope) | **GET** /service-quota/v1/scopes/{id} | Read a Scope
*ScopesServiceQuotaV1Api* | [**list_service_quota_v1_scopes**](docs/ScopesServiceQuotaV1Api.md#list_service_quota_v1_scopes) | **GET** /service-quota/v1/scopes | List of Scopes
*SearchV1Api* | [**search_using_attribute**](docs/SearchV1Api.md#search_using_attribute) | **GET** /catalog/v1/search/attribute | Search by Attribute
*SearchV1Api* | [**search_using_basic**](docs/SearchV1Api.md#search_using_basic) | **GET** /catalog/v1/search/basic | Search by Fulltext Query
*ServiceAccountsIamV2Api* | [**create_iam_v2_service_account**](docs/ServiceAccountsIamV2Api.md#create_iam_v2_service_account) | **POST** /iam/v2/service-accounts | Create a Service Account
*ServiceAccountsIamV2Api* | [**delete_iam_v2_service_account**](docs/ServiceAccountsIamV2Api.md#delete_iam_v2_service_account) | **DELETE** /iam/v2/service-accounts/{id} | Delete a Service Account
*ServiceAccountsIamV2Api* | [**get_iam_v2_service_account**](docs/ServiceAccountsIamV2Api.md#get_iam_v2_service_account) | **GET** /iam/v2/service-accounts/{id} | Read a Service Account
*ServiceAccountsIamV2Api* | [**list_iam_v2_service_accounts**](docs/ServiceAccountsIamV2Api.md#list_iam_v2_service_accounts) | **GET** /iam/v2/service-accounts | List of Service Accounts
*ServiceAccountsIamV2Api* | [**update_iam_v2_service_account**](docs/ServiceAccountsIamV2Api.md#update_iam_v2_service_account) | **PATCH** /iam/v2/service-accounts/{id} | Update a Service Account
*SharedTokensCdxV1Api* | [**redeem_cdx_v1_shared_token**](docs/SharedTokensCdxV1Api.md#redeem_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:redeem | Redeem token
*SharedTokensCdxV1Api* | [**resources_cdx_v1_shared_token**](docs/SharedTokensCdxV1Api.md#resources_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:resources | Validate token to view shared resources
*SignupPartnerV2Api* | [**activate_signup**](docs/SignupPartnerV2Api.md#activate_signup) | **POST** /partner/v2/signup/activate | Activate an Incomplete Signup
*SignupPartnerV2Api* | [**signup**](docs/SignupPartnerV2Api.md#signup) | **POST** /partner/v2/signup | Signup an Organization on behalf of a Customer
*SignupPartnerV2Api* | [**signup_partner_v2_link**](docs/SignupPartnerV2Api.md#signup_partner_v2_link) | **POST** /partner/v2/signup/link | Signup a Customer by Linking to an Existing Organization
*StatementExceptionsSqlV1beta1Api* | [**get_sqlv1beta1_statement_exceptions**](docs/StatementExceptionsSqlV1beta1Api.md#get_sqlv1beta1_statement_exceptions) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name}/exceptions | List of Statement Exceptions
*StatementResultsSqlV1beta1Api* | [**get_sqlv1beta1_statement_result**](docs/StatementResultsSqlV1beta1Api.md#get_sqlv1beta1_statement_result) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{name}/results | Read Statement Result
*StatementsSqlV1beta1Api* | [**create_sqlv1beta1_statement**](docs/StatementsSqlV1beta1Api.md#create_sqlv1beta1_statement) | **POST** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements | Create a Statement
*StatementsSqlV1beta1Api* | [**delete_sqlv1beta1_statement**](docs/StatementsSqlV1beta1Api.md#delete_sqlv1beta1_statement) | **DELETE** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Delete a Statement
*StatementsSqlV1beta1Api* | [**get_sqlv1beta1_statement**](docs/StatementsSqlV1beta1Api.md#get_sqlv1beta1_statement) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Read a Statement
*StatementsSqlV1beta1Api* | [**list_sqlv1beta1_statements**](docs/StatementsSqlV1beta1Api.md#list_sqlv1beta1_statements) | **GET** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements | List of Statements
*StatementsSqlV1beta1Api* | [**update_sqlv1beta1_statement**](docs/StatementsSqlV1beta1Api.md#update_sqlv1beta1_statement) | **PUT** /sql/v1beta1/organizations/{organization_id}/environments/{environment_id}/statements/{statement_name} | Update a Statement
*StatusConnectV1Api* | [**list_connectv1_connector_tasks**](docs/StatusConnectV1Api.md#list_connectv1_connector_tasks) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/tasks | List of Connector Tasks
*StatusConnectV1Api* | [**read_connectv1_connector_status**](docs/StatusConnectV1Api.md#read_connectv1_connector_status) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/status | Read a Connector Status
*SubjectsV1Api* | [**delete_schema_version**](docs/SubjectsV1Api.md#delete_schema_version) | **DELETE** /subjects/{subject}/versions/{version} | Delete schema version
*SubjectsV1Api* | [**delete_subject**](docs/SubjectsV1Api.md#delete_subject) | **DELETE** /subjects/{subject} | Delete subject
*SubjectsV1Api* | [**get_referenced_by**](docs/SubjectsV1Api.md#get_referenced_by) | **GET** /subjects/{subject}/versions/{version}/referencedby | List schemas referencing a schema
*SubjectsV1Api* | [**get_schema_by_version**](docs/SubjectsV1Api.md#get_schema_by_version) | **GET** /subjects/{subject}/versions/{version} | Get schema by version
*SubjectsV1Api* | [**get_schema_only1**](docs/SubjectsV1Api.md#get_schema_only1) | **GET** /subjects/{subject}/versions/{version}/schema | Get schema string by version
*SubjectsV1Api* | [**list**](docs/SubjectsV1Api.md#list) | **GET** /subjects | List subjects
*SubjectsV1Api* | [**list_versions**](docs/SubjectsV1Api.md#list_versions) | **GET** /subjects/{subject}/versions | List versions under subject
*SubjectsV1Api* | [**look_up_schema_under_subject**](docs/SubjectsV1Api.md#look_up_schema_under_subject) | **POST** /subjects/{subject} | Lookup schema under subject
*SubjectsV1Api* | [**register**](docs/SubjectsV1Api.md#register) | **POST** /subjects/{subject}/versions | Register schema under a subject
*SubscriptionsNotificationsV1Api* | [**create_notifications_v1_subscription**](docs/SubscriptionsNotificationsV1Api.md#create_notifications_v1_subscription) | **POST** /notifications/v1/subscriptions | Create a Subscription
*SubscriptionsNotificationsV1Api* | [**delete_notifications_v1_subscription**](docs/SubscriptionsNotificationsV1Api.md#delete_notifications_v1_subscription) | **DELETE** /notifications/v1/subscriptions/{id} | Delete a Subscription
*SubscriptionsNotificationsV1Api* | [**get_notifications_v1_subscription**](docs/SubscriptionsNotificationsV1Api.md#get_notifications_v1_subscription) | **GET** /notifications/v1/subscriptions/{id} | Read a Subscription
*SubscriptionsNotificationsV1Api* | [**list_notifications_v1_subscriptions**](docs/SubscriptionsNotificationsV1Api.md#list_notifications_v1_subscriptions) | **GET** /notifications/v1/subscriptions | List of Subscriptions
*SubscriptionsNotificationsV1Api* | [**update_notifications_v1_subscription**](docs/SubscriptionsNotificationsV1Api.md#update_notifications_v1_subscription) | **PATCH** /notifications/v1/subscriptions/{id} | Update a Subscription
*TopicV3Api* | [**create_kafka_topic**](docs/TopicV3Api.md#create_kafka_topic) | **POST** /kafka/v3/clusters/{cluster_id}/topics | Create Topic
*TopicV3Api* | [**delete_kafka_topic**](docs/TopicV3Api.md#delete_kafka_topic) | **DELETE** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Delete Topic
*TopicV3Api* | [**get_kafka_topic**](docs/TopicV3Api.md#get_kafka_topic) | **GET** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Get Topic
*TopicV3Api* | [**list_kafka_topics**](docs/TopicV3Api.md#list_kafka_topics) | **GET** /kafka/v3/clusters/{cluster_id}/topics | List Topics
*TopicV3Api* | [**update_partition_count_kafka_topic**](docs/TopicV3Api.md#update_partition_count_kafka_topic) | **PATCH** /kafka/v3/clusters/{cluster_id}/topics/{topic_name} | Update Partition Count
*TransitGatewayAttachmentsNetworkingV1Api* | [**create_networking_v1_transit_gateway_attachment**](docs/TransitGatewayAttachmentsNetworkingV1Api.md#create_networking_v1_transit_gateway_attachment) | **POST** /networking/v1/transit-gateway-attachments | Create a Transit Gateway Attachment
*TransitGatewayAttachmentsNetworkingV1Api* | [**delete_networking_v1_transit_gateway_attachment**](docs/TransitGatewayAttachmentsNetworkingV1Api.md#delete_networking_v1_transit_gateway_attachment) | **DELETE** /networking/v1/transit-gateway-attachments/{id} | Delete a Transit Gateway Attachment
*TransitGatewayAttachmentsNetworkingV1Api* | [**get_networking_v1_transit_gateway_attachment**](docs/TransitGatewayAttachmentsNetworkingV1Api.md#get_networking_v1_transit_gateway_attachment) | **GET** /networking/v1/transit-gateway-attachments/{id} | Read a Transit Gateway Attachment
*TransitGatewayAttachmentsNetworkingV1Api* | [**list_networking_v1_transit_gateway_attachments**](docs/TransitGatewayAttachmentsNetworkingV1Api.md#list_networking_v1_transit_gateway_attachments) | **GET** /networking/v1/transit-gateway-attachments | List of Transit Gateway Attachments
*TransitGatewayAttachmentsNetworkingV1Api* | [**update_networking_v1_transit_gateway_attachment**](docs/TransitGatewayAttachmentsNetworkingV1Api.md#update_networking_v1_transit_gateway_attachment) | **PATCH** /networking/v1/transit-gateway-attachments/{id} | Update a Transit Gateway Attachment
*TypesV1Api* | [**create_business_metadata_defs**](docs/TypesV1Api.md#create_business_metadata_defs) | **POST** /catalog/v1/types/businessmetadatadefs | Bulk Create Business Metadata Definitions
*TypesV1Api* | [**create_tag_defs**](docs/TypesV1Api.md#create_tag_defs) | **POST** /catalog/v1/types/tagdefs | Bulk Create Tag Definitions
*TypesV1Api* | [**delete_business_metadata_def**](docs/TypesV1Api.md#delete_business_metadata_def) | **DELETE** /catalog/v1/types/businessmetadatadefs/{bmName} | Delete Business Metadata Definition
*TypesV1Api* | [**delete_tag_def**](docs/TypesV1Api.md#delete_tag_def) | **DELETE** /catalog/v1/types/tagdefs/{tagName} | Delete Tag Definition
*TypesV1Api* | [**get_all_business_metadata_defs**](docs/TypesV1Api.md#get_all_business_metadata_defs) | **GET** /catalog/v1/types/businessmetadatadefs | Bulk Read Business Metadata Definitions
*TypesV1Api* | [**get_all_tag_defs**](docs/TypesV1Api.md#get_all_tag_defs) | **GET** /catalog/v1/types/tagdefs | Bulk Read Tag Definitions
*TypesV1Api* | [**get_business_metadata_def_by_name**](docs/TypesV1Api.md#get_business_metadata_def_by_name) | **GET** /catalog/v1/types/businessmetadatadefs/{bmName} | Read Business Metadata Definition
*TypesV1Api* | [**get_tag_def_by_name**](docs/TypesV1Api.md#get_tag_def_by_name) | **GET** /catalog/v1/types/tagdefs/{tagName} | Read Tag Definition
*TypesV1Api* | [**update_business_metadata_defs**](docs/TypesV1Api.md#update_business_metadata_defs) | **PUT** /catalog/v1/types/businessmetadatadefs | Bulk Update Business Metadata Definitions
*TypesV1Api* | [**update_tag_defs**](docs/TypesV1Api.md#update_tag_defs) | **PUT** /catalog/v1/types/tagdefs | Bulk Update Tag Definitions
*UsersIamV2Api* | [**delete_iam_v2_user**](docs/UsersIamV2Api.md#delete_iam_v2_user) | **DELETE** /iam/v2/users/{id} | Delete a User
*UsersIamV2Api* | [**get_iam_v2_user**](docs/UsersIamV2Api.md#get_iam_v2_user) | **GET** /iam/v2/users/{id} | Read a User
*UsersIamV2Api* | [**list_iam_v2_users**](docs/UsersIamV2Api.md#list_iam_v2_users) | **GET** /iam/v2/users | List of Users
*UsersIamV2Api* | [**update_iam_v2_user**](docs/UsersIamV2Api.md#update_iam_v2_user) | **PATCH** /iam/v2/users/{id} | Update a User


## Documentation For Models

 - [AbstractConfigData](docs/AbstractConfigData.md)
 - [AbstractConfigDataAllOf](docs/AbstractConfigDataAllOf.md)
 - [AclData](docs/AclData.md)
 - [AclDataAllOf](docs/AclDataAllOf.md)
 - [AclDataList](docs/AclDataList.md)
 - [AclResourceType](docs/AclResourceType.md)
 - [ActivatePartnerSignupRequest](docs/ActivatePartnerSignupRequest.md)
 - [AlterBrokerReplicaExclusionData](docs/AlterBrokerReplicaExclusionData.md)
 - [AlterBrokerReplicaExclusionDataAllOf](docs/AlterBrokerReplicaExclusionDataAllOf.md)
 - [AlterBrokerReplicaExclusionDataList](docs/AlterBrokerReplicaExclusionDataList.md)
 - [AlterBrokerReplicaExclusionDataListAllOf](docs/AlterBrokerReplicaExclusionDataListAllOf.md)
 - [AlterConfigBatchRequestData](docs/AlterConfigBatchRequestData.md)
 - [AlterConfigBatchRequestDataData](docs/AlterConfigBatchRequestDataData.md)
 - [AlterMirrorStatusResponseData](docs/AlterMirrorStatusResponseData.md)
 - [AlterMirrorStatusResponseDataAllOf](docs/AlterMirrorStatusResponseDataAllOf.md)
 - [AlterMirrorStatusResponseDataList](docs/AlterMirrorStatusResponseDataList.md)
 - [AlterMirrorStatusResponseDataListAllOf](docs/AlterMirrorStatusResponseDataListAllOf.md)
 - [AlterMirrorsRequestData](docs/AlterMirrorsRequestData.md)
 - [AnyUnevenLoadData](docs/AnyUnevenLoadData.md)
 - [AnyUnevenLoadDataAllOf](docs/AnyUnevenLoadDataAllOf.md)
 - [AttributeDef](docs/AttributeDef.md)
 - [AuthorizedOperations](docs/AuthorizedOperations.md)
 - [AzureSSOConfig](docs/AzureSSOConfig.md)
 - [BalancerStatusData](docs/BalancerStatusData.md)
 - [BalancerStatusDataAllOf](docs/BalancerStatusDataAllOf.md)
 - [BillingV1Cost](docs/BillingV1Cost.md)
 - [BillingV1CostList](docs/BillingV1CostList.md)
 - [BillingV1Environment](docs/BillingV1Environment.md)
 - [BillingV1Resource](docs/BillingV1Resource.md)
 - [BrokerConfigData](docs/BrokerConfigData.md)
 - [BrokerConfigDataAllOf](docs/BrokerConfigDataAllOf.md)
 - [BrokerConfigDataList](docs/BrokerConfigDataList.md)
 - [BrokerConfigDataListAllOf](docs/BrokerConfigDataListAllOf.md)
 - [BrokerData](docs/BrokerData.md)
 - [BrokerDataAllOf](docs/BrokerDataAllOf.md)
 - [BrokerDataList](docs/BrokerDataList.md)
 - [BrokerDataListAllOf](docs/BrokerDataListAllOf.md)
 - [BrokerRemovalData](docs/BrokerRemovalData.md)
 - [BrokerRemovalDataAllOf](docs/BrokerRemovalDataAllOf.md)
 - [BrokerRemovalDataList](docs/BrokerRemovalDataList.md)
 - [BrokerRemovalDataListAllOf](docs/BrokerRemovalDataListAllOf.md)
 - [BrokerReplicaExclusionBatchRequestData](docs/BrokerReplicaExclusionBatchRequestData.md)
 - [BrokerReplicaExclusionData](docs/BrokerReplicaExclusionData.md)
 - [BrokerReplicaExclusionDataAllOf](docs/BrokerReplicaExclusionDataAllOf.md)
 - [BrokerReplicaExclusionDataList](docs/BrokerReplicaExclusionDataList.md)
 - [BrokerReplicaExclusionDataListAllOf](docs/BrokerReplicaExclusionDataListAllOf.md)
 - [BrokerReplicaExclusionRequestData](docs/BrokerReplicaExclusionRequestData.md)
 - [BrokerTaskData](docs/BrokerTaskData.md)
 - [BrokerTaskDataAllOf](docs/BrokerTaskDataAllOf.md)
 - [BrokerTaskDataList](docs/BrokerTaskDataList.md)
 - [BrokerTaskDataListAllOf](docs/BrokerTaskDataListAllOf.md)
 - [BrokerTaskType](docs/BrokerTaskType.md)
 - [BusinessMetadata](docs/BusinessMetadata.md)
 - [BusinessMetadataDef](docs/BusinessMetadataDef.md)
 - [BusinessMetadataDefResponse](docs/BusinessMetadataDefResponse.md)
 - [BusinessMetadataResponse](docs/BusinessMetadataResponse.md)
 - [ByokV1AwsKey](docs/ByokV1AwsKey.md)
 - [ByokV1AzureKey](docs/ByokV1AzureKey.md)
 - [ByokV1GcpKey](docs/ByokV1GcpKey.md)
 - [ByokV1Key](docs/ByokV1Key.md)
 - [ByokV1KeyList](docs/ByokV1KeyList.md)
 - [CdxV1AwsNetwork](docs/CdxV1AwsNetwork.md)
 - [CdxV1AzureNetwork](docs/CdxV1AzureNetwork.md)
 - [CdxV1ConnectionTypes](docs/CdxV1ConnectionTypes.md)
 - [CdxV1ConsumerShare](docs/CdxV1ConsumerShare.md)
 - [CdxV1ConsumerShareList](docs/CdxV1ConsumerShareList.md)
 - [CdxV1ConsumerShareStatus](docs/CdxV1ConsumerShareStatus.md)
 - [CdxV1ConsumerSharedResource](docs/CdxV1ConsumerSharedResource.md)
 - [CdxV1ConsumerSharedResourceList](docs/CdxV1ConsumerSharedResourceList.md)
 - [CdxV1CreateProviderShareRequest](docs/CdxV1CreateProviderShareRequest.md)
 - [CdxV1EmailConsumerRestriction](docs/CdxV1EmailConsumerRestriction.md)
 - [CdxV1GcpNetwork](docs/CdxV1GcpNetwork.md)
 - [CdxV1Network](docs/CdxV1Network.md)
 - [CdxV1OptIn](docs/CdxV1OptIn.md)
 - [CdxV1ProviderShare](docs/CdxV1ProviderShare.md)
 - [CdxV1ProviderShareList](docs/CdxV1ProviderShareList.md)
 - [CdxV1ProviderShareStatus](docs/CdxV1ProviderShareStatus.md)
 - [CdxV1ProviderSharedResource](docs/CdxV1ProviderSharedResource.md)
 - [CdxV1ProviderSharedResourceList](docs/CdxV1ProviderSharedResourceList.md)
 - [CdxV1ProviderSharedResourceUpdate](docs/CdxV1ProviderSharedResourceUpdate.md)
 - [CdxV1RedeemTokenRequest](docs/CdxV1RedeemTokenRequest.md)
 - [CdxV1RedeemTokenResponse](docs/CdxV1RedeemTokenResponse.md)
 - [CdxV1Schema](docs/CdxV1Schema.md)
 - [CdxV1SharedGroup](docs/CdxV1SharedGroup.md)
 - [CdxV1SharedSubject](docs/CdxV1SharedSubject.md)
 - [CdxV1SharedToken](docs/CdxV1SharedToken.md)
 - [CdxV1SharedTopic](docs/CdxV1SharedTopic.md)
 - [Classification](docs/Classification.md)
 - [ClassificationHeader](docs/ClassificationHeader.md)
 - [ClusterConfig](docs/ClusterConfig.md)
 - [ClusterConfigData](docs/ClusterConfigData.md)
 - [ClusterConfigDataAllOf](docs/ClusterConfigDataAllOf.md)
 - [ClusterConfigDataList](docs/ClusterConfigDataList.md)
 - [ClusterConfigDataListAllOf](docs/ClusterConfigDataListAllOf.md)
 - [ClusterData](docs/ClusterData.md)
 - [ClusterDataAllOf](docs/ClusterDataAllOf.md)
 - [ClusterDataList](docs/ClusterDataList.md)
 - [ClusterDataListAllOf](docs/ClusterDataListAllOf.md)
 - [CmkV2Basic](docs/CmkV2Basic.md)
 - [CmkV2Cku](docs/CmkV2Cku.md)
 - [CmkV2Cluster](docs/CmkV2Cluster.md)
 - [CmkV2ClusterList](docs/CmkV2ClusterList.md)
 - [CmkV2ClusterSpec](docs/CmkV2ClusterSpec.md)
 - [CmkV2ClusterSpecUpdate](docs/CmkV2ClusterSpecUpdate.md)
 - [CmkV2ClusterStatus](docs/CmkV2ClusterStatus.md)
 - [CmkV2ClusterUpdate](docs/CmkV2ClusterUpdate.md)
 - [CmkV2Dedicated](docs/CmkV2Dedicated.md)
 - [CmkV2Enterprise](docs/CmkV2Enterprise.md)
 - [CmkV2Standard](docs/CmkV2Standard.md)
 - [ColumnDetails](docs/ColumnDetails.md)
 - [CompatibilityCheckResponse](docs/CompatibilityCheckResponse.md)
 - [Config](docs/Config.md)
 - [ConfigData](docs/ConfigData.md)
 - [ConfigDefaultMetadata](docs/ConfigDefaultMetadata.md)
 - [ConfigDefaultRuleSet](docs/ConfigDefaultRuleSet.md)
 - [ConfigOverrideMetadata](docs/ConfigOverrideMetadata.md)
 - [ConfigOverrideRuleSet](docs/ConfigOverrideRuleSet.md)
 - [ConfigSynonymData](docs/ConfigSynonymData.md)
 - [ConfigUpdateRequest](docs/ConfigUpdateRequest.md)
 - [ConnectV1Connector](docs/ConnectV1Connector.md)
 - [ConnectV1ConnectorError](docs/ConnectV1ConnectorError.md)
 - [ConnectV1ConnectorErrorError](docs/ConnectV1ConnectorErrorError.md)
 - [ConnectV1ConnectorExpansion](docs/ConnectV1ConnectorExpansion.md)
 - [ConnectV1ConnectorExpansionId](docs/ConnectV1ConnectorExpansionId.md)
 - [ConnectV1ConnectorExpansionInfo](docs/ConnectV1ConnectorExpansionInfo.md)
 - [ConnectV1ConnectorExpansionMap](docs/ConnectV1ConnectorExpansionMap.md)
 - [ConnectV1ConnectorExpansionStatus](docs/ConnectV1ConnectorExpansionStatus.md)
 - [ConnectV1ConnectorExpansionStatusConnector](docs/ConnectV1ConnectorExpansionStatusConnector.md)
 - [ConnectV1ConnectorTasks](docs/ConnectV1ConnectorTasks.md)
 - [ConnectV1Connectors](docs/ConnectV1Connectors.md)
 - [ConnectV1CustomConnectorPlugin](docs/ConnectV1CustomConnectorPlugin.md)
 - [ConnectV1CustomConnectorPluginList](docs/ConnectV1CustomConnectorPluginList.md)
 - [ConnectV1CustomConnectorPluginUpdate](docs/ConnectV1CustomConnectorPluginUpdate.md)
 - [ConnectV1PresignedUrl](docs/ConnectV1PresignedUrl.md)
 - [ConnectV1PresignedUrlRequest](docs/ConnectV1PresignedUrlRequest.md)
 - [ConnectV1UploadSourcePresignedUrl](docs/ConnectV1UploadSourcePresignedUrl.md)
 - [ConstraintDef](docs/ConstraintDef.md)
 - [ConsumerAssignmentData](docs/ConsumerAssignmentData.md)
 - [ConsumerAssignmentDataAllOf](docs/ConsumerAssignmentDataAllOf.md)
 - [ConsumerAssignmentDataList](docs/ConsumerAssignmentDataList.md)
 - [ConsumerAssignmentDataListAllOf](docs/ConsumerAssignmentDataListAllOf.md)
 - [ConsumerData](docs/ConsumerData.md)
 - [ConsumerDataAllOf](docs/ConsumerDataAllOf.md)
 - [ConsumerDataList](docs/ConsumerDataList.md)
 - [ConsumerDataListAllOf](docs/ConsumerDataListAllOf.md)
 - [ConsumerGroupData](docs/ConsumerGroupData.md)
 - [ConsumerGroupDataAllOf](docs/ConsumerGroupDataAllOf.md)
 - [ConsumerGroupDataList](docs/ConsumerGroupDataList.md)
 - [ConsumerGroupDataListAllOf](docs/ConsumerGroupDataListAllOf.md)
 - [ConsumerGroupLagSummaryData](docs/ConsumerGroupLagSummaryData.md)
 - [ConsumerGroupLagSummaryDataAllOf](docs/ConsumerGroupLagSummaryDataAllOf.md)
 - [ConsumerLagData](docs/ConsumerLagData.md)
 - [ConsumerLagDataAllOf](docs/ConsumerLagDataAllOf.md)
 - [ConsumerLagDataList](docs/ConsumerLagDataList.md)
 - [ConsumerLagDataListAllOf](docs/ConsumerLagDataListAllOf.md)
 - [CreateAclRequestData](docs/CreateAclRequestData.md)
 - [CreateAclRequestDataList](docs/CreateAclRequestDataList.md)
 - [CreateAclRequestDataListAllOf](docs/CreateAclRequestDataListAllOf.md)
 - [CreateLinkRequestData](docs/CreateLinkRequestData.md)
 - [CreateMirrorTopicRequestData](docs/CreateMirrorTopicRequestData.md)
 - [CreateTopicRequestData](docs/CreateTopicRequestData.md)
 - [CreateTopicRequestDataConfigs](docs/CreateTopicRequestDataConfigs.md)
 - [DataType](docs/DataType.md)
 - [Entity](docs/Entity.md)
 - [EntityHeader](docs/EntityHeader.md)
 - [EntityPartialUpdate](docs/EntityPartialUpdate.md)
 - [EntityPartialUpdateResponse](docs/EntityPartialUpdateResponse.md)
 - [EntityWithExtInfo](docs/EntityWithExtInfo.md)
 - [EnvScopedObjectReference](docs/EnvScopedObjectReference.md)
 - [Error](docs/Error.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [ErrorSource](docs/ErrorSource.md)
 - [ExceptionListMeta](docs/ExceptionListMeta.md)
 - [ExporterConfigResponse](docs/ExporterConfigResponse.md)
 - [ExporterReference](docs/ExporterReference.md)
 - [ExporterResponse](docs/ExporterResponse.md)
 - [ExporterStatusResponse](docs/ExporterStatusResponse.md)
 - [ExporterUpdateRequest](docs/ExporterUpdateRequest.md)
 - [Failure](docs/Failure.md)
 - [FcpmV2ComputePool](docs/FcpmV2ComputePool.md)
 - [FcpmV2ComputePoolList](docs/FcpmV2ComputePoolList.md)
 - [FcpmV2ComputePoolSpec](docs/FcpmV2ComputePoolSpec.md)
 - [FcpmV2ComputePoolSpecUpdate](docs/FcpmV2ComputePoolSpecUpdate.md)
 - [FcpmV2ComputePoolStatus](docs/FcpmV2ComputePoolStatus.md)
 - [FcpmV2ComputePoolUpdate](docs/FcpmV2ComputePoolUpdate.md)
 - [FcpmV2Region](docs/FcpmV2Region.md)
 - [FcpmV2RegionList](docs/FcpmV2RegionList.md)
 - [GlobalObjectReference](docs/GlobalObjectReference.md)
 - [IamV2ApiKey](docs/IamV2ApiKey.md)
 - [IamV2ApiKeyList](docs/IamV2ApiKeyList.md)
 - [IamV2ApiKeySpec](docs/IamV2ApiKeySpec.md)
 - [IamV2ApiKeySpecUpdate](docs/IamV2ApiKeySpecUpdate.md)
 - [IamV2ApiKeyUpdate](docs/IamV2ApiKeyUpdate.md)
 - [IamV2IdentityPool](docs/IamV2IdentityPool.md)
 - [IamV2IdentityPoolList](docs/IamV2IdentityPoolList.md)
 - [IamV2IdentityProvider](docs/IamV2IdentityProvider.md)
 - [IamV2IdentityProviderList](docs/IamV2IdentityProviderList.md)
 - [IamV2IdentityProviderUpdate](docs/IamV2IdentityProviderUpdate.md)
 - [IamV2Invitation](docs/IamV2Invitation.md)
 - [IamV2InvitationList](docs/IamV2InvitationList.md)
 - [IamV2IpFilter](docs/IamV2IpFilter.md)
 - [IamV2IpFilterList](docs/IamV2IpFilterList.md)
 - [IamV2IpGroup](docs/IamV2IpGroup.md)
 - [IamV2IpGroupList](docs/IamV2IpGroupList.md)
 - [IamV2Jwks](docs/IamV2Jwks.md)
 - [IamV2JwksObject](docs/IamV2JwksObject.md)
 - [IamV2JwksSpec](docs/IamV2JwksSpec.md)
 - [IamV2JwksStatus](docs/IamV2JwksStatus.md)
 - [IamV2RoleBinding](docs/IamV2RoleBinding.md)
 - [IamV2RoleBindingList](docs/IamV2RoleBindingList.md)
 - [IamV2ServiceAccount](docs/IamV2ServiceAccount.md)
 - [IamV2ServiceAccountList](docs/IamV2ServiceAccountList.md)
 - [IamV2ServiceAccountUpdate](docs/IamV2ServiceAccountUpdate.md)
 - [IamV2SsoGroupMapping](docs/IamV2SsoGroupMapping.md)
 - [IamV2SsoGroupMappingList](docs/IamV2SsoGroupMappingList.md)
 - [IamV2User](docs/IamV2User.md)
 - [IamV2UserList](docs/IamV2UserList.md)
 - [IamV2UserUpdate](docs/IamV2UserUpdate.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Connector](docs/InlineResponse2001Connector.md)
 - [InlineResponse2001Tasks](docs/InlineResponse2001Tasks.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Configs](docs/InlineResponse2003Configs.md)
 - [InlineResponse2003Definition](docs/InlineResponse2003Definition.md)
 - [InlineResponse2003Value](docs/InlineResponse2003Value.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [KafkaQuotasV1ClientQuota](docs/KafkaQuotasV1ClientQuota.md)
 - [KafkaQuotasV1ClientQuotaList](docs/KafkaQuotasV1ClientQuotaList.md)
 - [KafkaQuotasV1ClientQuotaSpec](docs/KafkaQuotasV1ClientQuotaSpec.md)
 - [KafkaQuotasV1ClientQuotaSpecUpdate](docs/KafkaQuotasV1ClientQuotaSpecUpdate.md)
 - [KafkaQuotasV1ClientQuotaUpdate](docs/KafkaQuotasV1ClientQuotaUpdate.md)
 - [KafkaQuotasV1Throughput](docs/KafkaQuotasV1Throughput.md)
 - [KsqldbcmV2Cluster](docs/KsqldbcmV2Cluster.md)
 - [KsqldbcmV2ClusterList](docs/KsqldbcmV2ClusterList.md)
 - [KsqldbcmV2ClusterSpec](docs/KsqldbcmV2ClusterSpec.md)
 - [KsqldbcmV2ClusterStatus](docs/KsqldbcmV2ClusterStatus.md)
 - [ListLinkConfigsResponseData](docs/ListLinkConfigsResponseData.md)
 - [ListLinkConfigsResponseDataAllOf](docs/ListLinkConfigsResponseDataAllOf.md)
 - [ListLinkConfigsResponseDataList](docs/ListLinkConfigsResponseDataList.md)
 - [ListLinkConfigsResponseDataListAllOf](docs/ListLinkConfigsResponseDataListAllOf.md)
 - [ListLinksResponseData](docs/ListLinksResponseData.md)
 - [ListLinksResponseDataAllOf](docs/ListLinksResponseDataAllOf.md)
 - [ListLinksResponseDataList](docs/ListLinksResponseDataList.md)
 - [ListLinksResponseDataListAllOf](docs/ListLinksResponseDataListAllOf.md)
 - [ListMeta](docs/ListMeta.md)
 - [ListMirrorTopicsResponseData](docs/ListMirrorTopicsResponseData.md)
 - [ListMirrorTopicsResponseDataAllOf](docs/ListMirrorTopicsResponseDataAllOf.md)
 - [ListMirrorTopicsResponseDataList](docs/ListMirrorTopicsResponseDataList.md)
 - [ListMirrorTopicsResponseDataListAllOf](docs/ListMirrorTopicsResponseDataListAllOf.md)
 - [MirrorLag](docs/MirrorLag.md)
 - [MirrorLags](docs/MirrorLags.md)
 - [MirrorTopicStatus](docs/MirrorTopicStatus.md)
 - [Mode](docs/Mode.md)
 - [ModeUpdateRequest](docs/ModeUpdateRequest.md)
 - [MultipleSearchFilter](docs/MultipleSearchFilter.md)
 - [NetworkingV1AwsAccount](docs/NetworkingV1AwsAccount.md)
 - [NetworkingV1AwsNetwork](docs/NetworkingV1AwsNetwork.md)
 - [NetworkingV1AwsPeering](docs/NetworkingV1AwsPeering.md)
 - [NetworkingV1AwsPrivateLinkAccess](docs/NetworkingV1AwsPrivateLinkAccess.md)
 - [NetworkingV1AwsPrivateLinkAttachmentConnection](docs/NetworkingV1AwsPrivateLinkAttachmentConnection.md)
 - [NetworkingV1AwsPrivateLinkAttachmentConnectionStatus](docs/NetworkingV1AwsPrivateLinkAttachmentConnectionStatus.md)
 - [NetworkingV1AwsPrivateLinkAttachmentStatus](docs/NetworkingV1AwsPrivateLinkAttachmentStatus.md)
 - [NetworkingV1AwsTransitGatewayAttachment](docs/NetworkingV1AwsTransitGatewayAttachment.md)
 - [NetworkingV1AwsTransitGatewayAttachmentStatus](docs/NetworkingV1AwsTransitGatewayAttachmentStatus.md)
 - [NetworkingV1AwsVpcEndpointService](docs/NetworkingV1AwsVpcEndpointService.md)
 - [NetworkingV1AzureNetwork](docs/NetworkingV1AzureNetwork.md)
 - [NetworkingV1AzurePeering](docs/NetworkingV1AzurePeering.md)
 - [NetworkingV1AzurePrivateLinkAccess](docs/NetworkingV1AzurePrivateLinkAccess.md)
 - [NetworkingV1AzurePrivateLinkAttachmentConnection](docs/NetworkingV1AzurePrivateLinkAttachmentConnection.md)
 - [NetworkingV1AzurePrivateLinkAttachmentConnectionStatus](docs/NetworkingV1AzurePrivateLinkAttachmentConnectionStatus.md)
 - [NetworkingV1AzurePrivateLinkAttachmentStatus](docs/NetworkingV1AzurePrivateLinkAttachmentStatus.md)
 - [NetworkingV1AzurePrivateLinkService](docs/NetworkingV1AzurePrivateLinkService.md)
 - [NetworkingV1Cidr](docs/NetworkingV1Cidr.md)
 - [NetworkingV1ConnectionTypes](docs/NetworkingV1ConnectionTypes.md)
 - [NetworkingV1DnsConfig](docs/NetworkingV1DnsConfig.md)
 - [NetworkingV1GcpNetwork](docs/NetworkingV1GcpNetwork.md)
 - [NetworkingV1GcpPeering](docs/NetworkingV1GcpPeering.md)
 - [NetworkingV1GcpPrivateLinkAttachmentConnection](docs/NetworkingV1GcpPrivateLinkAttachmentConnection.md)
 - [NetworkingV1GcpPrivateLinkAttachmentConnectionStatus](docs/NetworkingV1GcpPrivateLinkAttachmentConnectionStatus.md)
 - [NetworkingV1GcpPrivateLinkAttachmentStatus](docs/NetworkingV1GcpPrivateLinkAttachmentStatus.md)
 - [NetworkingV1GcpPrivateServiceConnectAccess](docs/NetworkingV1GcpPrivateServiceConnectAccess.md)
 - [NetworkingV1GcpPscServiceAttachment](docs/NetworkingV1GcpPscServiceAttachment.md)
 - [NetworkingV1IpAddress](docs/NetworkingV1IpAddress.md)
 - [NetworkingV1IpAddressList](docs/NetworkingV1IpAddressList.md)
 - [NetworkingV1Network](docs/NetworkingV1Network.md)
 - [NetworkingV1NetworkLinkEndpoint](docs/NetworkingV1NetworkLinkEndpoint.md)
 - [NetworkingV1NetworkLinkEndpointList](docs/NetworkingV1NetworkLinkEndpointList.md)
 - [NetworkingV1NetworkLinkEndpointSpec](docs/NetworkingV1NetworkLinkEndpointSpec.md)
 - [NetworkingV1NetworkLinkEndpointSpecUpdate](docs/NetworkingV1NetworkLinkEndpointSpecUpdate.md)
 - [NetworkingV1NetworkLinkEndpointStatus](docs/NetworkingV1NetworkLinkEndpointStatus.md)
 - [NetworkingV1NetworkLinkEndpointUpdate](docs/NetworkingV1NetworkLinkEndpointUpdate.md)
 - [NetworkingV1NetworkLinkService](docs/NetworkingV1NetworkLinkService.md)
 - [NetworkingV1NetworkLinkServiceAcceptPolicy](docs/NetworkingV1NetworkLinkServiceAcceptPolicy.md)
 - [NetworkingV1NetworkLinkServiceAssociation](docs/NetworkingV1NetworkLinkServiceAssociation.md)
 - [NetworkingV1NetworkLinkServiceAssociationList](docs/NetworkingV1NetworkLinkServiceAssociationList.md)
 - [NetworkingV1NetworkLinkServiceAssociationSpec](docs/NetworkingV1NetworkLinkServiceAssociationSpec.md)
 - [NetworkingV1NetworkLinkServiceAssociationStatus](docs/NetworkingV1NetworkLinkServiceAssociationStatus.md)
 - [NetworkingV1NetworkLinkServiceList](docs/NetworkingV1NetworkLinkServiceList.md)
 - [NetworkingV1NetworkLinkServiceSpec](docs/NetworkingV1NetworkLinkServiceSpec.md)
 - [NetworkingV1NetworkLinkServiceSpecUpdate](docs/NetworkingV1NetworkLinkServiceSpecUpdate.md)
 - [NetworkingV1NetworkLinkServiceStatus](docs/NetworkingV1NetworkLinkServiceStatus.md)
 - [NetworkingV1NetworkLinkServiceUpdate](docs/NetworkingV1NetworkLinkServiceUpdate.md)
 - [NetworkingV1NetworkList](docs/NetworkingV1NetworkList.md)
 - [NetworkingV1NetworkSpec](docs/NetworkingV1NetworkSpec.md)
 - [NetworkingV1NetworkSpecUpdate](docs/NetworkingV1NetworkSpecUpdate.md)
 - [NetworkingV1NetworkStatus](docs/NetworkingV1NetworkStatus.md)
 - [NetworkingV1NetworkUpdate](docs/NetworkingV1NetworkUpdate.md)
 - [NetworkingV1Peering](docs/NetworkingV1Peering.md)
 - [NetworkingV1PeeringList](docs/NetworkingV1PeeringList.md)
 - [NetworkingV1PeeringSpec](docs/NetworkingV1PeeringSpec.md)
 - [NetworkingV1PeeringSpecUpdate](docs/NetworkingV1PeeringSpecUpdate.md)
 - [NetworkingV1PeeringStatus](docs/NetworkingV1PeeringStatus.md)
 - [NetworkingV1PeeringUpdate](docs/NetworkingV1PeeringUpdate.md)
 - [NetworkingV1PrivateLinkAccess](docs/NetworkingV1PrivateLinkAccess.md)
 - [NetworkingV1PrivateLinkAccessList](docs/NetworkingV1PrivateLinkAccessList.md)
 - [NetworkingV1PrivateLinkAccessSpec](docs/NetworkingV1PrivateLinkAccessSpec.md)
 - [NetworkingV1PrivateLinkAccessSpecUpdate](docs/NetworkingV1PrivateLinkAccessSpecUpdate.md)
 - [NetworkingV1PrivateLinkAccessStatus](docs/NetworkingV1PrivateLinkAccessStatus.md)
 - [NetworkingV1PrivateLinkAccessUpdate](docs/NetworkingV1PrivateLinkAccessUpdate.md)
 - [NetworkingV1PrivateLinkAttachment](docs/NetworkingV1PrivateLinkAttachment.md)
 - [NetworkingV1PrivateLinkAttachmentConnection](docs/NetworkingV1PrivateLinkAttachmentConnection.md)
 - [NetworkingV1PrivateLinkAttachmentConnectionList](docs/NetworkingV1PrivateLinkAttachmentConnectionList.md)
 - [NetworkingV1PrivateLinkAttachmentConnectionSpec](docs/NetworkingV1PrivateLinkAttachmentConnectionSpec.md)
 - [NetworkingV1PrivateLinkAttachmentConnectionSpecUpdate](docs/NetworkingV1PrivateLinkAttachmentConnectionSpecUpdate.md)
 - [NetworkingV1PrivateLinkAttachmentConnectionStatus](docs/NetworkingV1PrivateLinkAttachmentConnectionStatus.md)
 - [NetworkingV1PrivateLinkAttachmentConnectionUpdate](docs/NetworkingV1PrivateLinkAttachmentConnectionUpdate.md)
 - [NetworkingV1PrivateLinkAttachmentList](docs/NetworkingV1PrivateLinkAttachmentList.md)
 - [NetworkingV1PrivateLinkAttachmentSpec](docs/NetworkingV1PrivateLinkAttachmentSpec.md)
 - [NetworkingV1PrivateLinkAttachmentSpecUpdate](docs/NetworkingV1PrivateLinkAttachmentSpecUpdate.md)
 - [NetworkingV1PrivateLinkAttachmentStatus](docs/NetworkingV1PrivateLinkAttachmentStatus.md)
 - [NetworkingV1PrivateLinkAttachmentUpdate](docs/NetworkingV1PrivateLinkAttachmentUpdate.md)
 - [NetworkingV1Services](docs/NetworkingV1Services.md)
 - [NetworkingV1SupportedConnectionTypes](docs/NetworkingV1SupportedConnectionTypes.md)
 - [NetworkingV1TransitGatewayAttachment](docs/NetworkingV1TransitGatewayAttachment.md)
 - [NetworkingV1TransitGatewayAttachmentList](docs/NetworkingV1TransitGatewayAttachmentList.md)
 - [NetworkingV1TransitGatewayAttachmentSpec](docs/NetworkingV1TransitGatewayAttachmentSpec.md)
 - [NetworkingV1TransitGatewayAttachmentSpecUpdate](docs/NetworkingV1TransitGatewayAttachmentSpecUpdate.md)
 - [NetworkingV1TransitGatewayAttachmentStatus](docs/NetworkingV1TransitGatewayAttachmentStatus.md)
 - [NetworkingV1TransitGatewayAttachmentUpdate](docs/NetworkingV1TransitGatewayAttachmentUpdate.md)
 - [NetworkingV1ZoneInfo](docs/NetworkingV1ZoneInfo.md)
 - [NetworkingV1ZonesInfo](docs/NetworkingV1ZonesInfo.md)
 - [NotificationsV1Integration](docs/NotificationsV1Integration.md)
 - [NotificationsV1IntegrationList](docs/NotificationsV1IntegrationList.md)
 - [NotificationsV1MsTeamsTarget](docs/NotificationsV1MsTeamsTarget.md)
 - [NotificationsV1NotificationType](docs/NotificationsV1NotificationType.md)
 - [NotificationsV1NotificationTypeList](docs/NotificationsV1NotificationTypeList.md)
 - [NotificationsV1RoleEmailTarget](docs/NotificationsV1RoleEmailTarget.md)
 - [NotificationsV1SlackTarget](docs/NotificationsV1SlackTarget.md)
 - [NotificationsV1Subscription](docs/NotificationsV1Subscription.md)
 - [NotificationsV1SubscriptionList](docs/NotificationsV1SubscriptionList.md)
 - [NotificationsV1SubscriptionUpdate](docs/NotificationsV1SubscriptionUpdate.md)
 - [NotificationsV1Target](docs/NotificationsV1Target.md)
 - [NotificationsV1UserEmailTarget](docs/NotificationsV1UserEmailTarget.md)
 - [NotificationsV1WebhookTarget](docs/NotificationsV1WebhookTarget.md)
 - [ObjectMeta](docs/ObjectMeta.md)
 - [ObjectReference](docs/ObjectReference.md)
 - [OrgV2Environment](docs/OrgV2Environment.md)
 - [OrgV2EnvironmentList](docs/OrgV2EnvironmentList.md)
 - [OrgV2Organization](docs/OrgV2Organization.md)
 - [OrgV2OrganizationList](docs/OrgV2OrganizationList.md)
 - [PartialUpdateParams](docs/PartialUpdateParams.md)
 - [PartitionData](docs/PartitionData.md)
 - [PartitionDataAllOf](docs/PartitionDataAllOf.md)
 - [PartitionDataList](docs/PartitionDataList.md)
 - [PartitionDataListAllOf](docs/PartitionDataListAllOf.md)
 - [PartnerLinkRequest](docs/PartnerLinkRequest.md)
 - [PartnerSignupRequest](docs/PartnerSignupRequest.md)
 - [PartnerSignupResponse](docs/PartnerSignupResponse.md)
 - [PartnerV2Entitlement](docs/PartnerV2Entitlement.md)
 - [PartnerV2EntitlementList](docs/PartnerV2EntitlementList.md)
 - [PartnerV2Organization](docs/PartnerV2Organization.md)
 - [PartnerV2OrganizationList](docs/PartnerV2OrganizationList.md)
 - [ProduceRequest](docs/ProduceRequest.md)
 - [ProduceRequestData](docs/ProduceRequestData.md)
 - [ProduceRequestHeader](docs/ProduceRequestHeader.md)
 - [ProduceResponse](docs/ProduceResponse.md)
 - [ProduceResponseData](docs/ProduceResponseData.md)
 - [ReassignmentData](docs/ReassignmentData.md)
 - [ReassignmentDataAllOf](docs/ReassignmentDataAllOf.md)
 - [ReassignmentDataList](docs/ReassignmentDataList.md)
 - [ReassignmentDataListAllOf](docs/ReassignmentDataListAllOf.md)
 - [RegisterExporterRequest](docs/RegisterExporterRequest.md)
 - [RegisterSchemaRequest](docs/RegisterSchemaRequest.md)
 - [RegisterSchemaResponse](docs/RegisterSchemaResponse.md)
 - [Relationship](docs/Relationship.md)
 - [RemoveBrokerTaskData](docs/RemoveBrokerTaskData.md)
 - [RemoveBrokerTaskDataAllOf](docs/RemoveBrokerTaskDataAllOf.md)
 - [RemoveBrokerTaskDataList](docs/RemoveBrokerTaskDataList.md)
 - [RemoveBrokerTaskDataListAllOf](docs/RemoveBrokerTaskDataListAllOf.md)
 - [RemoveBrokersRequestData](docs/RemoveBrokersRequestData.md)
 - [ReplicaData](docs/ReplicaData.md)
 - [ReplicaDataAllOf](docs/ReplicaDataAllOf.md)
 - [ReplicaDataList](docs/ReplicaDataList.md)
 - [ReplicaDataListAllOf](docs/ReplicaDataListAllOf.md)
 - [ReplicaStatusData](docs/ReplicaStatusData.md)
 - [ReplicaStatusDataAllOf](docs/ReplicaStatusDataAllOf.md)
 - [ReplicaStatusDataList](docs/ReplicaStatusDataList.md)
 - [ReplicaStatusDataListAllOf](docs/ReplicaStatusDataListAllOf.md)
 - [Resource](docs/Resource.md)
 - [ResourceCollection](docs/ResourceCollection.md)
 - [ResourceCollectionMetadata](docs/ResourceCollectionMetadata.md)
 - [ResourceMetadata](docs/ResourceMetadata.md)
 - [ResultListMeta](docs/ResultListMeta.md)
 - [RowFieldType](docs/RowFieldType.md)
 - [Schema](docs/Schema.md)
 - [SchemaReference](docs/SchemaReference.md)
 - [SchemaString](docs/SchemaString.md)
 - [SdV1Pipeline](docs/SdV1Pipeline.md)
 - [SdV1PipelineList](docs/SdV1PipelineList.md)
 - [SdV1PipelineSpec](docs/SdV1PipelineSpec.md)
 - [SdV1PipelineStatus](docs/SdV1PipelineStatus.md)
 - [SdV1SourceCodeObject](docs/SdV1SourceCodeObject.md)
 - [SearchParams](docs/SearchParams.md)
 - [SearchResult](docs/SearchResult.md)
 - [ServiceQuotaV1AppliedQuota](docs/ServiceQuotaV1AppliedQuota.md)
 - [ServiceQuotaV1AppliedQuotaList](docs/ServiceQuotaV1AppliedQuotaList.md)
 - [ServiceQuotaV1Scope](docs/ServiceQuotaV1Scope.md)
 - [ServiceQuotaV1ScopeList](docs/ServiceQuotaV1ScopeList.md)
 - [SqlV1beta1ResultSchema](docs/SqlV1beta1ResultSchema.md)
 - [SqlV1beta1ScalingStatus](docs/SqlV1beta1ScalingStatus.md)
 - [SqlV1beta1Statement](docs/SqlV1beta1Statement.md)
 - [SqlV1beta1StatementException](docs/SqlV1beta1StatementException.md)
 - [SqlV1beta1StatementExceptionList](docs/SqlV1beta1StatementExceptionList.md)
 - [SqlV1beta1StatementList](docs/SqlV1beta1StatementList.md)
 - [SqlV1beta1StatementResult](docs/SqlV1beta1StatementResult.md)
 - [SqlV1beta1StatementResultResults](docs/SqlV1beta1StatementResultResults.md)
 - [SqlV1beta1StatementSpec](docs/SqlV1beta1StatementSpec.md)
 - [SqlV1beta1StatementStatus](docs/SqlV1beta1StatementStatus.md)
 - [SrcmV2Cluster](docs/SrcmV2Cluster.md)
 - [SrcmV2ClusterList](docs/SrcmV2ClusterList.md)
 - [SrcmV2ClusterSpec](docs/SrcmV2ClusterSpec.md)
 - [SrcmV2ClusterSpecUpdate](docs/SrcmV2ClusterSpecUpdate.md)
 - [SrcmV2ClusterStatus](docs/SrcmV2ClusterStatus.md)
 - [SrcmV2ClusterUpdate](docs/SrcmV2ClusterUpdate.md)
 - [SrcmV2Region](docs/SrcmV2Region.md)
 - [SrcmV2RegionList](docs/SrcmV2RegionList.md)
 - [SrcmV2RegionSpec](docs/SrcmV2RegionSpec.md)
 - [SrcmV3Cluster](docs/SrcmV3Cluster.md)
 - [SrcmV3ClusterList](docs/SrcmV3ClusterList.md)
 - [SrcmV3ClusterSpec](docs/SrcmV3ClusterSpec.md)
 - [SrcmV3ClusterStatus](docs/SrcmV3ClusterStatus.md)
 - [StsV1TokenExchangeReply](docs/StsV1TokenExchangeReply.md)
 - [SubjectVersion](docs/SubjectVersion.md)
 - [Tag](docs/Tag.md)
 - [TagDef](docs/TagDef.md)
 - [TagDefResponse](docs/TagDefResponse.md)
 - [TagResponse](docs/TagResponse.md)
 - [TermAssignmentHeader](docs/TermAssignmentHeader.md)
 - [TimeBoundary](docs/TimeBoundary.md)
 - [TopicConfigData](docs/TopicConfigData.md)
 - [TopicConfigDataAllOf](docs/TopicConfigDataAllOf.md)
 - [TopicConfigDataList](docs/TopicConfigDataList.md)
 - [TopicConfigDataListAllOf](docs/TopicConfigDataListAllOf.md)
 - [TopicData](docs/TopicData.md)
 - [TopicDataAllOf](docs/TopicDataAllOf.md)
 - [TopicDataList](docs/TopicDataList.md)
 - [TopicDataListAllOf](docs/TopicDataListAllOf.md)
 - [TypedEnvScopedObjectReference](docs/TypedEnvScopedObjectReference.md)
 - [TypedGlobalObjectReference](docs/TypedGlobalObjectReference.md)
 - [UpdateConfigRequestData](docs/UpdateConfigRequestData.md)
 - [UpdateLinkConfigRequestData](docs/UpdateLinkConfigRequestData.md)
 - [UpdatePartitionCountRequestData](docs/UpdatePartitionCountRequestData.md)


## Documentation For Authorization


## api-key

- **Type**: HTTP basic authentication


## cloud-api-key

- **Type**: HTTP basic authentication


## confluent-sts-access-token

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## external-access-token

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## oauth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **partner:alter**: enables partners to alter entitlements
 - **partner:create**: enables partners to create entitlements and signup on behalf of customers
 - **partner:delete**: enables partners to delete entitlements and organizations
 - **partner:describe**: enables partners to read and list entitlements and organizations


## resource-api-key

- **Type**: HTTP basic authentication


## Author

support@confluent.io


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

