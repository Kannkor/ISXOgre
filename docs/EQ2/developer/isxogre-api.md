# ISXOgre API Reference

The `ISXOgre` top-level object exposes utility members and methods that the rest of OgreBot, OgreCraft, and your own scripts can use directly. This page documents the public, script-facing surface.

> **Note:** This reference will grow over time. It currently covers the Base64 encoding/decoding helpers, the async HTTP request API (`HttpRequestSubmit` / `HttpRequest` / `HttpLastSubmitError` / `SetFormBodyB64` plus the `ogrehttpjob` datatype). Additional APIs will be added here as they become officially supported for external script use.

---

## Base64 Encoding & Decoding

ISXOgre ships a pair of matched helpers, `Base64Encode` and `Base64Decode`, that work in two complementary modes:

- **Method form** — `ISXOgre:Base64Encode[...]` / `ISXOgre:Base64Decode[...]` — writes the result back into a destination `jsonvalue` you supply.
- **Member form** — `${ISXOgre.Base64Encode[...]}` / `${ISXOgre.Base64Decode[...]}` — returns the result as a `string` for inline use.

Both forms accept exactly two kinds of source argument:

- **A `jsonvalue` reference** — auto-dereferenced; the call operates on the variable's canonical JSON serialization.
- **Anything else** — treated as a **literal string**. No name lookup is performed on the argument.

To pass a `variable string`'s **value** (rather than its name), pre-interpolate at the call site with `${myStr~}`. See each section below for examples.

### Round-Trip Shape

`Base64Encode` always writes its output as a **JSON string scalar** — the destination `jsonvalue`'s `.AsJSON` will be a quoted base64 token, e.g. `"SGVsbG8sIHdvcmxkIQ=="`.

`Base64Decode` reverses this by inspecting the decoded bytes:

- If the decoded payload **is** valid JSON (object, array, number, `true`/`false`/`null`, or a quoted string scalar), the destination becomes a real `jsonvalue` of that shape.
- If the decoded payload is **plain text** (the common case for encoded strings), the destination becomes a JSON string scalar of that text.

The practical effect: encode a `jsonvalue` object → get back a base64 token → decode it → you have the original `jsonvalue` object again. Encode a string → get back a base64 token → decode it → you have a `jsonvalue` string scalar whose unwrapped value (`${var~}`) is the original string.

> **Note:** Both decode paths return text via a null-terminated C string internally, so embedded NUL bytes in the decoded payload will truncate. Intended use is text round-trips (JSON, ASCII, UTF-8 strings), not arbitrary binary data.

---

### Base64Encode — Method

Encode a source value into a destination `jsonvalue`.

**Syntax:**

```
ISXOgre:Base64Encode[<jsonref>]                    ; in-place
ISXOgre:Base64Encode[<jsonref-source>, <jsonref-destination>]
ISXOgre:Base64Encode[<string-source>,  <jsonref-destination>]
```

| Variant | argv[0] | argv[1] | Behavior |
|---------|---------|---------|----------|
| **In-place** | `jsonvalue` | *(not used)* | Read `argv[0]`'s `.AsJSON`, encode, write the result back into `argv[0]` |
| **jsonref → jsonref** | `jsonvalue` reference | `jsonvalue` (destination) | Read `argv[0]`'s `.AsJSON`, encode, write into `argv[1]`. `argv[0]` unchanged. |
| **literal → jsonref** | Anything that is **not** a `jsonvalue` reference (treated as literal text) | `jsonvalue` (destination) | Encode the literal text, write into `argv[1]` |

> **Note:** Bare names like `myStringVar` are **not** auto-dereferenced — they're encoded as the literal text `"myStringVar"`. To encode a string variable's value, pre-interpolate at the call site: `ISXOgre:Base64Encode["${myStringVar~}", dst]`.

The destination must be a `jsonvalue`. Passing any other variable type prints an error to the console and the call is a no-op:

```
ISXOgre:Base64Encode -- destination 'badDst' must be a jsonvalue (jsonvaluecontainer); got type 'int'
```

**Example — in-place encode of a JSON object:**

```
variable jsonvalue payload
payload:SetValue["{\"foo\":\"bar\",\"n\":42}"]
echo Before: ${payload.AsJSON~}

ISXOgre:Base64Encode[payload]
echo After:  ${payload.AsJSON~}
echo Raw:    ${payload~}
```

**Output:**

```
Before: {"foo":"bar","n":42}
After:  "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
Raw:    eyJmb28iOiJiYXIiLCJuIjo0Mn0=
```

**Example — encode a `jsonvalue` source into a separate destination:**

```
variable jsonvalue src
variable jsonvalue dst
src:SetValue["{\"foo\":\"bar\",\"n\":42}"]

ISXOgre:Base64Encode[src, dst]
echo src.AsJSON: ${src.AsJSON~}    ; unchanged
echo dst.AsJSON: ${dst.AsJSON~}
```

**Output:**

```
src.AsJSON: {"foo":"bar","n":42}
dst.AsJSON: "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
```

**Example — encode the value of a string variable into a `jsonvalue` destination:**

Use `${...~}` pre-interpolation so the *value* gets passed, not the variable's name:

```
variable string    plaintext = "Hello, world!"
variable jsonvalue dst

ISXOgre:Base64Encode["${plaintext~}", dst]
echo ${dst.AsJSON~}
```

**Output:**

```
"SGVsbG8sIHdvcmxkIQ=="
```

> **Note:** Writing `ISXOgre:Base64Encode[plaintext, dst]` (no `${...~}`) would encode the literal text `plaintext` — not its value. Bare names are treated as literal strings.

**Example — encode a literal string:**

```
variable jsonvalue dst
ISXOgre:Base64Encode["Hello, world!", dst]
echo ${dst.AsJSON~}
```

**Output:**

```
"SGVsbG8sIHdvcmxkIQ=="
```

> **Note:** When passing a literal string with quotes that should be part of the encoded value, escape them with `\"`:
>
> ```
> ISXOgre:Base64Encode["\"Hello, world!\"", dst]
> echo ${dst~}    ; -> IkhlbGxvLCB3b3JsZCEi (b64 of `"Hello, world!"`)
> ```

---

### Base64Encode — Member

Encode a source value and return the base64 token as a `string`.

**Syntax:** `${ISXOgre.Base64Encode[<source>]}`

| `<source>` shape | Result |
|------------------|--------|
| `jsonvalue` variable name | Base64 of the variable's JSON serialization (auto-deref) |
| Anything else — string literal, `${var~}` pre-interpolation, bare identifier, etc. | Base64 of the literal argument text |

To encode the **value** of a string variable, pre-interpolate with `${var~}`. A bare name like `plaintext` will be encoded as the literal text `"plaintext"`.

**Example:**

```
variable string    plaintext = "Hello, world!"
variable jsonvalue payload
payload:SetValue["{\"foo\":\"bar\",\"n\":42}"]

echo Literal:        ${ISXOgre.Base64Encode["Hello, world!"]~}
echo StringValue:    ${ISXOgre.Base64Encode["${plaintext~}"]~}
echo BareName:       ${ISXOgre.Base64Encode[plaintext]~}
echo JsonRef:        ${ISXOgre.Base64Encode[payload]~}
```

**Output:**

```
Literal:        SGVsbG8sIHdvcmxkIQ==
StringValue:    SGVsbG8sIHdvcmxkIQ==
BareName:       cGxhaW50ZXh0
JsonRef:        eyJmb28iOiJiYXIiLCJuIjo0Mn0=
```

Note that `StringValue` (uses `"${plaintext~}"` pre-interpolation) and `BareName` (uses the literal text `plaintext`) produce different results — exactly because there's no implicit name resolution.

> **Note:** Always wrap pre-interpolated values in `"..."` — without the quotes, a value containing commas (like `Hello, world!`) would split into multiple arguments and the member would reject it. The same rule applies in `Base64Decode` and in the method form.

> **Note:** The member form returns the **raw base64 token** (no surrounding quotes), unlike the method form which writes a JSON string scalar (`"<b64>"`) into its destination. Use `${ISXOgre.Base64Encode[x]~}` whenever you want to drop a base64 token directly into another string, URL parameter, log line, etc.

---

### Base64Decode — Method

Decode a base64 source into a destination `jsonvalue`.

**Syntax:**

```
ISXOgre:Base64Decode[<jsonref>]                    ; in-place
ISXOgre:Base64Decode[<jsonref-source>, <jsonref-destination>]
ISXOgre:Base64Decode[<string-source>,  <jsonref-destination>]
```

| Variant | argv[0] | argv[1] | Behavior |
|---------|---------|---------|----------|
| **In-place** | `jsonvalue` holding `"<b64>"` | *(not used)* | Read `argv[0]`'s scalar, decode, write the decoded payload back into `argv[0]` |
| **jsonref → jsonref** | `jsonvalue` reference holding `"<b64>"` | `jsonvalue` (destination) | Read `argv[0]`'s scalar, decode, write into `argv[1]`. `argv[0]` unchanged. |
| **literal → jsonref** | Anything that is **not** a `jsonvalue` reference (treated as literal base64 text) | `jsonvalue` (destination) | Decode the literal base64, write into `argv[1]` |

> **Note:** Same name-resolution contract as `Base64Encode`: bare names are literal text, not variable lookups. To decode the value held by a `variable string`, use `ISXOgre:Base64Decode["${myB64~}", dst]`.

The destination must be a `jsonvalue`. Same type-check error as `Base64Encode` if you pass anything else.

The destination's resulting shape depends on what the decoded bytes look like (see [Round-Trip Shape](#round-trip-shape) above).

**Example — in-place decode of a base64-encoded JSON object:**

```
variable jsonvalue payload
payload:SetValue["\"eyJmb28iOiJiYXIiLCJuIjo0Mn0=\""]
echo Before: ${payload.AsJSON~}

ISXOgre:Base64Decode[payload]
echo After:  ${payload.AsJSON~}
echo Get[foo]: ${payload.Get[foo]~}
```

**Output:**

```
Before: "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
After:  {"foo":"bar","n":42}
Get[foo]: bar
```

The decoded payload was valid JSON, so `payload` is now a real `jsonvalue` object you can index into with `.Get[...]`.

**Example — decode plain text into a `jsonvalue`:**

```
variable jsonvalue dst
ISXOgre:Base64Decode["SGVsbG8sIHdvcmxkIQ==", dst]
echo dst.AsJSON: ${dst.AsJSON~}
echo dst raw:    ${dst~}
```

**Output:**

```
dst.AsJSON: "Hello, world!"
dst raw:    Hello, world!
```

The decoded payload (`Hello, world!`) was plain text, so `dst` becomes a JSON string scalar. Use `${dst~}` to retrieve the unwrapped value.

**Example — decode the value held by a string variable:**

Pre-interpolate with `${...~}` so the value (not the variable's name) is passed:

```
variable string    b64       = "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
variable jsonvalue restored

ISXOgre:Base64Decode["${b64~}", restored]
echo ${restored.AsJSON~}
```

**Output:**

```
{"foo":"bar","n":42}
```

> **Note:** Writing `ISXOgre:Base64Decode[b64, restored]` (no `${...~}`) would try to decode the literal text `"b64"` — not the variable's value.

---

### Base64Decode — Member

Decode a base64 source and return the decoded bytes as a `string`.

**Syntax:** `${ISXOgre.Base64Decode[<source>]}`

| `<source>` shape | Result |
|------------------|--------|
| `jsonvalue` variable holding `"<b64>"` | Decoded text of the stored scalar (auto-deref) |
| Anything else — string literal, `${var~}` pre-interpolation, bare identifier, etc. | Decoded text of the literal argument |

To decode the **value** of a string variable, pre-interpolate with `${var~}`. A bare name like `b64` will be decoded as if it were itself the base64 input.

The outer JSON-string quotes on a `jsonvalue` source are stripped automatically before decoding (the base64 alphabet `[A-Za-z0-9+/=]` never contains `"`, so the strip is unambiguous).

**Example:**

```
variable string    b64       = "SGVsbG8sIHdvcmxkIQ=="
variable jsonvalue encoded
encoded:SetValue["\"eyJmb28iOiJiYXIiLCJuIjo0Mn0=\""]

echo Literal:      ${ISXOgre.Base64Decode["SGVsbG8sIHdvcmxkIQ=="]~}
echo StringValue:  ${ISXOgre.Base64Decode["${b64~}"]~}
echo JsonRef:      ${ISXOgre.Base64Decode[encoded]~}
```

**Output:**

```
Literal:      Hello, world!
StringValue:  Hello, world!
JsonRef:      {"foo":"bar","n":42}
```

> **Note:** The member form always returns the decoded bytes as a string. When the decoded payload is itself JSON, you typically want the **method** form instead so you can index into the result with `.Get[...]`, `.Type`, etc. Use the member form when you want the decoded text inline (logging, comparison, passing as another method argument).

---

### Full Round-Trip Examples

**Round-trip a JSON object:**

```
variable jsonvalue original
variable jsonvalue encoded
variable jsonvalue restored

original:SetValue["{\"foo\":\"bar\",\"n\":42}"]

ISXOgre:Base64Encode[original, encoded]
ISXOgre:Base64Decode[encoded,  restored]

echo Original: ${original.AsJSON~}
echo Encoded:  ${encoded.AsJSON~}
echo Restored: ${restored.AsJSON~}
echo Match:    ${original.AsJSON.Equal[${restored.AsJSON~}]}
```

**Output:**

```
Original: {"foo":"bar","n":42}
Encoded:  "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
Restored: {"foo":"bar","n":42}
Match:    TRUE
```

**Round-trip a plain string:**

```
variable string    original = "Hello, world!"
variable jsonvalue encoded
variable jsonvalue restored

ISXOgre:Base64Encode["${original~}", encoded]   ; pre-interp so the *value* is encoded
ISXOgre:Base64Decode[encoded,         restored] ; jsonref source -> auto-deref

echo Original:  ${original~}
echo Encoded:   ${encoded.AsJSON~}
echo Restored:  ${restored~}                 ; unwrapped scalar value
echo As JSON:   ${restored.AsJSON~}          ; JSON string scalar form
```

**Output:**

```
Original:  Hello, world!
Encoded:   "SGVsbG8sIHdvcmxkIQ=="
Restored:  Hello, world!
As JSON:   "Hello, world!"
```

---

### Use Cases

- **Logging and diagnostics:** safely embed multi-line, quote-heavy, or otherwise structurally-unfriendly payloads in single-line log entries or chat-style transports without escaping concerns.
- **Cross-session command payloads:** send JSON payloads through transports that don't tolerate raw `{`, `}`, `"` characters by encoding before transmission and decoding on receipt.
- **HTTP request bodies / URL parameters:** pre-encode binary-ish or quote-heavy strings before composing them into request bodies.
- **Persistent storage:** stash a complex `jsonvalue` as a single opaque token in a settings file, then restore it on next load.

---

## HTTP Requests (async)

ISXOgre exposes an asynchronous HTTP client built on libcurl. Submissions return immediately with a job handle — the request runs on a worker thread, and the script either polls the handle each frame or supplies an atom that gets called back on the main thread when the job completes.

The API is split across:

- `${ISXOgre.HttpRequestSubmit[<spec>, <body>]}` — submit a request. Returns an `ogrehttpjob` handle.
- `${ISXOgre.HttpRequest[<id>]}` — re-acquire an `ogrehttpjob` handle by its job id (useful for callback-flavored jobs whose id was stashed earlier).
- `${ISXOgre.HttpLastSubmitError}` — string describing why the most recent `HttpRequestSubmit` returned id=0, if it did.
- `ISXOgre:SetFormBodyB64[...]` — helper for building base64-encoded `x-www-form-urlencoded` bodies entirely in C++ (avoids the LavishScript ~24 KB string-handling ceiling on large payloads).

The `ogrehttpjob` datatype (returned by both `HttpRequestSubmit` and `HttpRequest`) is documented at the end of this section.

> **Note:** Bodies always pass through `HttpRequestSubmit` as a **separate** `jsonvalue` (the 2nd argument). The body lives at the root of that `jsonvalue` as a JSON string scalar. This single contract handles bodies of any size; there is no separate path for "small" vs. "large" bodies.

---

### Request Spec — fields recognised by HttpRequestSubmit

The 1st argument to `HttpRequestSubmit` is the **name** of a `jsonvalue` describing the request:

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| `url` | string | *(required)* | Full URL including scheme. |
| `method` | string | `"GET"` | `GET` / `POST` / `PUT` / `DELETE` / etc. |
| `content_type` | string | *(unset)* | If non-empty, sent as a `Content-Type:` header. |
| `headers` | array of strings | *(unset)* | Each entry is a full `"Name: Value"` header line, e.g. `"Authorization: Bearer ..."` |
| `timeout_sec` | int | `30` | Overall request timeout (libcurl `CURLOPT_TIMEOUT`). |
| `connect_timeout_sec` | int | `10` | TCP/TLS connect timeout (libcurl `CURLOPT_CONNECTTIMEOUT`). |
| `release_after_callback` | bool | atom-flavor: `TRUE`, polling-flavor: `FALSE` | If TRUE, the job slot is freed automatically once the script-side callback returns / once the job transitions to `Completed`/`Failed` and is read. |

The spec **never** holds the request body. Build the body in a separate `jsonvalue` and pass it as the 2nd argument.

---

### HttpRequestSubmit — Member

Submit an HTTP request. Returns an `ogrehttpjob` whose `.ID` is the assigned job id, or `0` on submit failure.

**Syntax:**

```
${ISXOgre.HttpRequestSubmit[<specJsonref>, <bodyJsonref>]}
${ISXOgre.HttpRequestSubmit[<specJsonref>, <bodyJsonref>, <atomName>]}
```

| argv[0] | argv[1] | argv[2] | Behavior |
|---------|---------|---------|----------|
| `jsonvalue` (spec) | `jsonvalue` (body) | *(omitted)* | **Polling flavor.** Script polls `${ISXOgre.HttpRequest[id].Complete}` each frame. Caller is responsible for `:Release` when done. |
| `jsonvalue` (spec) | `jsonvalue` (body) | atom name (string) | **Callback flavor.** The atom is invoked on the main thread as `call <atomName> <id>` once the job completes. Slot auto-released after the callback returns (unless the spec explicitly sets `release_after_callback` to `FALSE`). |

The body `jsonvalue` must hold a JSON string scalar at its root. Two patterns produce this:

- **Inline small bodies** — write directly with `:SetValue["\"...\""]`. The outer `\"...\"` makes it a JSON string scalar.
- **Form-encoded large bodies** — use `ISXOgre:SetFormBodyB64[...]` to assemble the body in C++.

On submit failure (`id == 0`), check `${ISXOgre.HttpLastSubmitError~}` for the reason.

**Example — polling flavor, small inline body:**

```
variable jsonvalue jvSpec
variable jsonvalue jvFormBody
variable jsonvalue jvHeaders
variable int       iJobId

jvHeaders:SetValue["[]"]
jvHeaders:AddString["Accept: application/json"]

jvSpec:SetValue["{}"]
jvSpec:SetString[url,"https://api.example.com/v1/sessions"]
jvSpec:SetString[method,"POST"]
jvSpec:SetString[content_type,"application/x-www-form-urlencoded"]
jvSpec:SetInteger[timeout_sec,30]
jvSpec:Set[headers,"${jvHeaders~}"]

; root scalar = JSON string scalar holding the URL-encoded form body
jvFormBody:SetValue["\"username=alice&duration=300\""]

iJobId:Set[${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody].ID}]
if ${iJobId} <= 0
{
    echo "submit failed: ${ISXOgre.HttpLastSubmitError~}"
    return
}

; Poll until the worker thread finishes the request
while !${ISXOgre.HttpRequest[${iJobId}].Complete}
    waitframe

if ${ISXOgre.HttpRequest[${iJobId}].Ok}
    echo "OK ${ISXOgre.HttpRequest[${iJobId}].Status}  body=${ISXOgre.HttpRequest[${iJobId}].Body~}"
else
    echo "FAIL state=${ISXOgre.HttpRequest[${iJobId}].State~}  status=${ISXOgre.HttpRequest[${iJobId}].Status}"

ISXOgre.HttpRequest[${iJobId}]:Release
```

**Example — callback flavor:**

```
atom MyCallback(int iJobId)
{
    if ${ISXOgre.HttpRequest[${iJobId}].Ok}
        echo "OK ${ISXOgre.HttpRequest[${iJobId}].Status}"
    else
        echo "FAIL state=${ISXOgre.HttpRequest[${iJobId}].State~}"
    ; Job slot auto-releases after this atom returns (release_after_callback default).
}

function:int LaunchRequest()
{
    variable jsonvalue jvSpec
    variable jsonvalue jvFormBody
    variable int       iJobId

    jvSpec:SetValue["{}"]
    jvSpec:SetString[url,"https://api.example.com/v1/ping"]
    jvSpec:SetString[method,"GET"]
    jvSpec:SetInteger[timeout_sec,10]

    ; GET with no body -- still required to pass an empty body jsonvalue
    jvFormBody:SetValue["\"\""]

    iJobId:Set[${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody, MyCallback].ID}]
    return ${iJobId}
}
```

> **Note:** GETs that have no body still take a 2nd argument. Pass a `jsonvalue` whose root is the empty JSON string scalar `""` (`:SetValue["\"\""]`).

> **Note:** The body bytes must be 7-bit ASCII suitable for `x-www-form-urlencoded` transmission (URL-encoded ASCII or base64-then-URL-encoded). Bodies containing raw `"`, `\`, or control characters are not safe through the typed read path used by `HttpRequestSubmit` and may not round-trip byte-for-byte.

---

### HttpRequest — Member

Look up an existing job handle by its job id. Returns an `ogrehttpjob` whose `.Exists` is `FALSE` if the id doesn't correspond to a known job (or it has been released).

**Syntax:** `${ISXOgre.HttpRequest[<id>]}`

Typical use is inside an atom callback or in a separate poll loop that only kept the id around:

```
variable int iJobId = ${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody].ID}

; ... later, possibly in a different scope ...

if ${ISXOgre.HttpRequest[${iJobId}].Complete}
    echo "${ISXOgre.HttpRequest[${iJobId}].Status}: ${ISXOgre.HttpRequest[${iJobId}].Body~}"
```

---

### HttpLastSubmitError — Member

String. Holds the reason the most recent `HttpRequestSubmit` returned `id == 0`. Empty string if the most recent submit succeeded.

**Syntax:** `${ISXOgre.HttpLastSubmitError}`

**Example:**

```
iJobId:Set[${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody].ID}]
if ${iJobId} <= 0
    echo "submit error: ${ISXOgre.HttpLastSubmitError~}"
```

Common reasons surfaced via this member:

- Missing or empty `url` in the spec.
- Spec / body `jsonvalue` could not be resolved by name (not declared, or wrong type).
- Body `jsonvalue` is not a `jsonvaluecontainer`.

---

### SetFormBodyB64 — Method

Build an `x-www-form-urlencoded` body of the form `<fieldName>=<urlencoded(base64(src.AsJSON))>` entirely in C++ and write it as a JSON string scalar at the root of `dstBody`. Pass `dstBody` to `HttpRequestSubmit` as the 2nd argument.

This helper exists specifically to keep large payloads out of LavishScript's expression evaluator. Bodies above ~24 KB cannot reliably be assembled or read through `${...}` text expansion; `SetFormBodyB64` performs the entire base64-encode + URL-encode + JSON-escape + assignment chain inside the extension.

**Syntax:**

```
ISXOgre:SetFormBodyB64[<fieldName>, <srcJsonref>, <dstBodyJsonref>]
```

| argv[0] | argv[1] | argv[2] | Behavior |
|---------|---------|---------|----------|
| `string` (form field name, e.g. `"payload_b64"`) | `jsonvalue` (source — the JSON tree to encode) | `jsonvalue` (destination — receives the assembled form body at its root) | Reads `src.AsJSON`, base64-encodes the bytes, URL-encodes the base64 token, prepends `<fieldName>=`, and writes the resulting form body into `dst` as a JSON string scalar. |

`dstBody` is **replaced** (via `SetValue`) — any previous contents are discarded.

**Example — POST a large JSON tree, base64-wrapped, in a single form field:**

```
variable jsonvalue jvPayload
variable jsonvalue jvSpec
variable jsonvalue jvFormBody
variable jsonvalue jvHeaders
variable int       iJobId

; Build the structured payload as a normal jsonvalue
jvPayload:SetValue["{}"]
jvPayload:SetString[name,"Example Item"]
jvPayload:SetInteger[level,100]
jvPayload:Set[tags,"[\"rare\",\"crafted\"]"]

; Build the request spec
jvHeaders:SetValue["[]"]
jvHeaders:AddString["Accept: application/json"]
jvHeaders:AddString["Authorization: Bearer <token>"]

jvSpec:SetValue["{}"]
jvSpec:SetString[url,"https://api.example.com/v1/items"]
jvSpec:SetString[method,"POST"]
jvSpec:SetString[content_type,"application/x-www-form-urlencoded"]
jvSpec:SetInteger[timeout_sec,60]
jvSpec:Set[headers,"${jvHeaders~}"]

; Assemble the form body in C++ (the entire base64+urlencode pipeline)
ISXOgre:SetFormBodyB64["payload_b64", jvPayload, jvFormBody]

; jvFormBody now contains:
;   "payload_b64=eyJuYW1lIjoiRXhhbXBsZSBJdGVtIiwibGV2ZWwiOjEwMCwidGFncyI6WyJyYXJlIiwiY3JhZnRlZCJdfQ%3D%3D"

iJobId:Set[${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody].ID}]

while !${ISXOgre.HttpRequest[${iJobId}].Complete}
    waitframe

echo "status=${ISXOgre.HttpRequest[${iJobId}].Status}"
ISXOgre.HttpRequest[${iJobId}]:Release
```

The server side reverses this in one step: URL-decode → base64-decode → parse JSON. No payload-size ceiling: payloads of tens of kilobytes have been verified end-to-end via this path.

> **Note:** `SetFormBodyB64` is the recommended path for any body large enough to make `${jvSrc.AsJSON~}` round-tripping inside LavishScript awkward. For small bodies (under a few KB) the manual `jvFormBody:SetValue["\"<urlencoded form>\""]` pattern is simpler and equally correct.

---

### ogrehttpjob — Datatype

Handle to a single async HTTP request. Returned by `${ISXOgre.HttpRequestSubmit[...]}` and `${ISXOgre.HttpRequest[<id>]}`. The handle is just the job id encoded into the LSOBJECT — there is no per-handle allocation, and you can re-acquire a handle for the same id any number of times.

#### Members

| Member | Type | Notes |
|--------|------|-------|
| `ID` | int | The underlying job id. `0` if the submit failed (`Exists` will be `FALSE`). |
| `State` | string | `"Pending"` / `"Completed"` / `"Failed"` / `"None"`. `"None"` means the id has been released or never existed. |
| `Status` | int | HTTP status code. `0` until completion. |
| `Body` | string | Response body. Empty until completion. |
| `Error` | string | libcurl error string. Empty unless `State == "Failed"`. |
| `Ok` | bool | `TRUE` iff `State == "Completed"` and `Status` is 2xx. |
| `Complete` | bool | `TRUE` iff `State` is `Completed` **or** `Failed`. Use this to exit a poll loop. |
| `Exists` | bool | `TRUE` iff a job record exists for this id (not yet released and not bogus). |

#### Methods

| Method | Notes |
|--------|-------|
| `:Release` | Frees the slot. Required for polling-flavor jobs once you've read the result. Atom-flavor jobs auto-release after the callback returns unless `release_after_callback=FALSE` was set in the spec. |

**Example — polling pattern:**

```
variable int iJobId = ${ISXOgre.HttpRequestSubmit[jvSpec, jvFormBody].ID}
variable int iFrames=0

while !${ISXOgre.HttpRequest[${iJobId}].Complete} && ${iFrames:Inc} < 600
    waitframe

if !${ISXOgre.HttpRequest[${iJobId}].Complete}
{
    echo "timeout after ${iFrames} frames (state=${ISXOgre.HttpRequest[${iJobId}].State~})"
    ISXOgre.HttpRequest[${iJobId}]:Release
    return
}

if ${ISXOgre.HttpRequest[${iJobId}].Ok}
    echo "OK: ${ISXOgre.HttpRequest[${iJobId}].Body~}"
else
    echo "FAIL ${ISXOgre.HttpRequest[${iJobId}].Status}: ${ISXOgre.HttpRequest[${iJobId}].Error~}"

ISXOgre.HttpRequest[${iJobId}]:Release
```

---

### HTTP Use Cases

- **REST API integration:** POST structured data to a web service from inside an EQ2 session without blocking the main thread / freezing the client.
- **Large-payload uploads:** when a body would otherwise exceed LavishScript's ~24 KB string-handling ceiling (the wedge that motivated `SetFormBodyB64`).
- **Webhook / Discord posts:** fire-and-forget POSTs with an atom callback for logging the result.
- **Async pull jobs:** kick off a `GET` against an internal service at the start of a fight and consume the response a few seconds later when it's needed.
