<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=240&color=0:2563eb,100:0f172a&text=CipherForge&fontColor=ffffff&fontSize=60&fontAlignY=40&desc=Professional%20Encryption%20Tool%20%7C%20CODE%20RAH&descAlignY=63&animation=twinkling" width="100%" />

# 🔐 ابزار حرفه‌ای رمزگذاری و هشینگ

### توسعه داده شده توسط تیم تخصصی CODE RAH 💻

</div>

---

# 🛑 بیانیه کپی‌رایت و مالکیت معنوی (مهم)

> ⚠️ **تذکر جدی برای همکاران و اساتید:**  
> این کد برای اولین بار در سطح اینترنت منتشر می‌شود و توسط **امیرفرخانی موسس آکادمی آنلاین کدراه** پیاده‌سازی و کدنویسی شده است.  
> هرگونه استفاده، برداشته شدن سورس‌کد، تولید محتوای ویدیویی مشابه در سطح وب و آموزش آن **منحصراً مشروط به ذکر منبع و نام CODE RAH** است.  
> در غیر این صورت هیچ‌گونه رضایتی وجود نداشته و عواقب آن متوجه فرد خاطی خواهد بود.

---

# 📝 درباره پروژه

**CipherForge** یک ابزار رمزگذاری دسکتاپ با رابط گرافیکی مدرن است که با Python و CustomTkinter ساخته شده.

این برنامه سه حالت مختلف رمزگذاری را پشتیبانی می‌کند:

1. **Hash Code**  
   تولید خروجی یک‌طرفه با الگوریتم SHA-256 برای بررسی یکپارچگی داده.

2. **Crypto Code**  
   رمزگذاری متقارن با الگوریتم Fernet (بر پایه AES-128) که قابل رمزگشایی است.

3. **Tarkiby Code**  
   ترکیب هوشمند هر دو روش — خروجی شامل Hash و رمز رمزگذاری‌شده با جداکننده `::` می‌باشد.

---

# ⚡ ویژگی‌های فنی و معماری کد

- **رابط گرافیکی مدرن (CustomTkinter)**  
  طراحی تمیز و حرفه‌ای با پشتیبانی از تم تاریک و روشن.

- **رمزگذاری چندلایه (Tarkiby Mode)**  
  ترکیب SHA-256 و Fernet در یک خروجی واحد با جداکننده `::` برای امنیت بیشتر.

- **مدیریت هوشمند خطا**  
  بررسی وضعیت چک‌باکس‌ها و نمایش پیام‌های راهنمای دقیق به کاربر.

- **سازگاری کامل با Python 3.10+**  
  استفاده از `hashlib` و کتابخانه `cryptography` برای پیاده‌سازی استاندارد.

---

# 🚀 راهنمای دانلود، نصب و راه‌اندازی

## 📥 مرحله اول: دانلود پروژه از گیت‌هاب

### روش اول — دانلود کل پروژه

روی دکمه سبز رنگ **Code** کلیک کرده و گزینه **Download ZIP** را انتخاب کنید، سپس فایل را از حالت فشرده خارج نمایید.

### روش دوم — دانلود مستقیم فایل

روی فایل پایتون کلیک کرده و گزینه **Download raw file** را بزنید.

---

## 🧩 مرحله دوم: نصب پایتون

اگر Python روی سیستم ندارید:

1. وارد سایت رسمی Python شوید و آخرین نسخه را دانلود کنید.
2. هنگام نصب حتماً گزینه زیر را فعال نمایید:

Add Python to PATH

---

## 📦 مرحله سوم: نصب پکیج‌ها

وارد پوشه پروژه شوید، کلید `Shift` را نگه دارید، راست کلیک کرده و **Open PowerShell here** را انتخاب نمایید.

سپس دستور زیر را اجرا کنید:

bash
pip install customtkinter cryptography pillow

---

## ▶️ مرحله چهارم: اجرای برنامه

bash
python main.py

> ⚠️ فایل‌های `hacker.ico` و تصویر پس‌زمینه باید دقیقاً کنار فایل پایتون قرار داشته باشند.

---

## 📂 ساختار پوشه پروژه


CipherForge/
├── main.py
├── hacker.ico
└── background.jpg

---

# 🧪 نمونه خروجی

| حالت | ورودی | خروجی |
|------|-------|--------|
| Hash Code | `hello` | `2cf24dba5fb0a30e...` |
| Crypto Code | `hello` | `gAAAAAB...` |
| Tarkiby Code | `hello` | `2cf24dba...::gAAAAAB...` |

---

# 🧠 درباره تیم CODE RAH

تیم **CODE RAH** یک گروه تخصصی در حوزه‌های پیشرفته فناوری است که در زمینه‌های زیر فعالیت گسترده دارد:

- 💻 برنامه‌نویسی و توسعه وب/بک‌اند  
  `C#` `Java` `Python` `JavaScript`

- 🔒 امنیت سایبری و تست نفوذ  
  `Ethical Hacking` `Kali Linux`

- 🤖 هوش مصنوعی و بینایی ماشین  
  `Machine Learning` `YOLO` `OpenCV`

- ⚙️ سیستم‌های سخت‌افزاری و اینترنت اشیاء  
  `Arduino` `Raspberry Pi`

---

# 🎓 کلاس‌ها و دوره‌های آموزشی

ما در **CODE RAH** دوره‌های تخصصی و کلاس‌های آموزشی هوشمندی را برای علاقه‌مندان به ورود به دنیای حرفه‌ای برنامه‌نویسی، رمزنگاری، هوش مصنوعی و امنیت سایبری برگزار می‌کنیم.

اگر به توسعه پروژه‌های این‌چنینی علاقه دارید، کدهای ما مسیر آینده را به شما نشان می‌دهند.

---

# ⚡ مهارت‌ها و فناوری‌ها

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-7B2FBE?style=for-the-badge)
![Cryptography](https://img.shields.io/badge/Cryptography-Fernet-1a1a2e?style=for-the-badge)
![Hashlib](https://img.shields.io/badge/SHA--256-HashLib-6a0dad?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Tool-dc143c?style=for-the-badge)

</div>

---

# 🌐 ارتباط با ما

برای شرکت در دوره‌های آموزشی، دریافت مشاوره‌های فنی و دنبال کردن پروژه‌های جدید، ما را در شبکه‌های اجتماعی دنبال کنید.

---

<div align="center">

# 💻 CODE RAH

### کدنویسی فقط نوشتن برنامه نیست؛ ساختن آینده است.

⭐ اگر از این پروژه خوشتان آمد، فراموش نکنید به پروژه ستاره بدهید ⭐

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0f172a,100:2563eb&section=footer" width="100%" />
`
