"""
    Confluent Cloud APIs

    # Introduction  <div class=\"status-info\"> <p class=\"status-info-title\">Note</p> This documents the collection of Confluent Cloud APIs. Each API documents its <a href=\"#section/Versioning/API-Lifecycle-Policy\">lifecycle phase</a>. APIs marked as Early Access or Preview are not ready for production usage. We're currently working with a select group of customers to get feedback and iterate on these APIs. </div>  Confluent Cloud APIs are a core building block of Confluent Cloud. You can use the APIs to manage your own account or to integrate Confluent into your product.  Most of the APIs are organized around <a href=\"http://en.wikipedia.org/wiki/Representational_State_Transfer\" target=\"_blank\">REST</a> and the resources which make up Confluent Cloud. The APIs have predictable resource-oriented URLs, transport data using JSON, and use standard HTTP verbs, response codes, authentication, and design principles.  # Object Model  <div class=\"status-info\"> <p class=\"status-info-title\">Note</p> This section describes the object model for many Confluent Cloud APIs, but not all. The Connect v1 API group has a different object model. You can review the example request and response bodies in <a href=\"#tag/Connectors-(v1)\">Connect v1 API</a> to see its object model. </div>  Confluent Cloud APIs are primarily designed to be declarative and intent-oriented. In other words,  tell the API what you want (for example, throughput or SLOs) and it will figure out how to make it happen  (for example, cluster sizing). A Confluent object acts as a \"record of intent\" — after you create the object, Confluent Cloud will work tirelessly in the background to ensure that the object exists as specified.  Confluent APIs represent objects in JSON with media-type `application/json`.  Many objects follow a model consisting of `spec` and `status`. An object's `spec` tells Confluent the _desired state_ (specification) of the resource. The object may not be immediately available or changes may not be immediately applied. For this reason, many objects also have a `status` property that provides info about the _current state_ of the resource. Confluent Cloud is continuously and actively managing each resource's current state to match it's desired state.  All Confluent objects share a set of common properties:  * **api_version** – API objects have an `api_version` field indicating their API version. * **kind** – API objects have a `kind` field indicating the kind of object it is. * **id** – Each object in the API will have an identifier, indicated via its `id` field,   and should be treated as an opaque string unless otherwise specified.  There are a number of other [standard properties](#standard-properties) and that you'll encounter used by many API objects. And of course, objects have plenty of non-standard fields that are specific to each object _kind_... this is what makes them interesting!  # Authentication  Confluent uses API keys and Java Web Tokens (JWTs) to integrate your applications and workflows to your Confluent Cloud resources using the Confluent Cloud REST APIs. Your applications and workflows must be authenticated and authorized in order to access and manage Confluent Cloud resources.  ## API keys  You can create and manage your API keys using the Confluent Cloud Console or Confluent CLI. For more information, see [Use API Keys to Control Access in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html).  Confluent Cloud uses the following two categories of API keys:  * A **Cloud API key** grants access to the Confluent Cloud Management APIs,   such as for Provisioning and Metrics integrations. * A **resource-specific API key** grants access to a Confluent Kafka cluster   (Kafka API key), a Confluent Cloud Schema Registry (Schema Registry API key),   Flink (Flink API key scoped to an Environment + Region pair), or a ksqlDB application.  Each Confluent Cloud API key is associated with a principal (specific user or service account) and inherits the permissions granted to the owner.  * For example, if service account `Armageddon` is granted ACLs on Kafka cluster   `neptune`, then a Kafka API Key for `neptune` owned by `Armageddon` will have   these ACLs enforced. * **Note:** API keys are automatically deleted when the associated user or service   account is deleted (for example, when an employee leaves the company or moves to   a new department and an SSO integration removes the Confluent Cloud user as they   no longer require access). * Confluent **strongly recommends** that you use service accounts for all   production-critical access.  Confluent Cloud API keys grant access to Confluent Cloud resources, so **keep them secure**! Do not share your API keys and secrets in publicly-accessible locations, such as  GitHub or client-side code.  All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.  To use an API key, you must send it in an `Authorization: Basic {credentials}` header. Remember that HTTP Basic authentication requires you to provide your credentials as the API key ID and associated API secret separated by a colon and encoded using Base64 format. For example, if your API key ID is `ABCDEFGH123456789` and the API key Secret  is `XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO`, then the authorization header is:  ```text​ Authorization: Basic QUJDREVGR0gxMjM0NTY3ODk6WE5DSVc5M0kyTDFTUVBKU0o4MjNLMUxTOTAyS0xERk1DWlBXRU8= ```  You can generate this header example from the API key:  macOS:  ```shell $ echo -n \"ABCDEFGH123456789:XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO\" | base64  ```  Linux:  ```shell $ echo -n \"ABCDEFGH123456789:XNCIW93I2L1SQPJSJ823K1LS902KLDFMCZPWEO\" | base64 -w 0 ```  To find out if an API operation supports Cloud API Keys, look in the **AUTHORIZATIONS** listing for `cloud-api-key`.  To find out if an API operation supports resource-specific API Keys, look in the **AUTHORIZATIONS** listing for `resource-api-key`.  ## External OAuth  You can use [OAuth/OIDC support for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html) to authenticate and authorize access to applications and workloads for the following Confluent Cloud REST APIs:  * **Kafka REST API**: [Kafka REST API for Clusters(V3)](https://docs.confluent.io/cloud/current/api.html#tag/Cluster-(v3)).   For an API overview and examples, see [Cluster Management with Kafka REST API](https://docs.confluent.io/cloud/current/kafka-rest/kafka-rest-cc.html). * **Schema Registry REST API**: [Schema Registry REST API for Schemas(V1)](https://docs.confluent.io/cloud/current/api.html#tag/Schemas-(v1))   and [Subjects](https://docs.confluent.io/cloud/current/api.html#tag/Subjects-(v1)).   For an API overview and examples, see [Schema Registry REST API for Confluent Cloud](https://docs.confluent.io/cloud/current/sr/sr-rest-apis.html).  Alternatively, to find out if an API operation supports external tokens, look in the **AUTHORIZATIONS** listing for `external-access-token`.  ## Confluent STS tokens  Confluent Security Token Service (STS) issues access tokens (`confluent-sts-access-token`) by exchanging an external token (`external-access-token`) for a `confluent-sts-access-token`. You can use Confluent STS tokens to authenticate to Confluent Cloud APIs that support the `confluent-sts-access-token` notation.  To find out if an API operation supports Confluent STS tokens, look in the **AUTHORIZATIONS** listing for `confluent-sts-access-token`.  ## Partner OAuth  Approved partners can fetch Partner tokens (`confluent-partner-access-token`) that validate their identity and grant access to the Partner API (`partner/v2`), which lets them sign up an organization on behalf of a customer, manage entitlements (create, read, and list), and read or list organizations they have signed up.  To find out an API operation supports Partner tokens, look in the **AUTHORIZATIONS** listing for `confluent-partner-access-token`.  <!-- TODO: port this back to the Confluent API Design Guide -->  <SecurityDefinitions />  # Errors  <div class=\"status-info\"> <p class=\"status-info-title\">Note</p> This section describes the structure of error responses for many Confluent Cloud APIs, but not all. The Connect v1 API group has a different set of structures for error responses. Please review the example request and response bodies in the Connect v1 API documentation <a href=\"#tag/Connectors-(v1)\">below</a> to see its error behaviour. </div>  Confluent uses conventional [HTTP status codes](#section/HTTP-Guidelines/Status-Codes) to indicate the success or failure of an API request.  Failures follow a standard model to tell you about what went wrong. They may include one or more error objects with the following fields:  | Field      | Type    | Description |------------|---------|-------------------------------------- | id*        | UUID    | A unique identifier for this particular occurrence of the problem. | status     | String  | The HTTP status code applicable to this problem. | code       | String  | An application-specific error code. | title      | String  | A short, human-readable summary of the problem that **should not** change from occurrence to occurrence of the problem, except for purposes of localization. | detail*    | String  | A human-readable explanation specific to this occurrence of the problem. Like title, this field’s value can be localized. | source     | Object  | An object that references the source of the error, and optionally includes any of the following members: | &nbsp;&nbsp;pointer   | String  | A <a href=\"https://tools.ietf.org/html/rfc6901\" target=\"_blank\">JSON Pointer</a> to the associated entity in the request document (e.g. `\"/spec/title\"` for a specific attribute). | &nbsp;&nbsp;parameter | String  | A string indicating which URI query parameter caused the error. | meta       | Object  | A meta object that contains non-standard meta-information about the error. | resolution | String  | Instructions for the end-user for correcting the error.  \\* indicates a required field  All errors include an `id` and some `detail` message. The `id` is a unique identifier — use it when you're working with Confluent support to debug a problem with a specific API call. The `detail` describes what went wrong.  Some errors that could be handled programmatically (e.g., a Kafka cluster config is invalid) may include an error `code` that briefly explains the error reported.  Validation issues and similar errors include a `source` which tells you exactly what in the request was responsible for the error.  For example, a failure may look like      {       \"errors\": [{         \"status\": \"422\",         \"code\": \"invalid_configuration\",         \"id\": \"30ce6058-87da-11e4-b116-123b93f75cba\",         \"title\": \"The Kafka cluster configuration is invalid\",         \"detail\": \"The property '/cluster/storage_size' of type string did not match the following type: integer\",         \"source\": {           \"pointer\": \"/cluster/storage_size\"         }       }]     }  If a request fails validation, it will return an HTTP `422 Unprocessable Entity` with a list of fields that failed validation.  # Pagination  <div class=\"status-info\"> <p class=\"status-info-title\">Note</p> This section describes the pagination behavior of “list” operations for many Confluent Cloud APIs, but not all. The Connect v1 API list operations do not support pagination. </div>  All API resources have support for bulk reads via \"list\" API operations. For example, you can \"list Kafka clusters\", \"list api keys\", and \"list environments\". These \"list\" operations require pagination; by requesting smaller subsets of data, API clients receive a response much faster than requesting the entire, potentially large, data set.  All \"list\" operations follow the same pattern with the following parameters:  * `page_size` –  client-provided max number of items per page, only valid on the first request. * `page_token` –  server-generated token used for traversing through the result set.  A paginated response may include any of the following pagination links. API clients may follow the respective link to page forward or backward through the result set as desired.  | [Link Relation](https://www.iana.org/assignments/link-relations/link-relations.xml) | Description |---------|--------------------------------------- | `next`  | A link to the next page of results. A response that does not contain a next link does not have further data to fetch. | `prev`  | A link to the previous page of results. A response that does not contain a prev link has no previous data. This link is **optional** for collections that cannot be traversed backward. | `first` | A link to the first page of results. This link is **optional** for collections that cannot be indexed directly to a given page. | `last`  | A link to the last page of results. This link is **optional** for collections that cannot be indexed directly to a given page.  API clients must treat pagination links and the `page_token` parameter in particular as an opaque string.   An example paginated list response may look like ``` {     \"api_version\": \"v2\",     \"kind\": \"KafkaClusterList\",     \"metadata\": {         \"next\": \"https://api.confluent.cloud/kafka-clusters?page_token=ABCDEFGHIJKLMNOP1234567890\"     }     \"data\": [         {             \"metadata\": {                 \"id\": \"lkc-abc123\",                 \"self\": \"https://api.confluent.cloud/kafka-clusters/lkc-abc123\",                 \"resource_name\": \"crn://confluent.cloud/kafka=lkc-abc123\",             }             \"spec\": {                 \"display_name\": \"My Kafka Cluster\",                 <snip>             },             \"status\": {                 \"phase\": \"RUNNING\",                 <snip>             }         },         <snip>     ] } ```  # Rate Limiting  To protect the stability of the API and keep it available to all users, Confluent employs multiple safeguards. If you send too many requests in quick succession or perform too many concurrent operations, you may be throttled or have your request rejected with an error.  When a rate limit is breached, an HTTP `429 Too Many Requests` error is returned. The following headers are sent back to provide assistance in dealing with rate limits. Note that headers are not returned for a `429` error response with  [Kafka REST API (v3)](https://docs.confluent.io/cloud/current/api.html#tag/Cluster-(v3)).  | Header                  | Description |-------------------------|---------------------------------------- | `X-RateLimit-Limit`     | The maximum number of requests you're permitted to make per time period. | `X-RateLimit-Reset`     | The relative time in seconds until the current rate limit window resets. | `Retry-After`           | The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. | `X-RateLimit-Remaining` | The number of requests remaining in the current rate-limit window. **Important:** This differs from Github and Twitter\\'s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues.   Confluent enforces multiple kinds of limits, including request-rate and concurrency limits, both per user and organization-wide. Unauthenticated requests are associated with the originating IP address, not the user making requests.   Integrations should gracefully handle these limits by watching for `429` error responses and building in a retry mechanism. This mechanism should follow a capped exponential backoff policy to prevent [retry amplification](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/) (\"retry storms\") and also introduce some randomness (\"jitter\") to avoid the [thundering herd effect](https://en.wikipedia.org/wiki/Thundering_herd_problem).   If you’re running into this error and think you need a higher rate limit, contact Confluent at [support@confluent.io](mailto:support@confluent.io).  # Identifiers and URLs  Most resources have multiple identifiers: * `id` is the \"natural identifier\" for an object. It is only unique within its parent resource.   The `id` is unique across time: the ID will not be reclaimed and reused after an object is deleted. * `resource_name` is a Uniform Resource Identifier (URI) that is globally unique across all resources.   This encompasses all parent resource `kind`s and `id`s necessary to uniquely identify a particular   instance of this object `kind`. Because it uses object `id`s, the CRN will not be reclaimed and   reused after an object is deleted. It is represented as a Confluent Resource Name (see below).  * `self` is a Uniform Resource Locator (URL) at which an object can be addressed.   This URL encodes the service location, API version, and other particulars necessary to   locate the resource at a point in time.  To see how these relate to each other, consider `KafkaBroker` with `broker.id=2` in a `KafkaCluster` in Confluent Cloud identified as `lkc-xsi8201`. In such an example, the `KafkaBroker` has `id=2`, the `resource_name` is `crn://confluent.cloud/kafka=lkc-xsi8201/broker=2` and the `self` URL may be something like `https://pkc-8wlk2n.us-west-2.aws.confluent.cloud`. Note that different identifiers carry different information for different purposes, but the `resource_name` is the most complete and canonical identifier.  ## Confluent Resource Names (CRNs)  *Confluent Resource Names* (CRNs) are used to uniquely identify all Confluent resources.  A CRN is a valid URI having an \"authority\" of `confluent.cloud` or a self-managed <a href=\"https://docs.confluent.io/current/security/rbac/configure-mds/index.html\" target=\"_blank\"> metadata service URL</a>, followed by the minimal hierarchical set of key-value pairs necessary to uniquely identify a resource.  Here are some examples for basic resources in Confluent Cloud:  | Resource                   | Example CRN                                                                                                                                                              | |----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Organization               | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a                                                                                                  | | Environment                | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy                                                                            | | User                       | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/user=u-rst9876                                                                                   | | API Key                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/user=u-zyx98/api-key=ABCDEFG9876543210                                                           | | Service Account            | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/service-account=sa-abc1234                                                                       | | Kafka Cluster              | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc                                  | | Kafka Topic                | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc/topic=my_kafka_topic             | | Consumer Group             | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/cloud-cluster=lkc-123abc/kafka=lkc-123abc/group=confluent_cli_consumer_123 | | Network                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc                                                           | | Peering                    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/peering=p-123abc                                          | | Private Link Access        | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/private-link-access=pla-123abc                            | | Transit Gateway Attachment | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/network=n-123abc/transit-gateway-attachment=tgwa-123abc                    | | Schema Registry Cluster    | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/schema-registry=lsrc-789qw                                                 | | Schema Subject             | crn://confluent.cloud/organization=9bb441c4-edef-46ac-8a41-c49e44a3fd9a/environment=env-456xy/schema-registry=lsrc-789qw/subject=test                                    |  # Data Types  ## Primitive Types  | Data Type  | Representation |------------|--------------------- | Integers   | Each API may specify the type as `int32` or `int64`. Note that many languages, including JavaScript, are limited to a max size of approx `2**53` and don't correctly handle large `int64` values with their default JSON parser. | Dates      | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given. | Times      | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given. | Durations  | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. | Periods    | <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> formatted string. UTC timezones are assumed, unless otherwise given. | Ranges     | All ranges are represented using half-open intervals with naming conventions like `[start_XXX, end_XXX)` such as `[start_time, end_time)`. | Enums      | Most APIs use <a href=\"https://opensource.zalando.com/restful-api-guidelines/#112\" target=\"_blank\">`x-extensible-enum`</a> as an open-ended list of values. This improves compatibility compared with a standard `enum` which by definition represents a closed set. All enums have a `0`-valued entry which either serves as the default for common cases, or represents `UNSPECIFIED` when no default exists and results in an error.  <!-- TODO ### Standard Objects  | Money Object | https://schema.org/MonetaryAmount or https://opensource.zalando.com/restful-api-guidelines/#173 | Price Specification | https://schema.org/PriceSpecification -> https://schema.org/UnitPriceSpecification and https://schema.org/PaymentChargeSpecification -->  ### Standard Properties  Confluent uses this set of standard properties to ensure common concepts use the same name and semantics across different APIs.  | Name             | Description |------------------|------------------------------------------ | **api_version**  | Many API objects have an `api_version` field indicating their API version. See the [Object Model](#section/Object-Model). | **kind**         | Many API objects have a `kind` field indicating the kind of object it is. See the [Object Model](#section/Object-Model). | **id**           | Many objects in the API will have an identifier, indicated via its `id` field, and should be treated as an opaque string unless otherwise specified. See the [Object Model](#section/Object-Model). | **name**         | Objects which support a client-provided unique identifier instead of a generated `id` will indicate this identifier via its `name` field. | **display_name** | The human-readable display name of an API object. | **title**        | The official name of an API object, such as a company name. It should be treated as the formal version of `display_name`. | **description**  | One or more paragraphs of text description of an entity. | **created_at**   | The date and time the object was created, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format. | **updated_at**   | The date and time the object was last modified, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format. | **deleted_at**   | If present, the date and time after which the object was/will be deleted, represented as a string in <a href=\"https://www.ietf.org/rfc/rfc3339.txt\" target=\"_blank\">RFC 3339</a> format. | **page_token**   | The pagination token in the List request. See [Pagination](#section/Pagination). | **page_size**    | The pagination size in the List request. See [Pagination](#section/Pagination). | **total_size**   | The total count of items in the list irrespective of pagination. See [Pagination](#section/Pagination). | **spec**         | The _desired state_ specification of the resource, as observed by Confluent Cloud. | **status**       | The _current state_ of the resource, as observed by Confluent Cloud.  # Versioning  Confluent APIs ensure stability for your integrations by avoiding the introduction of breaking changes to customers unexpectedly. Confluent will make non-breaking API changes without advance notice. Thus, API clients **must**  follow the [Compatibility Policy](#section/Versioning/Compatibility-Policy) below to ensure your ingtegration remains stable. All APIs follow the API Lifecycle Policy described below, which describes the guarantees API clients can rely on.  Breaking changes will be [widely communicated](#communication) in advance in accordance with the Confluent [Deprecation Policy](#section/Versioning/Deprecation-Policy). Confluent will provide  timelines and a migration path for all API changes, where available. Be sure to subscribe to one or more [communication channels](#communication) so you don't miss any updates!  One exception to these guidelines is for critical security issues. Confluent will take any necessary actions to mitigate any critical security issue as soon as possible, which may include disabling the vulnerable functionality until a proper solution is available.  Do not consume any Confluent API unless it is documented in the API Reference. All undocumented endpoints should be considered private, subject to change without notice, and not covered by any agreements.  > Note: The version in the URL (e.g. \"v1\" or \"v2\") is not a \"major version\" in the [Semantic Versioning](https://semver.org/) sense. It is a \"generational version\" or \"meta version\", as seen in APIs like <a href=\"https://developer.github.com/v3/versions/\" target=\"_blank\">Github API</a> or the <a href=\"https://stripe.com/docs/api/versioning\" target=\"_blank\">Stripe API</a>.  ## API Groups  Confluent APIs are divided into API Groups, such as the Cluster Management for Apache Kafka (CMK) API group, the Connect API group, and the Data Catalog API group. Each group has its own set of endpoints and resources, as well as its own API group version.  Because different API groups have different versions, there is no single version for the \"Confluent Cloud API\". The latest version of the Connect API group may be `connect/v1`, while the latest version of the CMK API group may be `cmk/v2`.  When a breaking change is introduced into one API group, Confluent will increase the API version for that API group only, leaving the other API groups' versions unchanged. This makes it easier for you to understand whether a given breaking change impacts your usage of the APIs.  ## Known Issues  During the Early Access and Preview periods, we have a few known issues.  | Issue          | Description                                                                   | Proposed Resolution |----------------|-------------------------------------------------------------------------------|----------------------------------------------------- | Quota Exceeded | Some \"Quota Exceeded\" errors will be returned as HTTP 400 instead of HTTP 402 | Return 402 consistently for \"Quota Exceeded\" errors   ## API Lifecycle Policy  The following status labels are applicable to APIs, features, and SDK versions, based on the current support status of each:  * **Early Access** – May change at any time. Not recommended for production usage. Not officially supported by   Confluent. Intended for user feedback only. Users must be granted explicit access to the API by Confluent. * **Preview** – Unlikely to change between Preview and General Availability. Not recommended for production usage.   Officially supported by Confluent for non-production usage. Accessible to all users. * **Limited Availability (LA)** - Available to key select customers in a subset of regions/providers/networks and recommended for production usage.   * **Generally Available (GA)** – Will not change at short notice. Recommended for production usage.   Officially supported by Confluent for non-production and production usage. * **Deprecated** – Still supported, but no longer under active development. Existing usage will continue to function   but migration following the upgrade guide is strongly recommended. New use cases should be built against the new   version. Deprecated feature or version will be removed in the future at the announced date. * **Sunset** – Removed, and no longer supported or available.  An API is \"Generally Available\" unless explicitly marked otherwise.  ## Compatibility Policy  Confluent Cloud APIs are governed by <a href=\"https://docs.confluent.io/cloud/current/clusters/upgrade-policy.html\" target=\"_blank\"> Confluent Cloud Upgrade Policy</a>, which means that backward incompatible changes and deprecations will be made approximately once per year, and 180 days notice will be provided via email to all registered Confluent Cloud users.  ### Backward Compatibility  > _An API version is backward compatible if a program written against the previous version of the API will continue to work the same way, without modification, against this version of the API._  Confluent considers the following changes to be backward compatible:  * Adding new API resources. * Adding new optional parameters to existing API requests (e.g., query string). * Adding new properties to existing API resources (e.g., request body). * Changing the order of properties in existing API responses. * Changing the length or format of object IDs or other opaque strings.   * Unless otherwise documented, you can safely assume object IDs generated by Confluent will never exceed 255     characters, but you should be able to handle IDs of up to that length. If you're using MySQL,     for example, you should store IDs in a `VARCHAR(255) COLLATE utf8_bin` column.   * This includes adding or removing fixed prefixes (such as `lkc-` on Kafka cluster IDs).   * This includes API keys, API tokens, and similar authentication mechanisms.   * This includes all strings described as \"opaque\" in the docs, such as pagination cursors. * Adding new API event types. * Adding new properties to existing API event types. * Omitting properties with null values from existing API responses.  ### Forward Compatibility  > _An API version is forward compatible if a program written against the next version of the API > will continue to work the same way, without modification, against this version of the API._  In other words, a forward compatible API will accept input intended for a later version of itself.  Confluent does not guarantee the forward compatibility of the APIs, but Confluent does generally follow the guidelines given by the [Robustness principle](https://en.wikipedia.org/wiki/Robustness_principle). This means that the API determines what to do with a request based only on the parts that it recognizes.  This is often referred to as the MUST IGNORE rule.  * Request parameters that are not recognized will be ignored (e.g., query string). * Request properties that are not recognized will be ignored (e.g., request body). * Request metadata that are not recognized will be ignored (e.g., request headers).  API clients must also follow the MUST IGNORE rule.  * Response properties that are not recognized must be ignored (e.g., response body). * Response metadata that are not recognized must be ignored (e.g., response headers).  Additionally, there is a more subtle related rule called the MUST FORWARD rule. Any parts of a request that an API doesn't recognize must be forwarded unchanged.  * Response properties that are not recognized must be included in any input subsequent updates (e.g., request body)   * This includes future `PUT` requests in a read/modify/write operation.     (This isn't required for `PATCH` partial updates, which is why Confluent APIs use `PATCH`.) * Event processors must not strip unknown properties before forwarding messages.  ### Client Responsibilities  * Resource and rate limits, and the default and maximum sizes of paginated data **are not**   considered part of the API contract and may change (possibly dynamically). It is the client's   responsibility to read the road signs and obey the speed limit. * If a property has a primitive type and the API documentation does not explicitly limit its   possible values, clients **must not** assume the values are constrained to a particular set   of possible responses. * If a property of an object is not explicitly declared as mandatory in the API, clients   **must not** assume it will be present. * A resource **may** be modified to return a \"redirection\" response (e.g. `301`, `307`) instead of   directly returning the resource. Clients **must** handle HTTP-level redirects, and respect HTTP   headers (e.g. `Location`).  ## Deprecation Policy  Confluent will announce deprecations at least 180 days in advance of a breaking change and will continue to maintain the deprecated APIs in their original form during this time.  Exceptions to this policy apply in case of critical security vulnerabilities or functional defects.  ### Communication  When a deprecation is announced, the details and any relevant migration information will be available on one or more of the following channels:  * Announcements on the <a href=\"https://www.confluent.io/blog/\" target=\"_blank\">Developer Blog</a>,   <a href=\"https://confluentcommunity.slack.com\" target=\"_blank\">Community Slack</a>   (<a href=\"https://slackpass.io/confluentcommunity\" target=\"_blank\">join!</a>),   <a href=\"https://groups.google.com/forum/#!forum/confluent-platform\" target=\"_blank\">Google Group</a>,   the <a href=\"https://twitter.com/ConfluentInc\" target=\"_blank\">@ConfluentInc twitter</a>   account, and similar channels * Enterprise customers may receive information by email to their specified Confluent contact, if applicable.  <!-- TODO: ### Discoverability -->  # HTTP Guidelines  ## Status Codes  Confluent respects the meanings and behavior of HTTP status codes as defined in <a href=\"https://tools.ietf.org/html/rfc2616\">RFC2616</a> and elsewhere.  * Codes in the `2xx` range indicate success * Codes in the `3xx` range indicate redirection * Codes in the `4xx` range indicate an error caused by the client request   (e.g., a required parameter was omitted, an invalid cluster configuration was provided, etc.) * Codes in the `5xx` range indicate an error with Confluent's servers (these are rare)  The various HTTP status codes that might be returned are listed below.  | Code | Title                  | Description |------|------------------------|-------------------------------- | 200  | OK                     | Everything worked as expected. | 201  | Created                | The resource was created. Follow the `Location` header. | 204  | No Content             | Everything worked and there is no content to return. | 400  | Bad Request         | The request was unacceptable, often due to malformed syntax, or a missing or malformed parameter. | 401  | Unauthorized           | No valid credentials provided. or the credentials are unsuitable, invalid, or unauthorized. | 402  | Over Quota             | The request was valid, but you've exceeded your plan quota or limits. | 404  | Not Found              | The requested resource doesn't exist or you're unauthorized to know it exists. | 409  | Conflict               | The request conflicts with another request (perhaps it already exists or was based on a stale version of data). | 422  | Validation Failed      | The request was parsed correctly but failed some sort of validation. | 429  | Too Many Requests      | Too many requests hit the API too quickly. Confluent recommends an exponential backoff of your requests. | 500, 502, 503, 504 | Server Errors | Something went wrong on Confluent's end. (These are rare.)  This list is not exhaustive; other standard HTTP error codes may be used, including `304`, `307`, `308`, `405`, `406`, `408`, `410`, and `415`.  For more details, see https://httpstatuses.com.  <!--  ## Method Overriding  Some firewalls and HTTP clients restrict the use of verbs other than `GET` and `POST`. In those environments, Confluent API operations that require `PUT`, `PATCH`, and `DELETE` verbs will be inaccessible.  To avoid this issue, Confluent APIs support the `X-HTTP-Method-Override` header, allowing clients to \"tunnel\" `PUT`, `PATCH`, and `DELETE` requests via a `POST` request.  For example, to call a Confluent `PATCH` resource via a `POST` request, you can include `X-HTTP-Method-Override: PATCH` as a header.  ## User Agent Required  Confluent API requests **should** include a valid `User-Agent` header. Requests with no `User-Agent` header may be rejected. You should use the name of your integration for the `User-Agent` header value and include contact information so that Confluent can contact you if there are problems.  > If your integration is acting as a proxy or gateway, you **should** forward the User-Agent > of the originating client with your API requests.  Here's a complete example:      User-Agent: CoolToolName/1.2.3 (https://example.org/CoolTool/; CoolTool@example.org) UsedBaseLibrary/2.1.0  The minimum user agent string is the integration name and version: `name/version`. You can string together multiple values in a space-separated list. The full syntax is:      name/version [(comments)] [name/version [(comments)]] [...]​  For the integration name, use a string (without whitespace) that clearly and meaningfully identifies your integration.  * Avoid ambiguous names: `Confluent-Integration`, `Kafka-Sink` * Use clear and meaningful names: `ABCTools-ToolName`, `StackStorm-Confluent-Plugin`  For the version, use a semantic version, build ID, commit hash, or other identifier that is updated automatically when you release a new version.  Wrap comments in parentheses `()` as a semi-colon separated list. Helpful comments to include:  * A public URL for your integration, such as a GitHub link or a page in your   docs site that describes the integration. * Contact information so that Confluent can easily reach the integration publisher. This   information from the user agent string will never be shared nor used by Confluent for   any purpose other than discussing the integration with its publisher.  If you provide an invalid `User-Agent` header, you may receive a `403 Forbidden` response.  -->  # Metrics APIs  For Metrics APIs, see <a href=\"https://api.telemetry.confluent.cloud/docs\">Confluent Cloud Metrics API</a>.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@confluent.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError



class AlterMirrorsRequestData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'mirror_topic_names': ([str],),  # noqa: E501
            'mirror_topic_name_pattern': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'mirror_topic_names': 'mirror_topic_names',  # noqa: E501
        'mirror_topic_name_pattern': 'mirror_topic_name_pattern',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AlterMirrorsRequestData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            mirror_topic_names ([str]): The mirror topics specified as a list of topic names.. [optional]  # noqa: E501
            mirror_topic_name_pattern (str): The mirror topics specified as a pattern.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AlterMirrorsRequestData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            mirror_topic_names ([str]): The mirror topics specified as a list of topic names.. [optional]  # noqa: E501
            mirror_topic_name_pattern (str): The mirror topics specified as a pattern.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
