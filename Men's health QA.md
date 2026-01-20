### **1\. Medicine Reminder**

- **Where will the medication schedule data originate?** (e.g., manually entered by staff, integrated from an EMR system, or entered by the patient?) Pull from the EHR, Tebra (https://helpme.tebra.com/Tebra\_PM/12\_API\_and\_Integration/01\_Get\_Started\_with\_Tebra\_API\_Integration)
- **Will the app need to track adherence?** (i.e., allow the patient to mark a dose as "taken") No

### **2\. Appointment Reminder**

- **Does the app need to handle appointment booking/rescheduling,** or just notifications for existing appointments? No appointment scheduling.
- **What reminder channels are required?** (e.g., in-app notification, SMS, email, or all three?)

### **3\. Graphs, Diagrams, and Lab Results**

- **What is the source system for the lab results?** How will this data be securely transmitted to the mobile app? (EHR, highlight the ranges)

### **4\. Retail Purchases**

- **What kinds of items will be sold?** (e.g., physical goods, over-the-counter medication, or services? taxable and non-taxable items, Supplements, and relevant medication supplies) Currently use Shopify, but only because of Stripe integration.
- Subscriptions
- **Does the app need to manage inventory and fulfillment,** or will it integrate with an existing e-commerce platform?

### **5\. Staff Functionality**

- **Will the staff primarily use the mobile app for managing patient records, or will a more robust desktop/web application be required for administrative and clinical work** (e.g., viewing multiple patient records side-by-side, heavy data entry)? It is often impractical to manage a full clinical workflow solely on a mobile app.
- Missing functionality from our point of view:  
  (PMS)

| Critical Feature                        | Description & Why It's Needed                                                                                                                                               |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Appointment Scheduling & Management** | The central digital calendar for all providers. Must handle availability, block-out times, recurring appointments, waiting lists, and sending out reminders automatically.  |
| **Patient Registration & Intake**       | A system for staff to quickly and accurately enter new patient data (demographics, insurance, emergency contacts) and manage all mandatory consent forms digitally.         |
| **Billing & Invoicing**                 | A core module to generate invoices, track services provided, manage patient payment history, and calculate co-pays. Without this, the practice cannot function financially. |
| **Insurance Claims Management**         | The ability to prepare, submit, and track insurance claims (e.g., using standard medical codes like ICD-10 or CPT). This is a massive time-saver compared to paper.         |
| **Facility/Resource Management**        | If applicable, managing rooms, equipment, or other critical resources to ensure staff don't double-book a limited asset.                                                    |

(EMR)

| Critical Feature                          | Description & Why It's Needed                                                                                                                                                                         |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comprehensive Clinical Charting**       | A robust system for staff (doctors, nurses) to record clinical notes (SOAP, progress notes), enter vitals, and track treatments. Mobile-only input is often insufficient for detailed clinical notes. |
| **Medication Management & e-Prescribing** | The ability to digitally prescribe medications, manage refill requests, and perform **drug interaction checks** against the patient's allergy and medication list to enhance patient safety.          |
| **Diagnostics & Procedure Coding**        | Tools for staff to accurately select and record **standardized medical codes** (e.g., ICD-10 for diagnoses, CPT for procedures). This is essential for billing and legal records.                     |
