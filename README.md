<div align="center">

<img src="./assets/profile-terminal.svg" alt="Mouhamed Aziz Belghaieb terminal profile" width="850"/>

<a href="https://azizbelghaieb.netlify.app/"><img src="https://img.shields.io/badge/PORTFOLIO-181825?style=for-the-badge&logo=googlechrome&logoColor=a6e3a1" alt="portfolio"/></a>
<a href="https://linkedin.com/in/aziz-belghaieb-749044382"><img src="https://img.shields.io/badge/LINKEDIN-181825?style=for-the-badge&logo=linkedin&logoColor=89b4fa" alt="linkedin"/></a>
<a href="mailto:azizbelghaieb@proton.me"><img src="https://img.shields.io/badge/EMAIL-181825?style=for-the-badge&logo=protonmail&logoColor=f38ba8" alt="email"/></a>

</div>

<br/>

## `~ $ cat identity.txt`

```text
Mouhamed Aziz Belghaieb
role       software engineering student + full-stack developer
location   Tunisia
focus      secure systems · applied AI · embedded & connected products
mode       turning complex requirements into working software
```

Third-year software engineering student at the University of Monastir. I combine strong fundamentals in algorithms, networks and object-oriented design with end-to-end implementation across backend, frontend, AI and embedded systems.

<br/>

## `~ $ ./showcase --mode=architecture`

```mermaid
flowchart LR
    U[User or client] --> UI[Web / mobile interface]
    UI --> API[REST API]
    API --> AUTH[JWT / role security]
    API --> BL[Business logic]
    BL --> DB[(Database)]
    BL --> AI[AI / OCR / NLP]
    IOT[ESP32-S3] -->|telemetry| API

    style U fill:#181825,stroke:#89b4fa,color:#cdd6f4
    style UI fill:#181825,stroke:#cba6f7,color:#cdd6f4
    style API fill:#181825,stroke:#f9e2af,color:#cdd6f4
    style AUTH fill:#181825,stroke:#f38ba8,color:#cdd6f4
    style BL fill:#181825,stroke:#a6e3a1,color:#cdd6f4
    style DB fill:#181825,stroke:#94e2d5,color:#cdd6f4
    style AI fill:#181825,stroke:#fab387,color:#cdd6f4
    style IOT fill:#181825,stroke:#89dceb,color:#cdd6f4
```

<br/>

## `~ $ ls -l ./featured-projects`

> Three systems, three kinds of complexity: **people and healthcare**, **commerce and roles**, and **documents and AI verification**.

---

### `01/ TBIBI`

**A complete medical web platform for patients, doctors and administrative staff**

TBIBI organizes the journey between a patient and a doctor. It combines account management, appointment availability, medical documents, subscriptions, live presence and an AI assistant in one application.

```mermaid
flowchart TD
    Patient([Patient]) --> Web[Responsive web platform]
    Doctor([Doctor]) --> Web
    Assistant([Assistant / Admin]) --> Web

    Web --> Security[JWT authentication\nrole-based access]
    Security --> Services[Spring Boot services]

    Services --> Users[Accounts & profiles]
    Services --> Booking[Appointments & availability]
    Services --> Documents[Medical files & uploads]
    Services --> Payments[Subscriptions & checkout]
    Services --> Presence[Doctor presence]

    Services --> AI[AI medical assistant]
    Services --> Chat[Real-time chat]
    Services --> DB[(User and medical data)]

    AI --> Web
    Chat --> Web
```

| What is implemented | Technical proof |
|---|---|
| Authentication and role separation | JWT filter, login/register flows and protected controllers |
| Appointment workflows | Availability, booking, status and appointment services |
| Medical document handling | Secure upload endpoints and file-category entities |
| AI-assisted support | Spring AI chat client and assistant controller |
| Live communication | WebSocket configuration and chat message entities |
| Account recovery | Password-reset tokens and email service |
| Production-oriented structure | DTOs, entities, repositories, services and exception handling |

`Java` `Spring Boot` `Spring Security` `JWT` `Spring AI` `WebSocket` `REST` `JavaScript` `HTML` `CSS`

<a href="https://github.com/belghaieb/tbibi">**→ Explore the TBIBI repository**</a>

---

### `02/ ShopFlow`

**A full-stack multi-role commerce system built around real business operations**

ShopFlow is more than a storefront: the same platform serves customers, sellers and administrators. Each role receives dedicated workflows, while the backend protects operations with authentication and role-aware services.

```mermaid
flowchart TD
    Customer([Customer]) --> Store[Next.js storefront]
    Seller([Seller]) --> Store
    Admin([Administrator]) --> Store

    Store --> API[Spring Boot REST API]
    API --> Auth[JWT login\nrefresh tokens]
    API --> Catalog[Products & variants]
    API --> Cart[Cart & stock handling]
    API --> Sales[Coupons & orders]
    API --> Review[Reviews & ratings]
    API --> RoleUI[Role-specific dashboards]

    Auth --> Security[Role authorization]
    Catalog --> DB[(Commerce database)]
    Cart --> DB
    Sales --> DB
    Review --> DB
    RoleUI --> DB
```

| What is implemented | Technical proof |
|---|---|
| Customer experience | Product browsing, details, cart, checkout and account pages |
| Seller operations | Seller dashboard and product/order-oriented flows |
| Administration | Dedicated admin dashboard and user administration |
| Secure sessions | JWT authentication, refresh-token entity and authorization filter |
| Commerce rules | Stock checks, order status changes, coupons and cart services |
| Trust and feedback | Review entities, service methods and rating UI |
| Testing | Service tests for cart, order, product and review behavior |

`Next.js` `TypeScript` `Tailwind CSS` `Java` `Spring Boot` `JWT` `PostgreSQL` `Python` `REST`

<a href="https://github.com/belghaieb/ShopFlow">**→ Explore the ShopFlow repository**</a>

---

### `03/ Cement Prefacture`

**An intelligent invoice workflow that turns a photo into verified business data**

This project addresses a concrete industrial process: importing invoice photos, extracting fields with AI, comparing them with purchase orders and presenting the result to operational users.

```mermaid
flowchart TD
    Photo([Invoice photo]) --> Import[Image import]
    Import --> Preprocess[Image preprocessing]
    Preprocess --> OCR[Gemini OCR service]
    OCR --> Fields[Structured extracted fields]

    Fields --> Verify[Purchase-order verification]
    Invoice([Purchase order]) --> Verify

    Verify --> Alerts[Alerts and validation result]
    Alerts --> API[Spring Boot REST API]
    API --> Dash[Administration dashboard]
    API --> Users[Role-based user access]
    API --> DB[(Invoice and order database)]
```

| What is implemented | Technical proof |
|---|---|
| Document import | Invoice/photo endpoints and import service |
| AI extraction | Gemini OCR service and extracted-field DTO |
| Business verification | Purchase-order comparison and validation-result service |
| Validation controls | Invoice status, custom exceptions and global error handling |
| Operational interface | Dashboard, invoice, factures and administrator screens |
| User management | Authentication, role entities and protected API configuration |
| API documentation | Springdoc/OpenAPI setup |

`Java` `Spring Boot` `Gemini AI` `OCR` `Spring Security` `REST` `JavaScript` `HTML` `CSS`

<a href="https://github.com/belghaieb/cement-project">**→ Explore the Cement Prefacture repository**</a>

<br/>

## `~ $ ./stack --compact`

| DOMAIN | TECHNOLOGIES |
|---|---|
| **Languages** | Java · C++ · C# · C · Python · TypeScript · JavaScript · Prolog |
| **Backend** | Spring Boot · JPA/Hibernate · REST · JWT · WebSockets |
| **Frontend** | Next.js · React · Angular · HTML/CSS · Thymeleaf |
| **Data & AI** | PostgreSQL · NLP · TF-IDF · OCR · ETL / OLAP |
| **Systems** | Linux · Arduino · ESP32-S3 · Cisco networking |

<br/>

## `~ $ cat credentials.txt`

- **LPI Linux Essentials**
- **Linux Unhatched — Cisco Networking Academy**, November 2024

<br/>

## `~ $ git status`

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=belghaieb&show_icons=true&include_all_commits=true&count_private=true&hide_border=true&bg_color=181825&title_color=89b4fa&icon_color=a6e3a1&text_color=cdd6f4" alt="GitHub stats"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=belghaieb&layout=compact&hide_border=true&bg_color=181825&title_color=89b4fa&text_color=cdd6f4" alt="Top languages"/>

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=belghaieb&hide_border=true&background=181825&ring=89b4fa&fire=fab387&currStreakNum=cdd6f4&sideNums=cdd6f4&currStreakLabel=a6e3a1&sideLabels=cdd6f4&dates=9399b2" alt="Contribution streak"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/belghaieb/belghaieb/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/belghaieb/belghaieb/output/github-snake.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/belghaieb/belghaieb/output/github-snake.svg" width="100%">
</picture>

</div>
