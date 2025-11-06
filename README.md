# Projekt-2
# ♻️ Projekt 1: MatsvinnSparningen – Smart Food Waste Dashboard ♻️

## ✅ Beskrivning
**MatsvinnSparningen** är ett smart system som övervakar och analyserar skolmatsalens matförbrukning för att minska matsvinn.  
Systemet registrerar:
- Antalet elever som äter i matsalen varje dag  
- Mängden mat som slängs  
- Dagens maträtt  
- Datum  

Dessa data sparas i en databas och analyseras av en AI-modell som:
1. Beräknar antalet portioner och matsvinn per elev (MPE)  
2. Förutspår hur mycket mat som behövs nästa dag  
3. Ger rekommendationer till skolan och matleverantören för att optimera beställningar  

---

## ✅ Syfte
Att skapa ett system som hjälper skolor och matleverantörer att:
- Beställa rätt mängd mat  
- Minska matsvinn  
- Bidra till ett mer hållbart samhälle  

---

## ✅ Arbetsgång / Så går eleverna till väga

### 1. Planering
- Rita strukturdiagram för:
  - AI-träning  
  - Räkning av elever  
  - Frontend och backend  
- Bestäm hur data ska samlas in och bearbetas  

### 2. Datainsamling
- Använd **viktsensorer** under tallrikarna eller **kameror** ovanför för att mäta mängden mat som slängs  
- Alternativt: använd befintliga dataset över matsvinn  

### 3. AI-träning
- Träna en modell i **TensorFlow** eller **Teachable Machine** för att känna igen och analysera matmängder  

### 4. Analys
- Beräkna:
  - Matsvinn per elev (MPE)  
  - Antalet elever som ätit respektive inte ätit  

### 5. Implementation
- Kör modellen på en **Raspberry Pi** eller dator med **Python**  
- Bygg ett **dashboard-gränssnitt** för att visualisera data och insikter  

### 6. Pitch / Redovisning
- Demonstrera systemet live  
- Visa resultat av minskat matsvinn och förbättrad matplanering  

---

## 🎯 Globala mål
Projektet stödjer FN:s globala mål:  
- **Mål 12:** Hållbar konsumtion och produktion  
- **Mål 13:** Bekämpa klimatförändringarna  

---

## 💡 Tekniker & Verktyg
- **Python**  
- **TensorFlow / Teachable Machine**  
- **Raspberry Pi**  
- **Databashantering (t.ex. SQLite / Firebase)**  
- **Frontend:** Python 

---

## 🧠 Framtida utveckling
- Automatiserad rapportering till skolledning  
- Realtidsuppdatering i dashboarden  
- Koppling till leverantörers beställningssystem  

---

© 2025 MatsvinnSparningen – Ett steg mot en hållbar framtid 🌍


```mermaid
flowchart TD
    Main["Dashboard"] --> Frontend["Frontend<br>Python GUI"] & Backend["Backend<br>Python"]
    Frontend --> Dashboard["Dashboard"]
    Dashboard --> DropdownMenu["DropdownMenu"]
    DropdownMenu --> Dropdown1["Dropdown att välja Datum"] & Dropdown2["Dropdown För att kolla senste veckan, månaden, År"]
    Dropdown1 --> data2["data: <br>Datum<br>Matsvinn(KG)<br>Antal Elever som ätit mat<br>Maträtt<br>"]
    Dropdown2 --> data3["Matsvinn/ Per Elev ( MPE)<br>Start Datum<br>Slut Datum"]
   
    Backend --> databas["MongoDB"] & AI["AI som läser av elever<br>(Kamera vid ingång och utgång/över talrikar)"]
    databas --> data1["data<br>Datum<br>Matsvinn/KG)<br>Antal Elever<br>Maträtt"]
    AI --> Function["Function<br>Räknar totala Elever"]
    Function --> data1
    data1-->Backend
    Backend-->Frontend
