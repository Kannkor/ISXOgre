# ISXOgre API Reference

The `ISXOgre` top-level object exposes utility members and methods that the rest of OgreBot, OgreCraft, and your own scripts can use directly. This page documents the public, script-facing surface.

> **Note:** This reference will grow over time. It currently covers the Base64 encoding/decoding helpers. Additional APIs will be added here as they become officially supported for external script use.

---

## Base64 Encoding & Decoding

ISXOgre ships a pair of matched helpers, `Base64Encode` and `Base64Decode`, that work in two complementary modes:

- **Method form** — `ISXOgre:Base64Encode[...]` / `ISXOgre:Base64Decode[...]` — writes the result back into a destination `jsonvalue` you supply.
- **Member form** — `${ISXOgre.Base64Encode[...]}` / `${ISXOgre.Base64Decode[...]}` — returns the result as a `string` for inline use.

Both forms accept literal strings, string variables, and `jsonvalue` references as inputs and resolve them through the same logic, so you can pass whatever shape is convenient at the call site.

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
| **jsonref → jsonref** | `jsonvalue` | `jsonvalue` (destination) | Read `argv[0]`'s `.AsJSON`, encode, write into `argv[1]`. `argv[0]` unchanged. |
| **string → jsonref** | `string` variable, literal, or LavishScript expression | `jsonvalue` (destination) | Encode the string value, write into `argv[1]` |

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

**Example — encode a string variable into a `jsonvalue` destination:**

```
variable string    plaintext = "Hello, world!"
variable jsonvalue dst

ISXOgre:Base64Encode[plaintext, dst]
echo ${dst.AsJSON~}
```

**Output:**

```
"SGVsbG8sIHdvcmxkIQ=="
```

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
| String literal | Base64 of the bare text |
| `variable string` name | Base64 of the variable's value |
| `jsonvalue` variable name | Base64 of the variable's JSON serialization |
| Any LavishScript expression resolving to a string (e.g. `Me.Name`) | Base64 of the resolved value |

**Example:**

```
variable string    plaintext = "Hello, world!"
variable jsonvalue payload
payload:SetValue["{\"foo\":\"bar\",\"n\":42}"]

echo Literal:    ${ISXOgre.Base64Encode["Hello, world!"]~}
echo StringVar:  ${ISXOgre.Base64Encode[plaintext]~}
echo JsonRef:    ${ISXOgre.Base64Encode[payload]~}
echo Expression: ${ISXOgre.Base64Encode[Me.Name]~}
```

**Output:**

```
Literal:    SGVsbG8sIHdvcmxkIQ==
StringVar:  SGVsbG8sIHdvcmxkIQ==
JsonRef:    eyJmb28iOiJiYXIiLCJuIjo0Mn0=
Expression: <base64 of your character's name>
```

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
| **jsonref → jsonref** | `jsonvalue` holding `"<b64>"` | `jsonvalue` (destination) | Read `argv[0]`'s scalar, decode, write into `argv[1]`. `argv[0]` unchanged. |
| **string → jsonref** | `string` variable, literal, or LavishScript expression | `jsonvalue` (destination) | Decode the string value, write into `argv[1]` |

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

**Example — decode from a string variable:**

```
variable string    b64       = "eyJmb28iOiJiYXIiLCJuIjo0Mn0="
variable jsonvalue restored

ISXOgre:Base64Decode[b64, restored]
echo ${restored.AsJSON~}
```

**Output:**

```
{"foo":"bar","n":42}
```

---

### Base64Decode — Member

Decode a base64 source and return the decoded bytes as a `string`.

**Syntax:** `${ISXOgre.Base64Decode[<source>]}`

| `<source>` shape | Result |
|------------------|--------|
| String literal | Decoded text of the literal |
| `variable string` name | Decoded text of the variable's value |
| `jsonvalue` variable holding `"<b64>"` | Decoded text of the stored scalar |
| Any LavishScript expression resolving to a base64 string | Decoded text of the resolved value |

The outer JSON-string quotes on a `jsonvalue` source are stripped automatically before decoding (the base64 alphabet `[A-Za-z0-9+/=]` never contains `"`, so the strip is unambiguous).

**Example:**

```
variable string    b64       = "SGVsbG8sIHdvcmxkIQ=="
variable jsonvalue encoded
encoded:SetValue["\"eyJmb28iOiJiYXIiLCJuIjo0Mn0=\""]

echo Literal:   ${ISXOgre.Base64Decode["SGVsbG8sIHdvcmxkIQ=="]~}
echo StringVar: ${ISXOgre.Base64Decode[b64]~}
echo JsonRef:   ${ISXOgre.Base64Decode[encoded]~}
```

**Output:**

```
Literal:   Hello, world!
StringVar: Hello, world!
JsonRef:   {"foo":"bar","n":42}
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

ISXOgre:Base64Encode[original, encoded]
ISXOgre:Base64Decode[encoded,  restored]

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
