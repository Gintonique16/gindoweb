Dạ vâng Ngài Gin, sau đây là phần trình bày **hoàn chỉnh, cập nhật đầy đủ thuộc tính HTML5** cho thẻ `<html>` theo đúng yêu cầu học để master.

---

## 🔖 **Thẻ `<html>`**

---

### 1. **Ý nghĩa / Viết tắt**

- Không phải viết tắt.
- Là **gốc rễ (root element)** của toàn bộ tài liệu HTML – chứa mọi thứ bên trong trang web.

---

### 2. **Công dụng chính**

- Xác định phạm vi của **tài liệu HTML**.
- Là **cha của mọi phần tử khác**, bao gồm cả `<head>` và `<body>`.
- Cho phép trình duyệt hiểu đây là một **tài liệu HTML hợp lệ**.
- Có thể khai báo **ngôn ngữ**, **hướng văn bản**, và không gian tên (với XML/XHTML).

---

### 3. **Thẻ tương tự / Có thể thay thế**

- Không có thẻ thay thế nào hợp lệ. Bắt buộc 1 thẻ `<html>` duy nhất cho mỗi trang.

---

### 4. **Thường đi kèm với**

- `<!DOCTYPE html>` ở dòng đầu tiên
- `<head>` và `<body>` nằm bên trong
- `<html>` là phần tử ngoài cùng

---

### 5. **Toàn bộ các attribute HTML5 có thể dùng với `<html>`**

#### 🧩 A. **Global attributes** (thuộc tính toàn cục – áp dụng cho mọi thẻ HTML):

- `accesskey`
- `autocapitalize`
- `class`
- `contenteditable`
- `dir`
- `draggable`
- `enterkeyhint`
- `exportparts`
- `hidden`
- `id`
- `inert`
- `inputmode`
- `is` (dành cho custom elements)
- `itemid`
- `itemprop`
- `itemref`
- `itemscope`
- `itemtype`
- `lang`
- `nonce`
- `part`
- `popover`
- `slot`
- `spellcheck`
- `style`
- `tabindex`
- `title`
- `translate`

#### 🧩 B. **Thuộc tính đặc trưng riêng cho `<html>`**

| Thuộc tính | Ý nghĩa                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| `lang`     | Ngôn ngữ chính của tài liệu (ví dụ: `lang="vi"`) ✅ Rất quan trọng                                    |
| `dir`      | Hướng văn bản: `ltr` (trái sang phải – mặc định), `rtl` (phải sang trái – dùng cho Ả Rập, Do Thái...) |
| `xmlns`    | Không gian tên – chỉ dùng khi viết XHTML, không cần trong HTML5                                       |

#### 🧩 C. **Event attributes (ít dùng trên `<html>`, nhưng hợp lệ)**

- `onload`
- `onerror`
- `onbeforeunload`
- `onunload`

⛔️ Nhưng **tránh gán event trực tiếp vào thẻ `<html>`**, nên để cho JS xử lý ở `<body>` hoặc qua `addEventListener`.

---

### 6. **Ví dụ thực tế**

```html
<!DOCTYPE html>
<html lang="vi" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <title>Trang của Ngài Gin</title>
  </head>
  <body>
    <h1>Chào Ngài!</h1>
  </body>
</html>
```

---

### 7. **Độ phổ biến / Thông dụng**

- ⭐️⭐️⭐️⭐️⭐️ (100%)
- Bắt buộc trong mọi tài liệu HTML hợp lệ

---

### 8. **Ảnh hưởng đến hiệu suất**

- Không ảnh hưởng hiệu suất trực tiếp
- Nhưng nếu **thiếu hoặc sai** → toàn bộ tài liệu sẽ bị trình duyệt **hiểu sai hoặc lỗi cú pháp**

---

### 9. **Khả năng bảo trì**

- Rất cao – vì hiếm khi cần chỉnh sửa
- Một số framework (Next.js, Nuxt, Astro...) sẽ thay thế bằng cách **custom document layout**, nhưng vẫn dựa trên `<html>`

---

### 10. **Khả năng mở rộng / phát triển**

- Là gốc rễ → mọi công nghệ web hiện đại (PWA, Web Component, SEO, SSR...) đều xây dựng từ đây

---

### 11. **Lưu ý nâng cao / Trick hay**

- `lang="..."`: rất quan trọng cho **SEO**, **screen reader** và **dịch tự động** (Google Translate)
- `dir="rtl"` giúp hỗ trợ ngôn ngữ từ phải qua trái
- `xmlns` chỉ nên dùng nếu đang làm XML/XHTML (ví dụ khi kết hợp SVG inline)

---

Nếu Ngài Gin cần em liệt kê toàn bộ các **Global Attributes** hoặc muốn so sánh các trình duyệt xử lý `<html>` ra sao thì cứ ra lệnh ạ.
Ngài muốn tiếp tục với thẻ nào nữa không ạ? `<head>`, `<body>`, hay bất kỳ thẻ nào khác cũng được ạ.

---

Dạ vâng Ngài Gin! Từ giờ khi em liệt kê các **attribute HTML5 có thể dùng với một thẻ**, em sẽ **giải thích tác dụng cụ thể của từng thuộc tính** — kể cả thuộc tính toàn cục (global), riêng biệt, và sự kiện (event attributes).

Vậy để em làm lại phần **thuộc tính đầy đủ cho thẻ `<html>`**, lần này **có giải thích chi tiết từng attribute**.

---

## 🧩 Toàn bộ các attribute hợp lệ trong HTML5 dành cho `<html>`

---

### 🔸 A. **Thuộc tính đặc trưng của thẻ `<html>`**

| Thuộc tính | Giải thích                                                                                                                                   |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `lang`     | Xác định ngôn ngữ chính của tài liệu (ví dụ: `"vi"` cho tiếng Việt, `"en"` cho tiếng Anh). Tác động tới SEO, screen reader, dịch tự động.    |
| `dir`      | Xác định chiều của văn bản: `ltr` (left-to-right) – trái sang phải; `rtl` (right-to-left) – phải sang trái (dành cho tiếng Ả Rập, Do Thái…). |
| `xmlns`    | Xác định "namespace" XML, chỉ dùng khi tài liệu là **XHTML** (XML + HTML). Không dùng trong HTML5 chuẩn.                                     |

---

### 🔸 B. **Global attributes (thuộc tính dùng được cho tất cả các thẻ)**

| Thuộc tính                                               | Giải thích                                                                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `accesskey`                                              | Gán phím tắt để truy cập nhanh phần tử (ít dùng với `<html>`, dùng cho `<button>`, `<a>` thì hợp lý hơn).          |
| `autocapitalize`                                         | Tự động viết hoa khi nhập liệu: `on`, `off`, `words`, `sentences`, `characters`. Hiệu lực chủ yếu trên form/input. |
| `class`                                                  | Gán tên lớp CSS để định kiểu hoặc xử lý bằng JavaScript.                                                           |
| `contenteditable`                                        | Cho phép chỉnh sửa nội dung trực tiếp trên trang (giá trị: `true` hoặc `false`).                                   |
| `dir`                                                    | (đã nói ở trên) – xác định chiều hiển thị văn bản.                                                                 |
| `draggable`                                              | Cho phép kéo thả phần tử (giá trị: `true`, `false`, `auto`).                                                       |
| `enterkeyhint`                                           | Gợi ý nhãn cho phím Enter trên bàn phím ảo (ví dụ: `"search"`, `"send"`...). Hữu ích trên thiết bị di động.        |
| `exportparts`                                            | Dùng để chia sẻ Shadow DOM parts ra ngoài component (ít dùng, liên quan Web Components).                           |
| `hidden`                                                 | Ẩn phần tử khỏi giao diện và accessibility. Không hiển thị nhưng vẫn tồn tại trong DOM.                            |
| `id`                                                     | Định danh duy nhất cho phần tử trong toàn bộ DOM. Quan trọng cho JS và CSS selector.                               |
| `inert`                                                  | Ngăn tương tác người dùng và truy cập focus (đang được chuẩn hóa – tốt cho modal/overlay).                         |
| `inputmode`                                              | Gợi ý loại bàn phím hiển thị: `"decimal"`, `"numeric"`, `"tel"`, `"email"`... (chủ yếu dùng trong input).          |
| `is`                                                     | Chỉ dùng khi mở rộng custom elements trong Web Components (`<button is="x-fancy-button">`).                        |
| `itemid`, `itemprop`, `itemref`, `itemscope`, `itemtype` | Các thuộc tính của **Microdata** – dùng để đánh dấu dữ liệu có cấu trúc (SEO nâng cao).                            |
| `lang`                                                   | (đã giải thích ở trên) – khai báo ngôn ngữ tài liệu.                                                               |
| `nonce`                                                  | Token dùng cho CSP (Content Security Policy) – giúp chống XSS (tấn công chèn mã độc).                              |
| `part`                                                   | Expose nội dung trong Shadow DOM để styling từ bên ngoài.                                                          |
| `popover`                                                | Thuộc tính mới giúp hiển thị popup theo chuẩn HTML5 (cần bật tính năng ở Chrome hiện tại).                         |
| `slot`                                                   | Dùng trong Web Components để gắn nội dung vào các vị trí (slots).                                                  |
| `spellcheck`                                             | Bật/tắt kiểm tra chính tả: `true` hoặc `false`.                                                                    |
| `style`                                                  | Gắn trực tiếp CSS inline. Tránh lạm dụng vì làm rối layout.                                                        |
| `tabindex`                                               | Xác định thứ tự tab khi di chuyển bằng phím Tab. Dùng `-1` để không focus được, `0` là theo thứ tự tự nhiên.       |
| `title`                                                  | Tooltip hiển thị khi hover chuột vào phần tử.                                                                      |
| `translate`                                              | Xác định nội dung có nên được dịch hay không: `"yes"` hoặc `"no"` (dành cho trình duyệt hỗ trợ dịch).              |

---

### 🔸 C. **Event attributes (có thể dùng nhưng nên tránh gán trực tiếp)**

| Thuộc tính       | Giải thích                                                                      |
| ---------------- | ------------------------------------------------------------------------------- |
| `onload`         | Gọi hàm JavaScript khi trang/tài nguyên tải xong.                               |
| `onerror`        | Gọi hàm khi có lỗi xảy ra (ví dụ: lỗi tải script, hình ảnh…).                   |
| `onbeforeunload` | Gọi hàm khi người dùng sắp rời khỏi trang. Dùng để hiển thị cảnh báo rời trang. |
| `onunload`       | Gọi hàm khi trang bắt đầu rời đi. (Cũ, không nên dùng).                         |

---

Nếu Ngài Gin muốn, em có thể xuất riêng một **bảng tổng hợp full tất cả Global Attributes** (và cả Event Attributes) để dùng cho các thẻ khác về sau, như tài liệu học chuyên sâu luôn ạ.

Ngài muốn em tiếp tục với thẻ nào kế tiếp ạ? `<head>`, `<body>`, hay đi vào các thẻ nội dung như `<section>`, `<main>`, `<article>`...?
