# ISXOgre API Reference

The `ISXOgre` top-level object exposes utility members and methods that the rest of OgreBot, OgreCraft, and your own scripts can use directly. This page documents the public, script-facing surface.

> **Note:** This reference will grow over time. It currently covers the Base64 encoding/decoding helpers. Additional APIs will be added here as they become officially supported for external script use.

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
