# บทคัดย่อ: ระบบปลูกต้นไม้ทางไกลด้วย Docker และ Django

ระบบปลูกต้นไม้ทางไกล (*Remote Tree Planting System*) เป็นโครงการที่ผสานความเข้าใจผู้ใช้งานเข้ากับเทคโนโลยีเพื่อสร้างแพลตฟอร์มที่ตอบโจทย์ทั้งสิ่งแวดล้อมและประสบการณ์ผู้ใช้อย่างครบวงจร โดยใช้ **Django** สำหรับพัฒนา backend และ **Docker** สำหรับจัดการ environment และ deployment อย่างมีประสิทธิภาพ

---

## 1. แนวคิดหลักของระบบ

Epic: **ปลูกต้นไม้ทางไกล** แยกออกเป็น 4 User Stories หลัก:

- ✅ **เลือกต้นไม้และพื้นที่ปลูก**  
  > ผู้ใช้สามารถเลือกชนิดต้นไม้และพื้นที่ปลูกได้อย่างอิสระ

- ✅ **ระบบแจ้งเตือนการดูแลต้นไม้**  
  > แจ้งเตือนเรื่องรดน้ำ ใส่ปุ๋ย ตัดแต่ง ผ่าน notification

- ✅ **เลือกแผนการปลูกระยะยาว**  
  > เลือกแพ็กเกจปลูก 1 ต้น/เดือน หรือ 10 ต้น/ปี

- ✅ **ซื้ออุปกรณ์และต้นไม้สำหรับปลูกที่บ้าน**  
  > ระบบขายต้นไม้และอุปกรณ์ผ่าน e-commerce flow

---

## 2. UX/UI และเอกลักษณ์แบรนด์

อิงตามกระบวนการ **Design Thinking**:

- เริ่มจากการสัมภาษณ์ (Empathise) → กำหนดปัญหา (Define) → ร่างไอเดีย (Ideate)
- สร้างต้นแบบ (Prototype) บน Figma และทำ usability test
- สร้าง **User Persona**, **POV Statements**, และ **User Stories** พร้อม Acceptance Criteria
- ใช้หลัก **Visual Identity**:
  - 🎨 โทนสี 60-30-10 (สีหลัก/รอง/เน้น)
  - 🔤 Modular scale ใน typography
  - ♿ Contrast Ratio ≥ 4.5:1
  - 🎯 Tailwind Design Tokens

---

## 3. พัฒนาโดยใช้ Django + Docker

ระบบถูกพัฒนาด้วย **Django + PostgreSQL + Redis** และจัดการผ่าน **Docker**:

- ใช้ Docker Compose สำหรับ dev/prod environments
- ทำ CI/CD ด้วย GitHub Actions
- ใช้ `django-extensions` และ `shell_plus` สำหรับ bulk operations เช่น สร้าง QR
- รองรับ static file, media, และ database volume mapping

---

## 4. การชำระเงินด้วย QR (PromptPay)

ระบบสร้าง QR Code แบบ **EMVCo-compliant**:

- ฝัง `payment_ref` (UUID) ใน tag `62`
- รองรับ webhook หรือ manual upload จากธนาคาร
- เมื่อชำระสำเร็จ → อัปเดต `is_paid=True` → ปลดล็อกสิทธิ์ให้ผู้ใช้

---

## 5. คุณค่าของโครงการ

- ผสาน **Design Thinking + Full-stack Engineering**
- ใช้แนวคิด **Atomic Design + Accessibility** ครบถ้วน
- ใช้ได้จริงกับ kiosk, POS, หรือระบบปลูกต้นไม้เชิงสังคม
- วางรากฐานการพัฒนาอย่างมีแบบแผน ใช้เครื่องมือ dev-friendly และทีมสามารถขยายต่อได้ง่าย

---

> โครงการนี้แสดงให้เห็นถึงแนวคิด *“ออกแบบจากผู้ใช้ → พัฒนาระบบด้วยเทคโนโลยี → สร้างผลกระทบในชีวิตจริง”* ได้อย่างลงตัว
