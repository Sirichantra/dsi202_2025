# 🌳 PLOOKJING - Tree Planting Platform

## บทคัดย่อ (Abstract)

โครงการ "PLOOKJING" หรือชื่อเต็มว่า "ระบบปลูกต้นไม้ทางไกล" เป็นแพลตฟอร์มที่พัฒนาขึ้นเพื่อส่งเสริมการมีส่วนร่วมของประชาชนทุกกลุ่มในการปลูกต้นไม้และอนุรักษ์สิ่งแวดล้อม โดยไม่จำเป็นต้องมีพื้นที่หรือเวลาสำหรับปลูกต้นไม้ด้วยตนเอง ระบบนี้เปิดโอกาสให้ผู้ใช้งานสามารถเลือกต้นไม้ พื้นที่ปลูก แจ้งเตือนการดูแล และสามารถสั่งซื้ออุปกรณ์ปลูกต้นไม้หรือต้นไม้จริงเพื่อปลูกที่บ้านได้อย่างครบวงจร

ระบบถูกออกแบบให้ใช้งานง่าย มีความทันสมัย สวยงาม และตอบโจทย์ผู้ใช้ในยุคดิจิทัล มีการเชื่อมโยงข้อมูลกับฐานข้อมูลต้นไม้ ข้อมูลแผนที่ การสร้างคำสั่งซื้อ การแจ้งเตือนผ่านเว็บไซต์ และมีระบบแยกคำสั่งซื้อระหว่างต้นไม้และอุปกรณ์ เพื่อความเป็นระบบ

ในช่วงเวลาการพัฒนา ระบบได้ถูกออกแบบและพัฒนาแบบเต็มรูปแบบ ทั้งในส่วนของ UX/UI, ระบบ Backend, ระบบจัดการฐานข้อมูล, การเชื่อมโยงแบบ RESTful API, และมีการรันผ่าน Docker Compose ได้อย่างสมบูรณ์

---

## User Story: ปลูกต้นไม้ทางไกล

1. **เลือกต้นไม้และพื้นที่ปลูก**

   * ในฐานะ ผู้ใช้ ฉันต้องการ เลือกต้นไม้ที่ต้องการปลูกและระบุพื้นที่ที่ต้องการให้ปลูก เพื่อที่ ฉันจะสามารถปลูกต้นไม้ในพื้นที่ที่ฉันสนใจได้

2. **แจ้งเตือนการดูแลต้นไม้**

   * ในฐานะ ผู้ใช้ ฉันต้องการ รับการแจ้งเตือนเกี่ยวกับการดูแลต้นไม้ เช่น การใส่ปุ๋ย รดน้ำ และตัดแต่ง เพื่อที่ ฉันจะสามารถติดตามการเติบโตของต้นไม้ได้อย่างมีประสิทธิภาพ

3. **เลือกแผนการปลูกต้นไม้**

   * ในฐานะ ผู้ใช้ ฉันต้องการ เลือกแผนการปลูกต้นไม้ เช่น ปลูก 1 ต้น/เดือน หรือ 10 ต้น/ปี เพื่อที่ ฉันจะสามารถวางแผนปลูกต้นไม้ระยะยาวได้

4. **ซื้ออุปกรณ์ปลูกต้นไม้**

   * ในฐานะ ผู้ใช้ ฉันต้องการ ซื้ออุปกรณ์ปลูกต้นไม้และต้นไม้จริงสำหรับนำไปปลูกเอง เพื่อที่ ฉันจะสามารถปลูกต้นไม้ด้วยตนเองที่บ้านได้

---

## 📌 ฟีเจอร์หลัก (Core Features)

### 1. เลือกต้นไม้และพื้นที่ปลูก

* ผู้ใช้งานสามารถเลือกต้นไม้จากรายการที่มี พร้อมดูรายละเอียดต้นไม้ เช่น ชื่อ ราคา ภาพ และคำแนะนำ
* เมื่อคลิก "ซื้อทันที" จะเข้าสู่ขั้นตอนการเลือกสถานที่ปลูกต้นไม้ (select location)
* ผู้ใช้สามารถเลือกโครงการเพื่อปลูกต้นไม้ และระบบจะบันทึกข้อมูลคำสั่งซื้อไปยังหน้า "My Trees"

### 2. แจ้งเตือนการดูแลต้นไม้

* มีระบบ Notifications ที่ใช้สำหรับแจ้งเตือนผู้ใช้เมื่อมีอัปเดตเกี่ยวกับต้นไม้ที่ตนปลูก เช่น “ต้นไม้ของคุณปลูกสำเร็จแล้ว”
* Admin สามารถเพิ่มรายการแจ้งเตือนจากฝั่ง backend ได้

### 3. ซื้ออุปกรณ์ปลูกต้นไม้

* แยกหน้าร้านอุปกรณ์ (equipment list) ผู้ใช้สามารถกดดูรายละเอียด (equipment detail)
* สินค้ามีระบบตะกร้าสินค้าแบบ Add to Cart และ Buy Now
* ระบบสามารถรวมคำสั่งซื้อแบบหลายรายการและแยกตามประเภทสินค้า (tree/equipment)

### 4. ระบบคำสั่งซื้อและชำระเงิน

* รองรับคำสั่งซื้อแบบหลายสินค้า แสดง QR สำหรับโอนเงิน
* มีการบันทึก Slip การโอนเงิน และสถานะคำสั่งซื้อ (Pending, Verifying, Shipping, Delivered, Cancelled)
* ผู้ใช้สามารถอัปโหลดสลิปได้ในหน้า My Orders/My Trees และระบบจะแสดงรายละเอียดสินค้าในรูปแบบกล่องภาพ

### 5. ระบบผู้ใช้งานและการล็อกอิน

* ล็อกอิน / ล็อกเอาต์ แบบปกติ
* ผู้ใช้สามารถเข้าถึง Profile ของตนเอง และจัดการข้อมูลการปลูกหรือคำสั่งซื้อได้อย่างครบถ้วน

### 6. ระบบ Notifications เต็มรูปแบบ

* แสดงข้อความแจ้งเตือนสถานะการสั่งซื้อ เช่น "คำสั่งซื้อของคุณได้รับการยืนยันแล้ว"
* แสดงเตือนเมื่อมีอัปเดตต้นไม้ เช่น "ทีมงานได้ปลูกต้นไม้ของคุณแล้ว"

---

## 🧑‍💻 รายละเอียดทางเทคนิค (Technical Overview)

* ภาษาและ Framework: Django 4.x, Python 3.11, Tailwind CSS, HTML
* Docker: ใช้งานผ่าน Docker Compose ได้ทันที (`docker compose up`)
* ฐานข้อมูล: SQLite ในระหว่างพัฒนา (สามารถเปลี่ยนเป็น PostgreSQL ได้)
* API: ใช้ Django REST Framework สำหรับ endpoint ที่เกี่ยวข้องกับการดึงข้อมูลต้นไม้ อุปกรณ์ และคำสั่งซื้อ
* Template: ใช้โครงสร้าง Template สืบทอดจาก base.html โดยใช้ Tailwind เป็นหลัก
* การจัดการ Cart: session-based cart ที่สามารถแยกประเภทสินค้าและรวมยอดอัตโนมัติ

---

## 📈 ผลลัพธ์ที่ได้ (Outcomes)

* ระบบสามารถเปิดให้บุคคลทั่วไปปลูกต้นไม้ทางไกลได้อย่างสมบูรณ์จริง
* ผู้ใช้สามารถเลือกต้นไม้ พื้นที่ ดูประวัติ ดูสเตตัส และได้รับการแจ้งเตือนโดยไม่ต้องเดินทาง
* เหมาะกับโครงการด้านสิ่งแวดล้อม เช่น CSR, Carbon Offset หรือกิจกรรมในโรงเรียน
* มีระบบร้านค้าพร้อมใช้งาน และสามารถซื้ออุปกรณ์เพื่อปลูกเองที่บ้านได้
* อินเตอร์เฟซมีความสวยงาม ใช้งานง่าย เหมาะกับผู้ใช้ทุกเพศทุกวัย

---

## 🔮 แผนพัฒนาต่อไป (Future Features)

* แสดงสถิติการปลูกต้นไม้ทั่วประเทศแบบ Interactive Map
* ระบบ Level & Badge สำหรับผู้ใช้ที่ปลูกต้นไม้ครบจำนวนที่กำหนด
* ระบบแชทหรือกระดานสนทนา (Tree Community)
* ระบบประเมินผลต้นไม้ที่รอดตายและเติบโตดี พร้อมนำมาใช้คำนวณผลกระทบด้านสิ่งแวดล้อม

---

## 📝 ข้อสรุป

โครงการ **PLOOKJING - ปลูกต้นไม้ทางไกล** ไม่ได้เป็นเพียงแค่แพลตฟอร์มสำหรับการซื้อขายต้นไม้หรือจัดการคำสั่งซื้อทั่วไป แต่เป็นระบบที่ถูกออกแบบด้วยเจตนารมณ์ในการเชื่อมโยง “ความตั้งใจ” ของผู้คนเข้ากับ “พื้นที่ป่า” ที่กำลังต้องการการฟื้นฟู ด้วยความเข้าใจว่าหลายคนมีหัวใจสีเขียวแต่ไม่มีเวลาหรือทรัพยากรในการลงพื้นที่ด้วยตนเอง โครงการนี้จึงเข้ามาทำหน้าที่เป็นสะพานเชื่อมระหว่างความตั้งใจและการลงมือทำในระดับพื้นที่จริง

ด้วยการบูรณาการระหว่าง UX/UI ที่ใช้งานง่าย ระบบข้อมูลที่โปร่งใส ระบบแจ้งเตือนการดูแลต้นไม้ และระบบแผนการปลูกแบบระยะยาว ผู้ใช้งานสามารถมีส่วนร่วมกับต้นไม้ของตนเองได้ตลอดทุกช่วงอายุของการเติบโต แม้อยู่ห่างไกลหลายร้อยกิโลเมตรก็ตาม ทุกขั้นตอนของระบบตั้งแต่การเลือกต้นไม้ไปจนถึงการอัปโหลดสลิปการโอนเงิน และการติดตามผลลัพธ์ ถูกออกแบบอย่างครบวงจรเพื่อสร้างประสบการณ์การปลูกต้นไม้ที่ “เข้าถึงง่าย แต่ไม่ลดคุณค่า”

**PLOOKJING** จึงไม่ใช่แค่แพลตฟอร์มของวันนี้ แต่สามารถพัฒนาเป็นเครื่องมือด้านสิ่งแวดล้อมในระดับชาติ ไม่ว่าจะใช้ในโครงการ CSR ของภาคธุรกิจ ใช้เป็นเครื่องมือส่งเสริมการเรียนรู้ในโรงเรียน หรือเชื่อมโยงกับนโยบายรัฐด้าน Carbon Offset และ Net Zero ได้อย่างมีประสิทธิภาพในอนาคต

> “การปลูกต้นไม้ไม่ใช่แค่การลงดิน แต่คือการหว่านความหวังให้กับอนาคตของโลก” 🌏
> **PLOOKJING คือเครื่องมือนั้น คือสะพานนั้น และคือน้ำใจที่เบ่งบานเป็นสีเขียวในทุกพื้นที่ของประเทศ**

**VDO การใช้ PlookJing** https://drive.google.com/file/d/1OFhryS4FIsU9nF4GUb20f_tu6oY3y0KZ/view?usp=sharing
