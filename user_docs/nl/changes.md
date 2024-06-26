# Wat is Nieuw in NVDA


## 2022.4

Deze release bevat verschillende nieuwe toetscommando's, waaronder Alles lezen commando's voor tabellen.
Er is een sectie "Snelstartgids" toegevoegd aan de gebruikershandleiding.
Er zijn ook verschillende bugfixes.

eSpeak is bijgewerkt en LibLouis is bijgewerkt.
Er zijn nieuwe Chinese, Zweedse, Luganda en Kinyarwanda brailletabellen.

### Nieuwe functies

* Een sectie "Snelstartgids" toegevoegd aan de gebruikershandleiding. (#13934)
* Een nieuwe opdracht toegevoegd om de sneltoets van de huidige focus te controleren. (#13960)
  * Desktop: `shift+numpad2`.
  * Laptop: `NVDA+ctrl+shift+.`.
* Nieuwe commando's toegevoegd om de leescursor per pagina te verplaatsen, waar ondersteund door de applicatie. (#14021)
  * Ga naar de vorige pagina:
    * Desktop: `NVDA+pageUp`.
    * Laptop: `NVDA+shift+pageUp`.
  * Ga naar de volgende pagina:
    * Desktop: `NVDA+pageDown`.
    * Laptop: `NVDA+shift+pageDown`.
* De volgende tabelopdrachten toegevoegd. (#14070)
  * Alles lezen in kolom: `NVDA+control+alt+pijl omlaag`
  * Alles lezen in rij: `NVDA+control+alt+rightArrow`
  * Lees hele kolom: `NVDA+control+alt+pijl omhoog`
  * Lees hele rij: `NVDA+control+alt+linkerpijl`
* Microsoft Excel via UI-automatisering: NVDA Meldt nu  het verlaten van een tabel binnen een spreadsheet. (#14165)
* Het melden van tabelkoppen kan nu afzonderlijk worden geconfigureerd voor rijen en kolommen. (#14075)

### Veranderingen

* eSpeak NG is bijgewerkt naar 1.52-dev commit `735ecdb8`. (#14060, #14079, #14118, #14203)
  * Rapportage van Latijnse karakters bij gebruik van Mandarijn opgelost. (#12952, #13572, #14197)
* LibLouis braillevertaler Bijgewerkt naar [3.23.0](https://github.com/liblouis/liblouis/releases/tag/v3.23.0). (#14112)
  * Brailletabellen toegevoegd:
    * Chinese gewone braille (vereenvoudigde Chinese karakters)
    * Kinyarwanda literaire braille
    * Luganda literaire braille
    * Zweeds niet-samengetrokken braille
    * Zweeds gedeeltelijk samengetrokken braille
    * Zweeds contract braille
    * Chinees (China, Mandarijn) huidig braillesysteem (geen tonen) (#14138)
* NVDA neemt nu de architectuur van het besturingssysteem mee bij het bijhouden van gebruikersstatistieken. (#14019)

### Opgeloste problemen

* Bij het updaten van NVDA met behulp van de Windows Package Manager CLI (ook wel winget genoemd), wordt een uitgebrachte versie van NVDA niet langer altijd als nieuwer behandeld dan de geïnstalleerde alfaversie. (#12469)
* NVDA kondigt nu correct Groepsboxen aan in Java-toepassingen. (#13962)
* De cursor volgt de gesproken tekst correct tijdens "alles lezen in toepassingen zoals Bookworm, WordPad of de NVDA-logviewer. (#13420, #9179)
* In programma's die UI-automatisering gebruiken, worden gedeeltelijk aangevinkte selectievakjes correct gerapporteerd. (#13975)
* Verbeterde prestaties en stabiliteit in Microsoft Visual Studio, Windows Terminal en andere op UI Automation gebaseerde applicaties. (#11077, #11209)
  * Deze fixes zijn van toepassing op Windows 11 Sun Valley 2 (versie 22H2) en hoger.
  * Selectieve registratie voor UI Automation-gebeurtenissen en eigenschapswijzigingen nu standaard ingeschakeld.
* Tekstrapportage, braille-uitvoer en wachtwoordonderdrukking werken nu zoals verwacht in het ingebouwde Windows Terminal-besturingselement in Visual Studio 2022. (#14194)
* NVDA is nu DPI-bewust bij gebruik van meerdere monitoren.
Er zijn verschillende oplossingen voor het gebruik van een DPI-instelling hoger dan 100% of meerdere monitoren.
Er kunnen nog steeds problemen optreden met versies van Windows ouder dan Windows 10 1809.
Om deze fixes te laten werken, moeten applicaties waarmee NVDA communiceert ook DPI-bewust zijn.
Let op: er zijn nog steeds bekende problemen met Chrome en Edge. (#13254)
  * Visuele markeringskaders moeten nu in de meeste toepassingen correct worden geplaatst. (#13370, #3875, #12070)
  * Interactie met het aanraakscherm zou nu nauwkeurig moeten zijn voor de meeste toepassingen. (#7083)
  * Muis volgen zou nu voor de meeste applicaties moeten werken. (#6722)
* Veranderingen in de oriëntatiestatus (liggend/portret) worden nu correct genegeerd als er geen verandering is (bijv. monitorveranderingen). (#14035)
* NVDA kondigt het slepen van items op het scherm aan op plaatsen zoals het herschikken van Windows 10 Start-menutegels en virtuele desktops in Windows 11. (#12271, #14081)
* In geavanceerde instellingen wordt de optie "Speel een geluid af voor gelogde fouten" nu correct hersteld naar de standaardwaarde wanneer op de knop "Standaardinstellingen herstellen" wordt gedrukt. (#14149)
* NVDA kan nu tekst selecteren met behulp van de sneltoets `NVDA+f10` in Java-toepassingen. (#14163)
* NVDA blijft niet langer vastzitten in een menu bij het omhoog en omlaag bewegen van conversaties in Microsoft Teams. (#14355)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2021.3.1

### Veranderingen

* Het nieuwe HID Braille-protocol heeft niet langer de voorkeur wanneer een ander brailleleesregelstuurprogramma kan worden gebruikt. (#13153)
* Het nieuwe HID Braille-protocol kan worden uitgeschakeld via een instelling in het paneel met geavanceerde instellingen. (#13180)

### Opgeloste problemen

* Oriëntatiepunt wordt weer afgekort in braille. (#13158)
* Instabiele automatische detectie van brailleleesregels voor Humanware Brailliant en APH Mantis Q40 brailleleesregels bij gebruik van Bluetooth opgelost. (#13153)

## 2021.3

Deze release introduceert ondersteuning voor de nieuwe HID Braille-specificatie.
Deze specificatie is bedoeld om de ondersteuning voor brailleleesregels te standaardiseren zonder dat er afzonderlijke stuurprogramma's nodig zijn.
Er zijn updates voor eSpeak-NG en LibLouis, inclusief nieuwe Russische en Tshivenda-tabellen.
Geluiden bij fouten kunnen worden ingeschakeld in stabiele versies van NVDA via een nieuwe optie in geavanceerde instellingen.
Alles lezen in Word schuift nu door de weergave om de huidige positie zichtbaar te houden.
Er zijn veel verbeteringen bij het gebruik van Office met UIA.
Een UIA-oplossing is dat Outlook nu meer soorten lay-outtabellen in berichten negeert.

Belangrijke opmerkingen:

Door een update van ons beveiligingscertificaat krijgt een klein aantal gebruikers een foutmelding wanneer NVDA 2021.2 op updates controleert.
NVDA vraagt ​​Windows nu om beveiligingscertificaten bij te werken, waardoor deze fout in de toekomst wordt voorkomen.
Getroffen gebruikers moeten deze update handmatig downloaden.

### Nieuwe functies

* Voegt een invoergebaar toe voor het schakelen tussen instellingen voor het rapporteren van de stijl van celranden. (#10408)
* Ondersteuning voor de nieuwe HID Braille-specificatie die tot doel heeft de ondersteuning voor brailleleesregels te standaardiseren. (#12523)
  * Apparaten die deze specificatie ondersteunen, worden automatisch gedetecteerd door NVDA.
  * Voor technische details over de implementatie van deze specificatie door NVDA, zie https://github.com/nvaccess/nvda/blob/master/devDocs/hidBrailleTechnicalNotes.md
* Ondersteuning toegevoegd voor het VisioBraille Vario 4 brailleapparaat. (#12607)
* Foutmeldingen kunnen worden ingeschakeld (geavanceerde instellingen) bij gebruik van elke versie van NVDA. (#12672)
* In Windows 10 en later zal NVDA het aantal suggesties aankondigen bij het invoeren van zoektermen in apps zoals Instellingen en Microsoft Store. (#7330, #12758, #12790)
* Tabelnavigatie wordt nu ondersteund in rasterbesturingselementen die zijn gemaakt met behulp van de Out-GridView-cmdlet in PowerShell. (#12928)

### Veranderingen

* Espeak-ng is bijgewerkt naar 1.51-dev commit `74068b91bcd578bd7030a7a6cde2085114b79b44`. (#12665)
* NVDA zal standaard eSpeak gebruiken als er geen geïnstalleerde OneCore-stemmen de NVDA-voorkeurstaal ondersteunen. (#10451)
* Als OneCore-stemmen consequent niet spreken, wordt eSpeak als synthesizer gebruikt. (#11544)
* Bij het lezen van de statusbalk met `NVDA+end`, wordt de leescursor niet langer naar zijn locatie verplaatst.
Als u deze functionaliteit nodig hebt, wijst u een invoerhandeling toe aan het juiste script in de categorie Objectnavigatie in het dialoogvenster Invoerhandelingen. (#8600)
* Bij het openen van een instellingendialoogvenster dat al geopend is, stelt NVDA de focus in op het bestaande dialoogvenster in plaats van een foutmelding te geven. (#5383)
* Liblouis braillevertaler bijgewerkt naar [3.19.0](https://github.com/liblouis/liblouis/releases/tag/v3.19.0). (#12810)
  * Nieuwe brailletabellen: Russisch graad 1, Tshivenda graad 1, Tshivenda graad 2
* NVDA zal niet langer proberen af ​​te sluiten wanneer dialoogvensters wachten op een vereiste actie (bijv. Bevestigen/Annuleren). (#12984)

### Opgeloste problemen

* Het volgen van toetsenbordmodificaties (zoals Control of Insert) is robuuster wanneer watchdog herstelt. (#12609)
* Het is weer mogelijk om op bepaalde systemen te controleren op NVDA-updates; bijv. schone Windows-installaties. (#12729)
* NVDA meldt correct lege tabelcellen in Microsoft Word bij gebruik van UI automation. (#11043)
* In ARIA-gegevensrastercellen op internet wordt de Escape-toets nu doorgegeven aan het raster en wordt de focusmodus niet langer onvoorwaardelijk uitgeschakeld. (#12413)
* Bij het lezen van een kopcel van een tabel in Chrome, lost het twee keer noemen van de kolomnaam op. (#10840)
* NVDA rapporteert niet langer een numerieke waarde voor UIA-schuifregelaars waarvoor een tekstuele weergave van hun waarde is gedefinieerd. (UIA ValuePattern heeft nu de voorkeur boven RangeValuePattern). (#12724)
* NVDA behandelt de waarde van UIA-schuifregelaars niet langer als altijd op percentages gebaseerd.
* Het rapporteren van de locatie van een cel in Microsoft Excel bij toegang via UI automation werkt weer correct op Windows 11. (#12782)
* NVDA stelt niet langer ongeldige Python-landinstellingen in. (#12753)
* Als een uitgeschakelde add-on wordt verwijderd en vervolgens opnieuw wordt geïnstalleerd, wordt deze opnieuw ingeschakeld. (#12792)
* Bugs opgelost rond het updaten en verwijderen van add-ons waar de add-onmap is hernoemd of waarin bestanden zijn geopend. (#12792, #12629)
* Bij gebruik van UI automation om toegang te krijgen tot Microsoft Excel-spreadsheetbesturingselementen, kondigt NVDA niet langer redundant aan wanneer een enkele cel wordt geselecteerd. (#12530)
* Meer dialoogtekst wordt automatisch gelezen in LibreOffice Writer, zoals in bevestigingsdialogen. (#11687)
* Lezen/navigeren met bladermodus in Microsoft Word via UI automation zorgt er nu voor dat het document altijd wordt gescrolld, zodat de huidige bladermoduspositie zichtbaar is en dat de cursorpositie in focusmodus de bladermoduspositie correct weerspiegelt. (#9611)
* Bij het uitvoeren van Alles lezen in Microsoft Word via UI automation, wordt nu automatisch door het document gescrolld en wordt de positie van de cursor correct bijgewerkt. (#9611)
* Bij het lezen van e-mails in Outlook terwijl NVDA toegang krijgt tot het bericht met UI Automation, worden bepaalde tabellen nu gemarkeerd als lay-outtabellen, wat betekent dat ze niet langer standaard worden gerapporteerd. (#11430)
* Een zeldzame fout bij het wisselen van audioapparaten is verholpen. (#12620)
* Invoer met literaire brailletabellen zou zich betrouwbaarder moeten gedragen in bewerkingsvelden. (#12667)
* Bij het navigeren door de Windows-systeemvakkalender geeft NVDA nu de dag van de week volledig weer. (#12757)
* Bij gebruik van een Chinese invoermethode zoals Taiwan - Microsoft Quick in Microsoft Word, het vooruit en achteruit scrollen van de brailleleesregel blijft niet langer foutief terugspringen naar de oorspronkelijke positie van de cursor. (#12855)
* Bij het lezen van Microsoft Word-documenten via UIA is navigeren per zin (alt+pijl omlaag / alt+pijl omhoog) weer mogelijk. (#9254)
* Bij het openen van MS Word met UIA wordt nu het inspringen van alinea's gerapporteerd. (#12899)
* Bij het openen van MS Word met UIA worden de opdracht voor het volgen van wijzigingen en enkele andere gelokaliseerde opdrachten nu gerapporteerd in Word. (#12904)
* Dubbele braille en spraak opgelost wanneer 'beschrijving' overeenkomt met 'inhoud' of 'naam'. (#12888)
* In MS Word met UIA ingeschakeld, is het afspelen van spelfoutgeluiden terwijl u typt nauwkeuriger. (#12161)
* In Windows 11 zal NVDA niet langer "venster" aankondigen wanneer u op Alt+Tab drukt om tussen programma's te schakelen. (#12648)
* Het nieuwe deelvenster Moderne opmerkingen aan de zijkant wordt nu ondersteund in MS Word wanneer het document niet via UIA wordt geopend. Druk op alt+f12 om tussen het deelvenster en het document te wisselen. (#12982)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2021.2

Deze release introduceert voorlopige ondersteuning voor Windows 11.
Hoewel Windows 11 nog moet worden uitgebracht, is deze release getest op preview-versies van Windows 11.
Dit omvat een belangrijke oplossing voor Schermgordijn (zie belangrijke opmerkingen).
De Probleemoplosser voor COM-registratie kan nu meer problemen oplossen terwijl NVDA wordt uitgevoerd.
Er zijn updates voor de synthesizer eSpeak en braillevertaler LibLouis.
Er zijn ook verschillende bugfixes en verbeteringen, met name voor brailleondersteuning en Windows-terminals, rekenmachine, emoji-paneel en klembordgeschiedenis.

### Belangrijke opmerkingen

Vanwege een wijziging in de Windows Magnification API moest Schermgordijn worden bijgewerkt om de nieuwste versies van Windows te ondersteunen.
Gebruik NVDA 2021.2 om Schermgordijn te activeren met Windows 10 21H2 (10.0.19044) of hoger.
Dit omvat Windows 10 Insiders en Windows 11.
Als u een nieuwe versie van Windows gebruikt, moet u om veiligheidsredenen om een bevestiging vragen van iemand die kan zien dat het schermgordijn het scherm volledig zwart maakt.

### Nieuwe functies

* Experimentele ondersteuning voor ARIA-annotaties:
  * voegt een commando toe om een ​​samenvatting van details van een object met aria-details te lezen. (#12364)
  * voegt een optie toe in geavanceerde instellingen om te melden of een object details heeft in bladermodus. (#12439)
* In Windows 10 versie 1909 en later (inclusief Windows 11) zal NVDA het aantal suggesties aankondigen bij het uitvoeren van zoekopdrachten in Verkenner. (#10341, #12628)
* In Microsoft Word kondigt NVDA nu het resultaat aan van sneltoetsen voor inspringen en verkeerd-om inspringen wanneer ze worden uitgevoerd. (#6269)

### Veranderingen

* Espeak-ng is bijgewerkt naar 1.51-dev commit `` ab11439b18238b7a08b965d1d5a6ef31cbb05cbb ''. (#12449, #12202, #12280, #12568)
* Als artikel is ingeschakeld in de gebruikersinstellingen voor documentopmaak, kondigt NVDA "artikel" aan na de inhoud. (#11103)
* Liblouis braillevertaler bijgewerkt naar [3.18.0](https://github.com/liblouis/liblouis/releases/tag/v3.18.0). (#12526)
  * Nieuwe brailletabellen: Bulgaars graad 1, Birmees graad 1, Birmees graad 2, Kazachs graad 1, Khmer graad 1, Noord-Koerdische graad 0, Sepedi graad 1, Sepedi graad 2, Sesotho graad 1, Sesotho graad 2, Setswana graad 1, Setswana graad 2, Tatar graad 1, Vietnamees graad 0, Vietnamees graad 2, Zuid-Vietnamees graad 1, Xhosa graad 1, Xhosa graad 2, Yakut graad 1, Zulu graad 1, Zulu graad 2
* Windows 10 OCR is hernoemd naar Windows OCR. (#12690)

### Opgeloste problemen

* In Windows 10 Rekenmachine toont NVDA rekenmachine-uitdrukkingen op een brailleleesregel. (#12268)
* In terminalprogramma's in Windows 10 versie 1607 en later worden bij het invoegen of verwijderen van tekens in het midden van een regel de tekens rechts van de cursor niet meer voorgelezen. (#3200)
  * Diff Match Patch nu standaard ingeschakeld. (#12485)
* De braille-invoer werkt correct met de volgende gecontracteerde tabellen: Arabisch graad 2, Spaans graad 2, Urdu graad 2, Chinees (China, Mandarijn) graad 2. (#12541)
* Het COM-registratiehulpprogramma lost nu meer problemen op, vooral op 64-bits Windows. (#12560)
* Verbeteringen aan het gebruik van de knoppen voor de Seika Notetaker braille leesregel van Nippon Telesoft. (#12598)
* Verbeteringen in het melden van het Windows Emoji-paneel en de klembordgeschiedenis. (#11485)
* De karakterbeschrijvingen van het Bengaalse alfabet bijgewerkt. (#12502)
* NVDA sluit veilig af wanneer een nieuw proces wordt gestart. (#12605)
* Het opnieuw selecteren van het Handy Tech brailleleesregelstuurprogramma in het dialoogvenster Brailleleesregel selecteren veroorzaakt geen fouten meer. (#12618)
* Windows versie 10.0.22000 of later wordt herkend als Windows 11, niet als Windows 10. (#12626)
* Ondersteuning voor schermgordijn is hersteld en getest voor Windows-versies tot 10.0.22000. (#12684)
* Als er geen resultaten worden weergegeven bij het filteren van invoerhandelingen, blijft het dialoogvenster voor het configureren van invoerhandelingen werken zoals verwacht. (#12673)
* Een bug opgelost waarbij het eerste menu-item van een submenu in sommige contexten niet werd aangekondigd. (#12624)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2021.1

Deze release bevat optionele experimentele ondersteuning voor UIA in Excel- en Chromium-browsers.
Er zijn verbeteringen voor verschillende talen en voor het openen van koppelingen in braille.
Er zijn updates voor Unicode CLDR, wiskundige symbolen en LibLouis.
En verder Veel bugfixes en verbeteringen, o.a.  in Office, Visual Studio en verschillende talen.

Opmerking:
 add-ons moeten worden bijgewerkt om met deze release van NVDA gebruikt te kunnen worden.
 Deze release heeft ook geen ondersteuning meer voor Adobe Flash.
 -

### Nieuwe functies

* Vroege ondersteuning voor UIA met op Chromium gebaseerde browsers (zoals Edge). (#12025)
* Optionele experimentele ondersteuning voor Microsoft Excel via UI Automation. Alleen aanbevolen voor Microsoft Excel build 16.0.13522.10000 of hoger. (#12210)
* Gemakkelijkere navigatie door uitvoer in de NVDA Python Console. (#9784)
  * alt + pijl omhoog / omlaag springt naar het vorige / volgende uitvoer resultaat (met shift erbij kun je selecteren).
  * control + l wist de uitvoer.
* NVDA meldt nu de categorieën die zijn toegewezen aan een afspraak in Microsoft Outlook, indien van toepassing. (#11598)
* Ondersteuning voor de Seika Notetaker brailleleesregel van Nippon Telesoft. (#11514)

### Veranderingen

* In bladermodus kunnen besturingselementen nu worden geactiveerd met de braillecursorrouterings knoppen bij de beschrijvende afkorting (o.a. "Lnk" voor een link). Dit is vooral handig voor het activeren van bijv. Selectievakjes zonder labels. (#7447)
* NVDA voorkomt nu dat de gebruiker Windows 10 OCR kan uitvoeren als schermgordijn is ingeschakeld. (#11911)
* Unicode Common Locale Data Repository (CLDR) bijgewerkt naar 39.0. (#11943, #12314)
* Meer wiskundige symbolen toegevoegd aan het symbolenwoordenboek. (#11467)
* De gebruikershandleiding, het Wat is er nieuw bestand en de lijst met sneltoetsen hebben nu een vernieuwd uiterlijk. (#12027)
* "Niet-ondersteund" wordt nu gemeld bij een poging om de schermindeling te wijzigen in toepassingen die dit niet ondersteunen, zoals Microsoft Word. (#7297)
* De optie 'Poging om spraak te annuleren voor verlopen focusgebeurtenissen' in het paneel met geavanceerde instellingen is nu standaard ingeschakeld. (#10885)
  * Dit gedrag kan worden uitgeschakeld door deze optie in te stellen op "Nee".
* In webapplicaties (bijv. Gmail) wordt niet langer verouderde informatie meer uitgesproken wanneer de focus snel wordt verplaatst.
* Liblouis braillevertaler bijgewerkt naar [3.17.0](https://github.com/liblouis/liblouis/releases/tag/v3.17.0). (#12137)
  * Nieuwe brailletabellen: Wit-Russische literaire braille, Wit-Russische computerbraille, Urdu graad 1, Urdu graad 2.
* Ondersteuning voor Adobe Flash-inhoud is verwijderd uit NVDA omdat het gebruik van Flash actief wordt ontmoedigd door Adobe. (#11131)
* NVDA zal afsluiten, zelfs als de vensters nog open zijn, het afsluitproces sluit nu alle NVDA-vensters en dialoogvensters. (#1740)
* Het Spraakweergavevenster kan nu worden afgesloten met `` alt + F4 '' en heeft een standaard sluitknop voor eenvoudigere interactie met gebruikers van aanwijsapparaten. (#12330)
* Het Brailleweergavevenster heeft nu een standaard sluitknop voor eenvoudigere interactie met gebruikers van aanwijsapparaten. (#12328)
* In het dialoogvenster Elementenlijst is de sneltoets voor de knop "Activeren" in sommige landen verwijderd om een konflikt met een label van een keuzerondje van het elementtype te voorkomen. Indien beschikbaar, is de knop nog steeds de standaardinstelling van het dialoogvenster en kan als zodanig nog steeds worden opgeroepen door simpelweg op enter te drukken vanuit de elementenlijst zelf. (#6167)

### Opgeloste problemen

* De lijst met berichten in Outlook 2010 is weer leesbaar. (#12241)
* In terminalprogramma's op Windows 10 versie 1607 en later worden bij het invoegen of verwijderen van tekens in het midden van een regel de tekens rechts van de cursor niet meer voorgelezen. (#3200)
  * Deze experimentele oplossing moet handmatig worden ingeschakeld in het paneel met geavanceerde instellingen van NVDA door het diff-algoritme te wijzigen in Diff Match Patch.
* In MS Outlook zullen onnodige afstandsmeldingen bij het shift + tabben van de berichttekst naar het onderwerpveld niet meer moeten voorkomen. (#10254)
* In de Python-console wordt nu het invoegen van een tab voor inspringen aan het begin van een niet-lege invoerregel en het uitvoeren van tabaanvulling in het midden van een invoerregel ondersteund. (#11532)
* Opmaakinformatie en andere doorzoekbare berichten bevatten niet langer onverwachte lege regels wanneer de schermindeling is uitgeschakeld. (#12004)
* Het is nu mogelijk om opmerkingen in MS Word te lezen met UIA ingeschakeld. (#9285)
* De prestaties bij interactie met Visual Studio zijn verbeterd. (#12171)
* Grafische bugs zoals ontbrekende elementen bij gebruik van NVDA met een rechts-naar-links lay-out opgelost. (#8859)
* Baseer de GUI-lay-outrichting op de NVDA-taal, niet de landinstelling van het systeem. (#638)
  * bekend probleem voor talen die van rechts naar links worden geschreven: de rechterrand van groeperingsclips met labels / bedieningselementen. (#12181)
* De Python-locale is zo ingesteld dat deze consistent overeenkomt met de taal die is geselecteerd in de Instellingen, en zal voorkomen bij gebruik van de standaardtaal. (#12214)
* TextInfo.getTextInChunks loopt niet langer vast wanneer gebruikt op Rich Edit-besturingselementen zoals de NVDA-logviewer. (#11613)
* Het is weer mogelijk om NVDA te gebruiken in talen met onderstrepingstekens in de locale naam zoals de_CH op Windows 10 1803 en 1809. (#12250)
* In WordPad werkt de configuratie van superscript / subscript-meldingen zoals verwacht. (#12262)
* NVDA verzuimt niet langer om de nieuw gefocuste inhoud op een webpagina aan te kondigen als de oude focus verdwijnt en wordt vervangen door de nieuwe focus op dezelfde positie. (#12147)
* Doorhalen, superscript en subscript-opmaak voor hele Excel-cellen worden nu gerapporteerd als de overeenkomstige optie is ingeschakeld. (#12264)
* Probleem opgelost met het kopiëren van config tijdens installatie vanaf een draagbare kopie als de standaard bestemmingsconfiguratiemap leeg is. (# 12071, #12205)
* Opgelost: onjuiste aankondiging van sommige letters met accenten of diakritische tekens wanneer de optie 'Het woord "Hoofdletter" uitspreken voor hoofdletters' is aangevinkt. (#11948)
* Probleem met toonhoogteverandering opgelost in SAPI4-spraaksynthesizer. (#12311)
* Het NVDA-installatieprogramma respecteert nu ook de ``--minimal'' opdrachtregelparameter en speelt het opstartgeluid niet af, volgens hetzelfde gedocumenteerde gedrag als een geïnstalleerd of draagbaar exemplaar van NVDA. (#12289)
* In MS Word of Outlook kan de snelnavigatietoets voor tabellen nu naar de lay-outtabel springen als de optie "Lay-outtabellen opnemen" is ingeschakeld in de instellingen van de bladermodus. (#11899)
* NVDA zal niet langer "↑↑↑" aankondigen voor emoji's in bepaalde talen. (#11963)
* Espeak ondersteunt nu weer Kantonees en Mandarijn. (#10418)
* In de nieuwe op Chromium gebaseerde Microsoft Edge worden tekstvelden, zoals de adresbalk, nu aangekondigd als ze leeg zijn. (#12474)
* Probleem met Seika Braille-stuurprogramma opgelost. (#10787)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2020.4

Deze release bevat nieuwe Chinese invoermethoden, een update van Liblouis en de elementenlijst (NVDA + f7) werkt nu in focusmodus.
Contextgevoelige hulp is nu beschikbaar wanneer u op F1 drukt in NVDA-dialoogvensters.
Verbeteringen aan de regels voor de uitspraak van symbolen, het spraakwoordenboek, braillemeldingen en Doorbladeren bij Alles lezen.
Bugfixes en verbeteringen aan Mail, Outlook, Teams, Visual Studio, Azure Data Studio, Foobar2000.
Op internet zijn er verbeteringen in Google Documenten en meer ondersteuning voor ARIA.
Plus vele andere belangrijke bugfixes en verbeteringen. 

### Nieuwe Functies

* Als u in de dialoogvensters van NVDA op F1 drukt, wordt nu het helpbestand geopend op de meest relevante sectie. (#7757)
* Ondersteuning voor suggesties voor automatisch aanvullen (IntelliSense) in Microsoft SQL Server Management Studio plus Visual Studio 2017 en hoger. (#7504)
* Uitspraak van symbolen: ondersteuning voor groepering in een complexe symbooldefinitie en ondersteuning van groepsreferenties in een vervangende regel, waardoor ze eenvoudiger en krachtiger worden. (#11107)
* Gebruikers worden nu op de hoogte gesteld wanneer ze proberen om spraakwoordenboekvermeldingen te maken met ongeldige vervangingen voor reguliere expressies. (#11407)
  * Specifiek worden groeperingsfouten nu gedetecteerd.
* Ondersteuning toegevoegd voor de nieuwe Chinese traditionele snelle en Pinyin-invoermethoden in Windows 10. (#11562)
* Tabkopteksten worden nu beschouwd als formuliervelden met de f-toets voor snelle navigatie. (#10432)
* Een commando toegevoegd om het melden van gemarkeerde tekst in of uit te schakelen; Er is geen standaard sneltoets toegewezen. (#11807)
* De opdrachtregelparameter --copy-portable-config toegevoegd waarmee u de opgegeven configuratie automatisch naar het gebruikersaccount kunt kopiëren wanneer u NVDA stil installeert. (#9676)
* Braille-routing wordt nu ondersteund met het Brailleweergavevenster voor muisgebruikers, beweeg de muis om naar een braillecel te springen. (#11804)
* NVDA zal nu automatisch de Humanware Brailliant BI 40X- en 20X-apparaten detecteren via zowel USB als Bluetooth. (#11819)

### Veranderingen

* Liblouis braillevertaler bijgewerkt naar versie 3.16.1:
 * Lost meerdere crashes op
 * Voegt Bashkir graad 1 brailletabel toe
 * Voegt Koptische 8-punts computer brailletabel toe
 * Voegt Russische literaire braille en Russische literaire braille (gedetailleerd) tabellen toe
 * Voegt Afrikaans graad 2 brailletabel toe
 * Verwijdert de Russische graad 1 brailletabel 
* Bij 'alles lezen' in de bladermodus, stoppen de volgende en vorige zoeken opdrachten het lezen niet meer als de optie Doorbladeren bij alles lezen toestaan is ingeschakeld; het lezen wordt in plaats daar van hervat na het volgende of vorige zoekresultaat. (#11563)
* Voor HIMS-brailleleesregels is F3 opnieuw toegewezen aan spatie + punten 148. (#11710)
* Verbeteringen aan de UX van de opties "braille time-out" voor meldingen en "Toon meldingen voor onbepaalde tijd". (#11602)
* In webbrowsers en andere toepassingen die de bladermodus ondersteunen, kan het dialoogvenster Elementenlijst (NVDA + F7) nu worden opgeroepen in de focusmodus. (#10453)
* Updates voor live ARIA-regio's worden nu onderdrukt wanneer het melden van wijzigingen van dynamische inhoud is uitgeschakeld. (#9077)
* NVDA meldt nu "Gekopieerd naar klembord" vóór de gekopieerde tekst. (#6757)
* Presentatie van grafische weergavetabel in schijfbeheer is verbeterd. (#10048)
* Labels voor bedieningselementen zijn nu uitgeschakeld (grijs weergegeven) wanneer het bedieningselement is uitgeschakeld. (#11809)
* CLDR-emoji-annotatie bijgewerkt naar versie 38. (#11817)
* De ingebouwde "Focus markering" -functie is omgedoopt tot "Visuele markering". (#11700)

### Opgeloste Problemen

* NVDA werkt weer correct met invoervelden bij gebruik van de applicatie Fast Log Entry. (#8996)
* Meld verstreken tijd in Foobar2000 als er geen totale tijd beschikbaar is (bijvoorbeeld bij het afspelen van een livestream). (#11337)
* NVDA respecteert nu het aria-roledescription-attribuut voor elementen in bewerkbare inhoud op webpagina's. (#11607)
* 'lijst' wordt niet langer aangekondigd op elke regel van een lijst in Google Documenten of andere bewerkbare inhoud in Google Chrome. (#7562)
* Wanneer u per teken of woord van het ene lijstitem naar het andere gaat in bewerkbare inhoud op internet, wordt het binnengaan van het nieuwe lijstitem nu aangekondigd. (#11569)
* NVDA leest nu de juiste regel wanneer de cursor aan het einde van een link aan het einde van een lijstitem in Google Documenten of andere bewerkbare inhoud op internet wordt geplaatst. (#11606)
* In Windows 7, het openen en sluiten van het startmenu vanaf het bureaublad plaatst de focus nu correct. (#10567)
* Wanneer "Probeer spraak te annuleren voor verlopen focuswijzigingen" is ingeschakeld, wordt de titel van het tabblad nu opnieuw aangekondigd bij het wisselen van tabbladen in Firefox. (#11397)
* NVDA verzuimt niet langer om een ​​lijstitem te melden na het typen van een teken in een lijst bij het gebruik van de SAPI5 Ivona-stemmen. (#11651)
* Het is weer mogelijk om de bladermodus te gebruiken bij het lezen van e-mails in Windows 10 Mail 16005.13110 en hoger. (#11439)
* Bij gebruik van de SAPI5 Ivona-stemmen van harposoftware.com, kan NvDA nu de configuratie opslaan, van synthesizer wisselen en blijft NVDA niet langer stil na het herstarten. (#11650)
* Het is nu mogelijk om nummer 6 in computerbraille in te voeren vanaf een brailletoetsenbord op HIMS-leesregels. (#11710)
* Grote prestatieverbeteringen in Azure Data Studio. (#11533, #11715)
* Met "Poging om spraak te annuleren voor verlopen focusgebeurtenissen" ingeschakeld, wordt de titel van het NVDA-zoeken dialoogvenster opnieuw aangekondigd. (#11632)
* NVDA zou niet langer moeten bevriezen bij het ontwaken van de computer als de focus terecht komt in een Microsoft Edge-document. (#11576)
* Het is niet langer nodig om op tab te drukken of de focus te verplaatsen na het sluiten van een contextmenu in MS Edge om de bladermodus weer te laten werken. (#11202)
* NVDA verzuimt niet langer om items in lijstweergaven te lezen binnen een 64-bits applicatie zoals Tortoise SVN. (#8175)
* ARIA-treegrids worden nu weergegeven als normale tabellen in bladermodus in zowel Firefox als Chrome. (#9715)
* Een omgekeerde zoekopdracht kan nu worden gestart met 'vorige zoeken' via NVDA + shift + F3 (#11770)
* Een NVDA-script wordt niet langer als herhaald beschouwd als een niet-gerelateerde toetsaanslag plaatsvindt tussen de twee uitvoeringen van het script. (#11388)
* Sterke tags en nadruk tags in Internet Explorer kunnen weer niet gemeld worden door Nadruk melden uit te schakelen in de NVDA-instellingen voor documentopmaak. (#11808)
* Een bevriezing van enkele seconden die door een klein aantal gebruikers wordt ervaren bij het verplaatsen tussen cellen met de pijltjes in Excel zou niet langer moeten voorkomen. (#11818)
* In Microsoft Teams-builds met versienummers zoals 1.3.00.28xxx, faalt NVDA niet langer bij het lezen van berichten in chats of Teams-kanalen vanwege een verkeerd gefocust menu. (#11821)
* Tekst die zowel als een spelling- en grammaticafout is gemarkeerd in Google Chrome, wordt door NVDA ook aangekondigd als zowel een spellings- als grammaticafout. (#11787)
* Bij gebruik van Outlook (Franse versie) werkt de sneltoets voor 'Allen beantwoorden' (control + shift + R) weer. (#11196)
* In Visual Studio worden IntelliSense-tooltips die aanvullende details geven over het momenteel geselecteerde IntelliSense-item nu slechts één keer gerapporteerd. (#11611)
* In Windows 10 Rekenmachine kondigt NVDA de voortgang van berekeningen niet aan als uitspreken van getypte tekens is uitgeschakeld. (#9428)
* NVDA crasht niet langer bij gebruik van Engels US grade 2 en met Woord onder cursor uitbreiden naar computerbraille  ingeschakeld, bij het weergeven van bepaalde inhoud, zoals een URL in braille. (#11754)
* Het is weer mogelijk om opmaakinformatie te rapporteren voor de gefocuste Excel-cel met NVDA + F. (#11914)
* QWERTY-invoer op Papenmeier-brailleleesregels die dit ondersteunen, werkt weer en veroorzaakt niet langer dat NVDA willekeurig vastloopt. (#11944)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2020.3

Deze release bevat verschillende grote verbeteringen op het gebied van stabiliteit en prestaties, met name in Microsoft Office-toepassingen. Er zijn nieuwe instellingen om touchscreenondersteuning en grafische rapportage in of uit te schakelen.
Het bestaan ​​van gemarkeerde inhoud kan in browsers worden gemeld en er zijn nieuwe Duitse brailletabellen.

### Nieuwe Functies

* U kunt nu het melden van afbeeldingen in- en uitschakelen via de instellingen voor documentopmaak van NVDA. Merk op dat als u deze optie uitschakelt, nog steeds de alternatieve teksten van afbeeldingen worden gelezen. (#4837)
* U kunt nu de touchscreen-ondersteuning van NVDA in- en uitschakelen. Er is een optie toegevoegd aan de instellingen voor aanraakinteractie van de NVDA-instellingen. De standaardsneltoets is NVDA+control+alt+t. (#9682)
* Nieuwe Duitse brailletabellen toegevoegd. (#11268)
* NVDA detecteert nu UIA-tekstvelden die alleen lezen zijn. (#10494)
* Het bestaan ​​van gemarkeerde (gehighlighte) inhoud wordt in alle webbrowsers zowel in spraak als in braille gemeld. (#11436)
 * Dit kan worden in- en uitgeschakeld met de nieuwe optie voor gemarkeerde tekst in de NVDA-instellingen voor documentopmaak.
* Nieuwe geëmuleerde systeemtoetsen kunnen worden toegevoegd vanuit het NVDA-dialoogvenster Invoerhandelingen. (#6060)
 * Om dit te doen, drukt u op de knop Toevoegen nadat u de categorie Geëmuleerde systeemtoetsen heeft geselecteerd.
* Handy Tech Active Braille met joystick wordt nu ondersteund. (#11655)
* De instelling "Automatische focusmodus bij cursorbeweging" is nu compatibel met het uitschakelen van "Systeemfocus automatisch verplaatsen naar focusbare elementen". (#11663)

### Veranderingen

* Het script om opmaakinformatie op te vragen (NVDA + f) is dusdanig gewijzigd dat het nu de opmaak onder de systeemcursor meldt in plaats van bij de leescursor. Voor de opmaak bij de positie van de leescursor gebruikt u NVDA+shift+f. (#9505)
* NVDA stelt de systeemfocus niet langer standaard automatisch in op focusbare elementen in de bladermodus, waardoor de prestaties en stabiliteit worden verbeterd. (#11190)
* CLDR bijgewerkt van versie 36.1 naar versie 37. (#11303)
* eSpeak-NG bijgewerkt naar 1.51-dev, commit 1fb68ffffea4
* U kunt nu tabelnavigatie gebruiken in lijsten met lijstitems met selectievakjes wanneer de betreffende lijst meerdere kolommen heeft. (#8857)
* Wanneer in het venster Add-ons beheren wordt gevraagd om het verwijderen van een add-on te bevestigen, is "Nee" nu de standaardinstelling. (#10015)
* In de elementenlijst binnen Microsoft Excel worden formules nu in hun vertaalde vorm weergegeven. (#9144)
* NVDA gebruikt nu de juiste terminologie voor notities in MS Excel. (#11311)
* Bij gebruik van het script "Verplaats leescursor naar focus" in bladermodus, wordt de leescursor nu geplaatst op de positie van de virtuele cursor. (#9622)
* Informatie die wordt gemeld in bladermodus, zoals de opmaakinformatie met NVDA+F, wordt nu weergegeven in een iets groter venster gecentreerd op het scherm. (#9910)

### Opgeloste Problemen

* NVDA spreekt nu altijd bij het navigeren per woord en bij het navigeren langs een enkel symbool dat gevolgd wordt door witruimte, ongeacht de breedsprakigheidsinstellingen. (#5133)
* In applicaties die QT 5.11 of nieuwer gebruiken, worden objectbeschrijvingen opnieuw gemeld. (#8604)
* Bij het verwijderen van een woord met control+delete, blijft NVDA niet langer stil. (#3298, #11029)
  * Nu wordt het woord rechts van het verwijderde woord gemeld.
* In de algemene instellingen van NVDA wordt de talenlijst nu correct gesorteerd. (#10348)
* In het dialoogvenster Invoerhandelingen zijn de prestaties tijdens het filteren aanzienlijk verbeterd. (#10307)
* U kunt nu Unicode-tekens buiten U+FFFF verzenden vanaf een brailleleesregel. (#10796)
* NVDA meldt de inhoud van het Openen met dialoogvenster nu correct in de Mei 2020 update van Windows 10. (#11335)
* Een nieuwe experimentele optie in de Geavanceerde instellingen (Selectieve registratie voor UI Automation gebeurtenissen en elementwijzigingen inschakelen) kan belangrijke prestatieverbeteringen bieden in Microsoft Visual Studio en andere op UIAutomation gebaseerde applicaties, indien ingeschakeld. (#11077, #11209)
* Voor lijstitems met selectievakje wordt de geselecteerde status niet langer nutteloos aangekondigd, en indien van toepassing wordt de niet-geselecteerde status in plaats daarvan aangekondigd. (#8554)
* Bij gebruik van de Mei 2020 update van Windows 10 toont NVDA nu "Microsoft-geluidstoewijzing" bij het bekijken van uitvoerapparaten vanuit het dialoogvenster voor synthesizerselectie. (#11349)
* In Internet Explorer worden nummers nu correct aangekondigd voor geordende lijsten als de lijst niet begint met 1. (#8438)
* In Google Chrome meldt NVDA nu voor alle aanvinkbare besturingselementen (niet alleen selectievakjes) dat ze niet aangevinkt zijn wanneer dit niet het geval is. (#11377)
* Het is weer mogelijk om in verschillende besturingselementen te navigeren wanneer de taal van NVDA is ingesteld op Aragonees. (#11384)
* NVDA zou niet langer soms moeten vastlopen in Microsoft Word bij het snel omhoog en omlaag pijlen of het typen van tekens terwijl Braille is ingeschakeld. (#11431, #11425, #11414)
* NVDA voegt aan het einde van het klembord niet langer een niet-bestaande spatie toe bij het kopiëren van het huidige navigatorobject. (#11438)
* NVDA activeert het automatisch lezen configuratieprofiel niet langer als er niets te lezen is. (#10899, #9947)
* Het is niet langer onmogelijk voor NVDA om de lijst met onderdelen te lezen in internet Information Services (IIS) Manager. (#11468)
* NVDA houdt het audioapparaat nu open en verbetert de prestaties met sommige geluidskaarten. (#5172, #10721)
* NVDA zal niet langer vastlopen of afsluiten bij het ingedrukt houden van control+shift+Pijl omlaag in Microsoft Word. (#9463)
* De uitgevouwen / samengevouwen status van mappen in de navigatiestructuur op drive.google.com wordt nu altijd gerapporteerd door NVDA. (#11520)
* NVDA detecteert automatisch de NLS eReader Humanware brailleleesregel via Bluetooth wanneer de Bluethooth-naam "NLS eReader Humanware" is. (#11561)
* Grote prestatieverbeteringen in Visual Studio Code. (#11533)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2020.2

Hoogtepunten van deze release zijn onder meer ondersteuning voor een nieuwe brailleleesregel van Nattiq, betere ondersteuning voor de ESET antivirus GUI en Windows Terminal, prestatieverbeteringen in 1Password en met de Windows OneCore synthesizer. Plus vele andere belangrijke oplossingen en verbeteringen.

### Nieuwe Functies

* Ondersteuning voor nieuwe brailleleesregels:
  * Nattiq nBraille (#10778)
* Script toegevoegd om de configuratiemap van NVDA te openen (geen standaard toegewezen invoerhandeling). (#2214)
* Betere ondersteuning voor ESET antivirus GUI. (#10894)
* Ondersteuning toegevoegd voor Windows Terminal. (#10305)
* Een commando toegevoegd om het actieve configuratieprofiel te melden (standaard geen invoerhandeling). (#9325)
* Een commando toegevoegd om het melden van subscripts en superscripts in- en uit te schakelen (standaard geen invoerhandeling). (#10985)
* Webapplicaties (bijv. Gmail) spreken geen verouderde informatie meer uit wanneer de focus snel wordt verplaatst. (#10885)
  * Deze experimentele oplossing moet handmatig worden ingeschakeld via de optie 'Probeer spraak te annuleren voor verlopen focuswijzigingen' in het paneel met geavanceerde instellingen.
* Er zijn veel meer symbolen toegevoegd aan het standaard interpunctiewoordenboek. (#11105)

### Veranderingen

* Liblouis braillevertaler bijgewerkt van 3.12 naar [3.14.0](https://github.com/liblouis/liblouis/releases/tag/v3.14.0). (#10832, #11221)
* Het melden van superscripts en subscripts wordt nu apart beheerd van het melden van lettertypeattributen. (#10919)
* Vanwege wijzigingen die zijn aangebracht in VS Code, schakelt NVDA de bladermodus in Code niet langer standaard uit. (#10888)
* NVDA rapporteert niet langer de berichten "boven" en "onder" wanneer de leescursor rechtstreeks naar de eerste of laatste regel van het huidige navigatorobject wordt verplaatst met de scripts voor respectievelijk verplaats naar vorige/volgende regel. (#9551)
* NVDA meldt niet langer de berichten "links" en "rechts" bij het direct verplaatsen van de leescursor naar het eerste of laatste teken van de regel voor het huidige navigatorobject met de scripts voor respectievelijk verplaats naar begin/einde regel. (#9551)

### Opgeloste Problemen

* NVDA start nu correct wanneer het logbestand niet kan worden aangemaakt. (#6330)
* In recente releases van Microsoft Word 365 kondigt NVDA niet langer aan dat het vorige woord is verwijderd wanneer Control+Backspace wordt ingedrukt tijdens het bewerken van een document. (#10851)
* In Winamp kondigt NVDA opnieuw de status aan bij het in- en uitschakelen van shuffle en herhalen. (#10945)
* NVDA is niet langer extreem traag bij het navigeren binnen de lijst met items in 1Password. (#10508)
* De Windows OneCore-spraaksynthesizer is niet langer traag tussen uitspraken. (#10721)
* NVDA loopt niet langer vast wanneer u het contextmenu voor 1Password opent vanuit de systeemwerkbalk. (#11017)
* In Office 2013 en ouder:
  * Linten worden aangekondigd wanneer de focus er voor het eerst naartoe wordt verplaatst. (#4207)
  * Contextmenu-items worden weer correct gemeld. (#9252)
  * Lintsecties worden consequent aangekondigd bij het navigeren met Control+pijltjes. (#7067)
* In de bladermodus in Mozilla Firefox en Google Chrome verschijnt tekst niet langer ten onrechte op een aparte regel wanneer de webinhoud CSS display: inline-flex gebruikt. (#11075)
* In bladermodus met Systeemfocus automatisch verplaatsen naar focusbare elementen uitgeschakeld, is het nu mogelijk om elementen te activeren die de focus niet kunnen hebben.
* In bladermodus met Systeemfocus automatisch verplaatsen naar focusbare elementen uitgeschakeld, is het nu mogelijk om elementen te activeren waar naartoe is genavigeerd door op de Tab-toets te drukken. (#8528)
* In bladermodus met Systeemfocus automatisch verplaatsen naar focusbare elementen uitgeschakeld, veroorzaakt het activeren van bepaalde elementen niet langer een muisklik op een verkeerde locatie. (#9886)
* NVDA logt niet langer een foutmelding bij het gebruik van DevExpress-tekstvelden. (#10918)
* De flitsberichten van de pictogrammen in het systeemvak worden niet langer gerapporteerd bij toetsenbordnavigatie als hun tekst gelijk is aan de naam van de pictogrammen, om dubbele aankondiging te voorkomen. (#6656)
* In bladermodus met Systeemfocus automatisch verplaatsen naar focusbare elementen uitgeschakeld, krijgt bij schakelen naar focusmodus met NVDA + spatie nu het element onder de cursor de focus. (#11206)
* Op bepaalde systemen is het weer mogelijk om te controleren op NVDA-updates; bijv. schone Windows-installaties. (#11253)
* De focus wordt niet langer verplaatst in Java-applicaties wanneer de selectie wordt gewijzigd in een boomstructuur, tabel of lijst die niet de focus heeft. (#5989)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2020.1

Hoogtepunten van deze release zijn onder meer ondersteuning voor verschillende nieuwe brailleleesregels van HumanWare en APH, plus vele andere belangrijke bugfixes zoals de mogelijkheid om wiskunde opnieuw te lezen in Microsoft Word met MathPlayer / MathType.

### Nieuwe Functies

* Het momenteel geselecteerde item in keuzelijsten wordt opnieuw gepresenteerd in bladermodus in Chrome, vergelijkbaar met NVDA 2019.1. (#10713)
* U kunt nu met de rechtermuisknop klikken door iddel van 	touchscreens door met één vinger te tikken en vast te houden. (#3886)
* Ondersteuning voor nieuwe brailleleesregels: APH Chameleon 20, APH Mantis Q40, HumanWare BrailleOne, BrailleNote Touch v2 en NLS eReader. (#10830)

### Veranderingen

* NVDA probeert te voorkomen dat het systeem vergrendelt of in slaap valt tijdens automatisch lezen. (#10643)
* Ondersteuning voor out-of-process iframes in Mozilla Firefox. (#10707)
* Liblouis braillevertaler bijgewerkt naar versie 3.12. (#10161)

### Opgeloste Problemen

* Probleem opgelost waardoor NVDA het Unicode-minteken (U+2212) niet uitsprak. (#10633)
* Bij het installeren van een add-on vanuit het dialoogvenster Add-ons beheren worden namen van bestanden en mappen in het bladervenster niet langer tweemaal gemeld. (#10620, #2395)
* In Firefox, wanneer Mastodon wordt geladen met de geavanceerde webinterface ingeschakeld, worden alle tijdlijnen nu correct weergegeven in bladermodus. (#10776)
* In bladermodus meldt NVDA nu "uitgeschakeld" voor niet-ingeschakelde selectievakjes waar dit voorheen niet het geval was. (#10781)
* ARIA switch besturingselementen melden niet langer verwarrende informatie zoals "niet ingedrukt ingeschakeld" or "pressed checked". (#9187)
* SAPI4 stemmen zouden niet langer moeten kunnen weigeren om bepaalde tekst uit te spreken. (#10792)
* NVDA kan weer wiskundige vergelijkingen in Microsoft Word lezen en ermee werken. (#10803)
* NVDA is weer in staat om te melden dat tekst wordt gedeselecteerd in bladermodus als op een pijltoets wordt gedrukt terwijl er tekst is geselecteerd. (#10731).
* NVDA wordt niet meer afgesloten als er een fout optreedt bij het initialiseren van eSpeak. (#10607)
* Fouten veroorzaakt door unicode in vertalingen voor snelkoppelingen stoppen het installatieprogramma niet langer, wat berijkt wordt door terug te vallen op de Engelse tekst. (#5166, #6326)
* Het uit en weg van lijsten navigeren met de pijltjestoetsen wanneer doorbladeren tijdens automatisch lezen is ingeschakeld, kondigt niet langer continu het verlaten van de lijst of tabel aan. (#10706)
* Muis volgen voor sommige MSHTML-elementen in Internet Explorer functioneert weer naar behoren. (#10736)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2019.3

NVDA 2019.3 is een zeer belangrijke release die veel veranderingen onder de motorkap bevat, waaronder de upgrade van Python 2 naar Python 3 en een belangrijke herschrijving van het spraaksubsysteem van NVDA.
Hoewel deze wijzigingen de compatibiliteit met oudere NVDA-add-ons verbreken, is de upgrade naar Python 3 noodzakelijk voor de veiligheid. De veranderingen in het spraaksysteem zorgen daarnaast voor belangrijke innovatiemogelijkheden in de nabije toekomst.
 Andere hoogtepunten in deze release zijn 64-bits ondersteuning voor Java, schermgordijn en focusmarkeringsffunctionaliteit, ondersteuning voor meer brailleleesregels en een nieuw spraakweergavevenster, en vele andere probleemojplossingen.

### Nieuwe Functies

* In Opdrachtprompt, PowerShell en het Windows Subsystem for Linux op Windows 10 version 1809 en nieuwer:
 * Sterk verbeterde prestaties en stabiliteit. (#9771)
 * Het melden van getypte tekst die niet op het scherm verschijnt (zoals wachtwoorden) kan nu worden ingeschakeld via een optie in het geavanceerde instellingenpaneel van NVDA. (#9649)
* De nauwkeurigheid van het commando muis naar navigatorobject verplaatsen is verbeterd in tekstvelden in Java-toepassingen. (#10157)
* Schermgordijn, dat, indien ingeschakeld, het hele scherm zwart maakt op Windows 8 en hoger. (#7857)
* Ondersteuning voor de volgende Handy Tech brailleleesregels toegevoegd (#8955):
 * Basic Braille Plus 40
 * Basic Braille Plus 32
 * Connect Braille
* Alle door de gebruiker gedefinieerde invoerhandelingen kunnen nu worden verwijderd via een nieuwe knop "Fabrieksinstellingen herstellen" in het dialoogvenster Invoerhandelingen. (#10293)
* Het melden van het lettertype in Microsoft Word omvat nu ook of tekst is gemarkeerd als verborgen. (#8713)
* Een commando toegevoegd om de leescursor te verplaatsen naar de positie die eerder was ingesteld als startmarkering voor selectie of kopiëren: NVDA+shift+F9. (#1969)
* In Internet Explorer, Microsoft Edge en recente versies van Firefox en Chrome worden oriëntatiepunten (landmarks) nu gemeld in focusmodus en bij objectnavigatie. (#10101)
* In Internet Explorer, Google Chrome en Mozilla Firefox kunt u nu navigeren per artikel met gebruik van snelnavigatiescripts. Deze scripts zijn standaard niet toegewezen en kunnen worden toegewezen in het dialoogvenster Invoerhandelingen wanneer het dialoogvenster wordt geopend vanuit een bladermodusdocument. (#9227)
* In Internet Explorer, Google Chrome en Mozilla Firefox worden artikel-elementen nu gemeld bij objectnavigatie en optioneel in de bladermodus indien ingeschakeld in de instellingen voor documentopmaak. (#10424)

### Veranderingen

* De gebruikershandleiding beschrijft nu hoe NVDA te gebruiken in de Windows Console. (#9957)
* Het uitvoeren van nvda.exe zal nu een ​​reeds actief exemplaar van NVDA afsluiten alvorens NVDA te starten. De opdrachtregelparameter -r | --replace wordt nog steeds geaccepteerd, maar genegeerd. (#8320)
* In Windows 8 en nieuwer meldt NVDA nu productnaam- en versiegegevens voor gehoste apps zoals apps die zijn gedownload vanuit de Microsoft Store. Deze informatie wordt door de app verstrekt. (#4259, #10108)
* Bij het met het toetsenbord in- en uitschakelen van wijzigingen bijhouden in Microsoft Word zal NVDA de status van de instelling melden. (#942) 
* Het NVDA-versienummer wordt nu vastgelegd als het eerste bericht in het logboek. Dit gebeurt zelfs als logboekregistratie is uitgeschakeld in de instellingen. (#9803)
* In het instellingendialoogvenster kunt u het geconfigureerde logniveau niet meer wijzigen als dit is overschreven vanaf de opdrachtregel. (#10209)
* In Microsoft Word meldt NVDA nu de weergavestatus van niet-afdrukbare tekens bij het indrukken van de sneltoets Ctrl+Shift+8. (#10241)
* Wanneer het melden van CLDR-tekens (inclusief emoji) is ingeschakeld worden ze nu uitgesproken op alle symboolniveaus. (#8826)
* Pythonpakketten van derden die zijn opgenomen in NVDA, zoals comtypes, registreren nu hun waarschuwingen en fouten in het NVDA-logboek. (#10393)

### Opgeloste Problemen

* Emoji en andere 32-bits unicode-tekens nemen nu minder ruimte in op een brailleleesregel wanneer ze worden weergegeven als hexadecimale waarden. (#6695)
* In Windows 10 zal NVDA flitsberichten van universele apps aankondigen als NVDA is geconfigureerd om flitsberichten te rapporteren in de instellingen voor objectweergave. (#8118)
* In Windows 10 versie 1607 en nieuwer wordt getypte tekst nu gemeld in Mintty. (#1348)
* In Windows 10 versie 1607 en hoger wordt de uitvoer in de Windows-console die dicht bij de cursor verschijnt niet meer gespeld. (#513)
* Besturingselementen in het Compressor dialoogvenster in Audacity worden nu gemeld tijdens het navigeren in het venster. (#10103)
* NVDA behandelt spaties niet langer als woorden bij het gebruik van de leescursor in op Scintilla gebaseerde tessktverwerkers zoals Notepad++. (#8295)
* NVDA zal voorkomen dat het systeem in de slaapstand gaat wanneer er door tekst wordt gescrolld met een brailleleesregel. (#9175)
* In Windows 10 zullen veranderingen correct weergegeven worden in braille bij het bewerken van celinhoud in Microsoft Excel en in andere UIA-tekstbesturingselementen waar dit eerder niet het geval was. (#9749)
* NVDA meldt opnieuw suggesties in de adresbalk van Microsoft Edge. (#7554)
* NVDA blijft niet langer stil bij het focussen van een HTML-tabbesturingselement in Internet Explorer. (#8898)
* In Microsoft Edge op basis van EdgeHTML speelt NVDA geen geluid voor zoeksuggesties meer af wanneer het venster wordt gemaximaliseerd. (#9110, #10002)
* ARIA 1.1 vervolgkeuezelijsten worden nu ondersteund in Mozilla Firefox en Google Chrome. (#9616)
* NVDA meldt niet langer de inhoud van visueel verborgen kolommen voor lijstitems in SysListView32-besturingselementen. (#8268)
* Het dialoogvenster Instellingen laat niet langer "informatie" zien als het huidige logniveau wanneer gebruikt op een beveiligd bureaublad. (#10209)
* In het Start-menu van de Windows 10 Verjaardagsupdate en niewuer zal NVDA details van zoekresultaten melden. (#10232)
* Als in de bladermodus het document wordt gewijzigd als de cursor wordt verplaatst of snelnavigatie wordt gebruikt, spreekt NVDA in sommige gevallen niet langer onjuiste inhoud uit. (#8831, #10343)
* Sommige namen van opsommingstekens in Microsoft Word zijn gecorrigeerd. (#10399)
* In de Windows 10 mei 2019 Update en nieuwer zal NVDA opnieuw de eerst geselecteerde emoji of het eerste klemborditem melden wanneer respectievelijk het emoji-paneel en de klembordgeschiedenis worden geopend. (#9204)
* In Poedit is het opnieuw mogelijk om sommige vertalingen te bekijken voor talen van rechts naar links. (#9931)
* In de Instellingen-app in de Windows 10 april 2018 Update en nieuwer meldt NVDA niet langer voortgangsbalkinformatie voor volumemeters op de pagina Systeem / Geluid. (#10284)
* Ongeldige reguliere expressies in spraakwoordenboeken zorgen er niet langer voor dat de spraak in NVDA stopt met werken. (#10334)
* Bij het lezen van items met opsommingstekens in Microsoft Word met UIA ingeschakeld, wordt het opsommingsteken van het volgende lijstitem niet langer ten onrechte gemeld. (#9613)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2019.2.1

In deze versie van NVDA zijn er diverse crashes opgelost die zich voordeden in 2019.2, waaronder:

* Verschillende crashes opgelost in Gmail die merkbaar waren in zowel Firefox als Chrome bij interactie met bepaalde pop-upmenu's zoals bij het maken van filters of het wijzigen van bepaalde Gmail-instellingen. (#10175, #9402, #8924)
* In Windows 7 veroorzaakt NVDA niet langer een crash van de Windows Verkenner wanneer de muis wordt gebruikt in het startmenu. (#9435) 
* Windows Verkenner in Windows 7 crasht niet langer bij het gebruik van metadata-invoervelden. (#5337) 
* NVDA crasht niet langer bij interactie met afbeeldingen met een base64 URI in Mozilla Firefox of Google Chrome. (#10227)

## 2019.2

Hoogtepunten in deze versie zijn automatische detectie van Freedom Scientific brailleleesregels, een expirimentele functie in de geavanceerde instellingencategorie waardoor de bladermodus de focus niet langer automatisch verplaatst (wat mogelijk prestatieverbeteringen oplevert), toevoeging van de optie snelheidsboost voor de Windows OneCore synthesizer voor het gebruiken van zeer snelle spraak, en vele andere oplossingen voor problemen.

### Nieuwe Functies

* NVDA's ondersteuning voor Miranda NG werkt met nieuwere versies van de client. (#9053) 
* U kunt nu standaard de bladermodus uitschakelen door het uitschakelen van de optie "Bladermodus inschakelen bij laden van pagina" in de NVDA-instellingen voor de bladermodus. (#8716) 
 * Merk op dat wanneer deze optie is uitgeschakeld, u nog steeds de bladermodus handmatig kunt inschakelen door op NVDA+spatie te drukken.
* U kunt nu symbolen filteren in het dialoogvenster voor uitspraak van interpunctie en symbolen, vergelijkbaar met hoe filteren werkt in de elementenlijst en het dialoogvenster invoerhandelingen. (#5761)
* Er is een commando toegevoegd om de Resolutie van de teksteenheid voor de muis aan te passen (hoeveel tekst er wordt uitgesproken wanneer de muis zich verplaatst), er is geen standaardinvoerhandeling aan toegewezen. (#9056)
* De windows OneCore synthesizer heeft nu een optie snelheidsboost, die aanzienlijk snellere spraak mogelijk maakt. (#7498)
* De optie snelheidsboodst kan nu ingesteld worden in de ring met synthesizerinstellingen voor ondersteunde spraaksynthesizers. (Momenteel eSpeak-NG en Windows OneCore). (#8934)
* Configuratieprofielen kunnen nu handmatig worden geactiveerd met invoerhandelingen. (#4209)
 * De invoerhandeling moet worden ingesteld in het dialoogvenster "Invoerhandelingen".
* In Eclipse, ondersteuning toegevoegd voor automatische aanvullingen in de code editor. (#5667)
 * Bovendien kan Javadoc-informatie worden gelezen vanuit de editor wanneer deze aanwezig is door NVDA + d te gebruiken.
* Er is een experimentele optie toegevoegd aan het paneel met Geavanceerde instellingen waarmee u kunt voorkomen dat de systeemfocus de bladermoduscursor volgt (Systeemfocus automatisch verplaatsen naar focusbare elementen). (#2039) Hoewel dit misschien niet geschikt is om voor alle websites uit te schakelen , kan dit mogelijk de volgende problemen oplossen: 
 * Rubberen band effect: NVDA maakt de laatste toetsaanslag binnen de bladermodus sporadisch ongedaan door naar de vorige locatie te springen.
 * Invoervelden die de systeemfocus stelen wanneer u op sommige websites door deze invoervelden loopt.
 * De toetsaanslagen in de bladermodus reageren traag.
* Voor ondersteunde brailleleesregels kunnen de instellingen van de driver nu gewijzigd worden vanuit de categorie braillein NVDA's instellingenvenster. (#7452)
* Automatische detectie van Freedom Scientific brailleleesregels wordt nu ondersteund. (#7727)
* Er is een commando toegevoegd om de vervanging weer te geven van het symbool onder de leescursor. (#9286)
* Er is een experimentele optie toegevoegd aan het paneel met Geavanceerde instellingen die u in staat stel om een nieuwe, in ontwikkeling zijnde herschreven implementatie te proberen van NVDA's Windows Console ondersteuning die gebruik maakt van de Microsoft UI Automation API. (#9614)
* In the Python Console ondersteunt het invoerveld nu het plakken van meerdere regels vanaf het klembord. (#9776)

### Veranderingen

* Synthesizervolume wordt nu verhoogd en verlaagd met 5 in plaats van 10 bij gebruik van de instellingenring. (#6754)
* De tekst in add-onbeheer verduidelijkt wanneer NVDA wordt gestart met de --disable-addons parameter. (#9473)
* Unicode Common Locale Data Repository (uitspraak van emoji) bnbijgewerkt naar versie 35.0. (#9445)
* Wanneer een automatisch gedetecteerde brailleleesregel via Bluetooth verbonden is, zal NVDA blijven zoeken naar USB-leesregels die door dezelfde driver worden aangestuurd en overschakelen naar een USB-verbinding als deze beschikbaar komt. (#8853)
* eSpeak-NG is bijgewerkt naar commit 67324cc.
* Liblouis braillevertaler bijgewerkt naar versie 3.10.0. (#9439, #9678)
* NVDA meldt het woord 'geselecteerd' nu na de zojuist door de gebruiker geselecteerde tekst. (#9028, #9909)
* In Microsoft Visual Studio Code is de bladermodus nu standaard uitgeschakeld. (#9828)

### Opgeloste Problemen

* NVDA crasht niet langer als de map van een add-on leeg is. (#7686)
* Links-naar-rechts en rechts-naar-links-markeringen worden niet langer weergegeven in Braille of spraak bij het openen van het eigenschappenvenster. (#8361)
* Bij het springen naar formuliervelden met snelnavigatie in de bladermodus wordt nu het volledige formulierveld gemeld in plaats van alleen de eerste regel. (#9388)
* NVDA valt niet langer stil na het afsluiten van de Windows 10 Mail-app. (#9341)
* NVDA weigert niet langer te starten wanneer de regionale instellingen van de gebruiker is ingesteld op een taal die niet bekend is bij NVDA, zoals Engels (Nederland). (#8726)
* Als de bladermodus is ingeschakeld in Microsoft Excel en u overschakelt naar een browser in de focusmodus of vice versa, wordt de status van de bladermodus nu juist gemeld. (#8846)
* NVDA meldt nu correct de regel onder de muiscursor in Notepad++ en andere op Scintilla gebaseerde tekstverwerker. (#5450)
* In Google Docs (en andere webgebaseerde tekstverwerkers) wordt er in braille niet langer onterecht "lst einde" getoond voor de cursor in het midden van een lijstitem. (#9477)
* In de Windows 10 mei 2019 Update spreekt NVDA niet langer veel volumemeldingen uit als het volume wordt gewijzigd met hardwareknoppen wanneer de Windows Verkenner de focus heeft. (#9466)
* Het laden van het dialoogvenster voor uitspraak van interpunctie en symbolen is nu veel sneller bij het gebruik van symboolwoordenboeken met meer dan 1000 items. (#8790)
* In Scintilla-besturingselementen zoals Notepad++ is NVDA nu in staat om de juiste regel te melden wanneer automatische terugloop is ingeschakeld. (#9424)
* In Microsoft Excel wordt de locatie van de cel nu gemeld nadat deze is gewijzigd als gevolg van de toetscombinatie shift+enter of shift+numpadEnter. (#9499)
* In Visual Studio 2017 en nieuwer wordt in de Objects Explorer het geselecteerde item in de objects tree of members tree nu correct gemeld. (#9311)
* Add-ons met namen die alleen verschillen in hoofdletters worden niet langer als afzonderlijke add-ons behandeld. (#9334)
* Voor Windows OneCore stemmen wordt de in NVDA ingestelde snelheid niet langer beinvloed door de ingestelde snelheid in de Windows 10 Spraakinstellingen. (#7498)
* Het logboek kan nu worden geopend met NVDA+F1 wanneer er geen ontwikkelaarsinfo is voor het huidige navigatorobject. (#8613)
* Het is opnieuw mogelijk om NVDA's tabelnavigatiecommando's te gebruiken in Google Docs, in Firefox en Chrome. (#9494)
* De bumpertoetsen op Freedom Scientific brailleleesregels werken nu correct. (#8849)
* Bij het lezen van het eerste teken van een document in Notepad++ 7.7 X64 zal NVDA niet langer tot wel tien seconden bevriezen. (#9609)
* HTCom kan nu gebruikt worden met een Handy Tech brailleleesregel in combinatie met NVDA. (#9691)
* In Mozilla Firefox worden updates in een live region niet langer gemeld wanneer de live region zich in een achtergrondtablad bevindt. (#1318)
* Het zoekvenster van de NVDA bladermodus functioneert nu ook wanneer het Over dialoogvenster momenteel in de achtergrond is geopend. (#8566)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2019.1.1

In deze versie van NVDA zijn de volgende problemen opgelost:

* NVDA veroorzaakt niet langer een crash van Excel 2007 en weigert niet langer om te melden wanneer een cel een formule heeft. (#9431)
* Google Chrome crasht niet langer bij interactie met bepaalde keuzelijsten. (#9364)
* Er is een probleem opgelost waardoor de gebruikersconfiguratie mogelijk niet naar het systeemconfiguratieprofiel kon worden gekopieerd. (#9448)
* In Microsoft Excel gebruikt NVDA opnieuw de vertaalde melding bij het melden van de locatie van samengevoegde cellen. (#9471)

## 2019.1

Hoogtepunten in deze versie zijn prestatieverbeteringen bij het gebruik van zowel Microsoft Word als Excel, stabiliteits- en beveiligingsverbeteringen zoals ondersteuning voor add-ons met informatie over versiecompatibiliteit en vele andere probleemoplossingen.

Houd er rekening mee dat aangepaste appModules, globalPlugins en brailleleesregel- en synthesizer drivers vanaf deze versie van NVDA niet langer automatisch worden geladen vanuit de NVDA-gebruikersconfiguratiemap.
Deze dienen in plaats daarvan geïnstalleerd te worden als onderdeel van een NVDA add-on. Voor het ontwikkelen van code voor een add-on kan gebruik gemaakt worden van het ontwikkelaarskladblok (developer scratchpad) in de NVDA-gebruikersconfiguratiemap. Hiervoor dient de optie voor het ontwikkelaarskladblok ingeschakeld te zijn in de nieuwe categorie met geavanceerde instellingen van NVDA.
Deze wijzigingen zijn nodig om compatibiliteit van aangepaste code beter te waarborgen, zodat er geen problemen in NVDA ontstaan wanneer deze code incompatibel wordt met nieuwere versies.
Raadpleeg de lijst met wijzigingen verderop voor meer informatie hierover.

### Nieuwe Functies

* Nieuwe brailletabellen: Afrikaans, Arabisch 8 punt computerbraille, Arabisch graad 2, Spaans graad 2. (#4435, #9186)
* Een optie toegevoegd aan de muisinstellingen van NVDA om ervoor te zorgen dat NVDA situaties verwerkt waarin de muis wordt bestuurd door een andere applicatie. (#8452)
 * Hierdoor kan NVDA de muis volgen wanneer een systeem op afstand wordt bediend met behulp van TeamViewer of andere afstandsbedieningssoftware.
* De `--enable-start-on-logon` commandoregelparameter is toegevoegd zodat stille installaties van NVDA dusdanig geconfigureerd kunnen worden dat NVDA wel of niet start tijdens Windows aanmelding. Specificeer true om te starten op het aanmeldscherm of false om dit niet te doen. Wanneer --enable-start-on-logon niet gespecificeerd is, zal NVDA standaard starten tijdens Windows aanmelding, tenzij dit tijdens een eerdere installatie uitgeschakeld was. (#8574)
* Het is mogelijk om de logfuncties van NVDA uit te schakelen door het niveau van loggen in te stellen op "uitgeschakeld" in de categorie met Algemene instellingen. (#8516)
* De aanwezigheid van formules in -spreadsheets in LibreOffice en Apache OpenOffice wordt nu gemeld. (#860)
* In Mozilla Firefox en Google Chrome meldt de bladermodus nu het geselecteerde item in keuzelijsten en boomstructuren.
 - Dit werkt in Firefox 66 en later.
 - Dit werkt niet voor bepaalde keuzelijsten (HTML select elementen) in Chrome.
* Vroege ondersteuning voor apps zoals Mozilla Firefox op computers met ARM64-processors (bijvoorbeeld Qualcomm Snapdragon). (#9216)
* Er is een nieuwe geavanceerd categorie toegevoegd aan het dialoogvenster Instellingen van NVDA, inclusief een optie om NVDA's nieuwe ondersteuning voor Microsoft Word uit te proberen via de Microsoft UI Automation API. (#9200)
* Ondersteuning toegevoegd voor de grafische weergave in Windows Schijfbeheer. (#1486)
* Ondersteuning toegevoegd voor Handy Tech Connect Braille en Basic Braille 84. (#9249)

### Veranderingen

* Liblouis braillevertaler bijgewerkt naar versie 3.8.0. (#9013)
* Add-on-auteurs kunnen nu een minimaal vereiste NVDA-versie afdwingen voor hun add-ons. NVDA zal weigeren een add-on te installeren of te laden waarvan de minimaal vereiste NVDA-versie hoger is dan de huidige NVDA-versie. (#6275)
* Add-on-auteurs kunnen nu de versie van NVDA specificeren waarmee de add-on als laatste is getest. Als een add-on alleen getest is met een versie van NVDA ouder dan de huidige versie, weigert NVDA de add-on te installeren of te laden. (#6275)
* Deze versie van NVDA staat het installeren en laden van add-ons toe die nog geen gegevens over de Minimale en Laatst Getestte NVDA-versie bevatten. Het upgraden naar toekomstige versies van NVDA (bijv. 2019.2) zou er echter automatisch voor kunnen gaan zorgen dat deze oudere add-ons worden uitgeschakeld.
* De opdracht om de muis naar het huidige navigatorobject te verplaatsen, is nu beschikbaar in Microsoft Word evenals voor UIA-besturingselementen, waaronder Microsoft Edge. (#7916, #8371)
* Het melden van tekst onder de muis is verbeterd binnen Microsoft Edge en andere UIA-applicaties. (#8370)
* Wanneer NVDA wordt gestart met de opdrachtregelparameter `--portable path', wordt het opgegeven pad automatisch ingevuld wanneer wordt geprobeerd een draagbare kopie van NVDA te maken met behulp van het NVDA-menu. (#8623)
* Het pad naar de Noorse brailletabel is bijgewerkt voor gebruik van de standaard uit het jaar 2015. (#9170)
* Bij navigeren op basis van een alinea (control + pijl omhoog of omlaag) of bij tabelnavigatie(control + alt + pijltjestoetsen), wordt de aanwezigheid ​​van spelfouten niet langer gemeld, zelfs als NVDA is geconfigureerd om deze automatisch te melden. Dit komt doordat alinea's en tabelcellen vrij omvangrijk kunnen zijn en het detecteren van spelfouten in sommige toepassingen erg veel tijd kan kosten. (#9217)
* NVDA laadt niet langer automatisch aangepaste appModules, globalPlugins en brailleleesregel- en synthesizer drivers uit de NVDA-gebruikersconfiguratiemap. Deze code moet in plaats daarvan worden gedistribueerd als een add-on met de juiste versiegegevens, zodat incompatibele code niet wordt uitgevoerd door huidige versies van NVDA. (#9238)
 * Ontwikkelaars die code dienen te testen terwijl deze wordt ontwikkeld, kunnen NVDA's ontwikkelaarskladblokmap inschakelen via de categorie geavanceerd in de NVDA-instellingen. Na het inschakelen kan code geplaatst worden in de map 'scratchpad' in de NVDA-gebruikersconfiguratiemap.
* Bij het gebruik van de Nederlandse taal wordt de punt nu alleen geïnterpreteerd als scheidingsteken voor duizendtallen wanneer de punt wordt gevolgd door 3 cijfers. Voorheen werd een punt tussen cijfers altijd geïnterpreteerd als een cijfergroeperingsteken.

### Opgeloste Problemen

* Bij gebruik van de OneCore spraaksynthesizer met de Windows 10 april 2018 update en nieuwer, worden er niet langer grote stukken stilte toegevoegd in de spraak. (#8985)
* Bij het navigeren per karakter in invoervelden voor platte tekst (zoals Kladblok) of bladermodus, worden 32-bits emoji-tekens die bestaan uit twee UTF-16 code points (zoals 🤦) nu correct gelezen. (#8782)
* Het dialoogvenster om het herstarten van NVDA te bevestigen na het wijzigen van de interfacetaal is verbeterd. De tekst en de knoplabels zijn nu beknopter en minder verwarrend. (#6416)
* Als een spraaksynthesizer van een derde partij niet kan worden geladen, zal NVDA bij gebruik van Windows 10 terugvallen op de Windows OneCore spraaksynthesizer in plaats van espeak. (#9025)
* Het item "Welkomstvenster" in het NVDA-menu is niet langer zichtbaar . (#8520)
* Bij gebruik van tab of snelnavigatie in bladermodus worden legenda's op tabbladen nu consequenter gemeld. (#709)
* NVDA zal nu selectiewijzigingen aankondigen voor bepaalde tijdkiezers, zoals in de app Alarmen en klok in Windows 10. (#5231)
* In het Actiecentrum van Windows 10 zal NVDA statusmeldingen aankondigen bij het veranderen van snelle acties zoals helderheid en Concentratiehulp. (#8954)
* In het Actiecentrum in de Windows 10 oktober 2018 Update en ouder, zal NVDA de snelle actie voor helderheid herkennen als een knop in plaats van een schakelknop. (#8845)
* NVDA is opnieuw in staat om de cursor te volgen en verwijderde karakters te melden in de Microsoft Excel invoervelden voor ga naar en zoeken. (#9042)
* Een zeldzame crash in de bladermodus in Firefox is opgelost. (#9152)
* NVDA heeft niet langer moeite met het melden van de focus voor sommige besturingselementen in het lint van Microsoft Office 2016 wanneer dit is samengevouwen.
* NVDA heeft niet langer moeite met het melden van de voorgestelde contactpersoon bij het invoeren van adressen in nieuwe berichten in Outlook 2016. (#8502)
* De laatste cursorroutingstoetsen op 80-cellige leesregels van Eurobraille verplaatsen de cursor niet langer naar een positie aan of net na het begin van de brailleleesregel. (#9160)
* Tabelnavigatie is opnieuw beschikbaar in de conversatieweergave van Mozilla Thunderbird. (#8396)
* In Mozilla Firefox en Google Chrome werkt het overschakelen naar de focusmodus nu correct voor bepaalde keuzelijsten en boomstructuren (waarbij de keuzelijst/boomstructuur niet zelf de focus kan krijgen, maar de items daarin wel). (#3573, #9157)
* Bladermodus is standaard correct ingeschakeld bij het lezen van berichten in Outlook 2016/365 als de experimentele UI Automation-ondersteuning van NVDA wordt gebruikt voor Word-documenten. (#9188)
* NVDA zal nu minder snel dusdanig bevriezen dat uitloggen uit uw huidige Windows-sessie de enige manier is om te ontsnappen. (#6291)
* Wanneer in de Windows 10 oktober 2018 update en nieuwer de geschiedenis van het klembord in de cloud wordt geopend als het klembord leeg is, meldt NVDA de klembordstatus. (#9103)
* Wanneer er in de Windows 10 oktober 2018 update en nieuwer wordt gezocht naar emoji in het emoji-paneel, meldt NVDA het bovenste zoekresultaat. (#9105)
* NVDA bevriest niet langer in het hoofdvenster van Oracle VirtualBox 5.2 en nieuwer. (#9202)
* De responsiviteit in Microsoft Word bij het navigeren per regel, alinea of ​​tabelcel kan in sommige documenten aanzienlijk zijn verbeterd. Een herinnering dat u Microsoft Word voor de beste prestaties dient in te stellen op de conceptweergave met alt + v, p na het openen van een document. (#9217)
* In Mozilla Firefox en Google Chrome worden lege berichten (ARIA alerts) niet langer gemeld. (#5657)
* Aanzienlijke prestatieverbeteringen bij het navigeren door cellen in Microsoft Excel, met name wanneer de spreadsheet opmerkingen en/of keuzelijsten voor validatie bevat. (#7348)
* Het is niet langer nodig om het direct bewerken in cellen uit te schakelen in de opties van Microsoft Excel om met NVDA toegang te krijgen tot het invoerveld voor celbewerking in Excel 2016/365. (#8146).
* Een bevriezingsprobleem opgelost in Firefox dat soms zichtbaar werd wanneer snelnavigatie gebruikt werd om te navigeren tussen oriëntatiepunten terwijl de Enhanced Aria add-on gebruikt werd. (#8980)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2018.4.1

Deze versie lost een crash op bij het opstarten wanneer de taal van de NVDA gebruikersinterface is ingesteld op Aragonees. (#9089)

## 2018.4

Hoogtepunten in deze versie zijn prestatieverbeteringen in recente Mozilla Firefox versies, het uitspreken van emoji door alle synthesizers, het melden van beantwoord/doorgestuurd voor berichten in Outlook, het melden van de afstand tussen de cursor en de rand van een Microsoft Word pagina, en vele probleemoplossingen.

### Nieuwe Functies

* Nieuwe brailletabellen: Chinees (China, Mandarijn) graden 1 en 2. (#5553)
* De status beantwoord / doorgestuurd wordt nu gemeld voor e-mails in de Microsoft Outlook berichtenlijst. (#6911)
* NVDA is nu in staat om beschrijvingen te lezen van emoji en andere tekens die deel uitmaken van de Unicode Common Locale Data Repository. (#6523)
* In Microsoft Word kan de afstand tussen de cursor en de linker- en bovenrand van de pagina gemeld worden bij het indrukken van NVDA+numpadDelete. (#1939)
* In Google Sheets met brailleondersteuning ingeschakeld, meldt NVDA niet langer 'geselecteerd' voor iedere cel bij het verplaatsen van de focus tussen cellen. (#8879)
* Ondersteuning toegevoegd voor Foxit Reader en Foxit Phantom PDF. (#8944)
* Ondersteuning toegevoegd voor de DBeaver database tool. (#8905)

### Veranderingen

* "Helpbalonnen melden" in de instellingen voor objectweergave is hernoemd naar "Notificaties melden" om aan te geven dat deze optie ook het melden van toast-notificaties in Windows 8 en nieuwer omvat. (#5789)
* In de NVDA toetsenbordinstellingen worden de selectievakjes voor het in- of uitschakelen van de NVDA_toetsen nu weergegeven in een lijst in plaats van als aparte selectievakjes. 
* NVDA zal niet langer overbodige informatie presenteren bij het lezen van de klok in de systeembalk bij sommige versies van Windows. (#4364)
* Liblouis braillevertaler bijgewerkt naar versie 3.7.0. (#8697)
* eSpeak-ng is bijgewerkt naar commit 919f3240cbb.

### Opgeloste Problemen

* In Outlook 2016/365 worden de categorie en vlagstatus nu gemeld voor berichten. (#8603)
* Wanneer de taal van NVDA is ingesteld op Kirgyzisch, Mongools of Macedonisch wordt er niet langer een waarschuwing weergegeven dat de taal niet ondersteund wordt door het besturingssysteem. (#8064)
* Het verplaatsen van de muis naar het navigatorobject zal de muis nu veel accurater verplaatsen naar de bladermoduspositie in Mozilla Firefox, Google Chrome en Acrobat Reader DC. (#6460)
* De interactie met vervolgkeuzelijsten op het web in Firefox, Chrome en Internet Explorer is verbeterd. (#8664)
* Bij gebruik met de Japanse versie van Windows XP of Vista geeft NVDA nu zoals verwacht de systeemvereisten weer. (#8771)
* Prestatieverbeteringen bij het navigeren binnen lange pagina's met een grote hoeveelheid dynamische wijzigingen in Mozilla Firefox. (#8678)
* Er zijn niet langer lettertypeattributen zichtbaar in braille wanneer deze zijn uitgeschakeld in de instellingen voor documentopmaak. (#7615)
* NVDA no longer fails to track focus in File Explorer and other applications using UI Automation when another app is busy (such as batch processing audio). (#7345)
* In ARIA menu's op het web wordt de escape-toets nu doorgestuurd naar het menu, waardoor de focusmodus niet langer onvoorwaardelijk wordt uigeschakeld. (#3215)
* Bij het lezen van berichten in de nieuwe webinterface van GMail wordt bij het gebruiken van snelnavigatie niet langer de volledige inhoud gemeld na het element waar naartoe genavigeerd is. (#8887)
* Na het updaten van NVDA zullen browsers zoals Firefox en google Chrome niet langer crashen, en zal bladermodus updates blijven weergeven in momenteel geladen documenten. (#7641) 
* NVDA meldt niet langer meerdere malen klikbaar op een rij bij het navigeren door klikbare inhoud. (#7430)
* Invoerhandelingen uitgevoerd op baum Vario 40 brailleleesregels worden opnieuw correct afgehandeld. (#8894)
* In Google Slides met Mozilla Firefox zal NVDA niet langer geselecteerde tekst melden bij ieder element dat de focus krijgt. (#8964)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2018.3.2

Deze versie lost een probleem op dat een crash in Google Chrome veroorzaakte bij het navigeren tussen tweets op [www.twitter.com](http://www.twitter.com). (#8777)

## 2018.3.1

Deze versie lost een kritiek probleem op in NVDA dat ervoor zorgde dat 32-bit versies van Mozilla Firefox konden crashen. (#8759)

## 2018.3

Hoogtepunten in deze versie zijn het automatisch detecteren van verschillende brailleleesregels, ondersteuning voor nieuwe Windows 10 functies waaronder het Windows 10 Emoji invoerpaneel, en veel aanvullende probleemoplossingen.

### Nieuwe Functies

* NVDA meldt nu grammaticafouten wanneer zij correct worden aangeboden op webpagina's in Mozilla Firefox en Google Chrome. (#8280)
* Inhoud in webpagina's die is aangemerkt als ingevoegd of verwijderd, wordt nu als zodanig gemeld in Google Chrome. (#8558)
* Ondersteuning toegevoegd voor BrailleNote QT en Apex BT's scrollwiel wanneer BrailleNote wordt gebruikt als een brailleleesregel met NVDA. (#5992, #5993)
* Scripts toegevoegd voor het melden van verstreken en totale tijd voor het huidige nummer in Foobar2000. (#6596)
* Het symbool voor de Mac command-toets (⌘) wordt nu gemeld door iedere synthesizer bij het lezen van tekst. (#8366)
* Aangepaste rollen (roles) via het aria-roledescription attribuut worden nu ondersteund in alle web browsers. (#8448)
* Nieuwe brailletabbellen: Tsjechisch 8 punt, Centraal-Koerdisch, Esperanto, Hongaars, Zweeds 8 punt computerbraille. (#8226, #8437)
* Ondersteuning toegevoegd voor het automatisch herkennen van brailleleesregels op de achtergrond. (#1271)
 * ALVA, Baum/HumanWare/APH/Orbit, Eurobraille, Handy Tech, Hims, SuperBraille en HumanWare BrailleNote en Brailliant BI/B leesregels worden op dit moment ondersteund.
 * U kunt deze functie activeren door het selecteren van de optie automatisch in de lijst met leesregels in het dialoogvenster "selecteer brailleleesregel".
 * Bekijk de documentatie voor meer details.
* Ondersteuning toegevoegd voor moderne invoermethoden die geïntroduceerd zijn in recente versies van Windows 10. Deze omvatten het emoji-paneel (Fall Creators Update), dicteren (Fall Creators Update), hardwaretoetsenbord invoersuggesties (April 2018 Update), en het cloud klembord (October 2018 Update). (#7273)
* Inhoud die gemarkeerd is als blokcitaat met gebruik van ARIA (role blockquote) wordt nu ondersteund in Mozilla Firefox 63. (#8577)

### Veranderingen

* De lijst met beschikbare talen in de algemene instellingen van NVDA wordt nu gesorteerd op taal in plaats van op basis van ISO 639 codes. (#7284)
* Standaardtoewijzingen toegevoegd voor alt shift tab en windows tab voor alle ondersteunde Freedom Scientific brailleleesregels. (#7387)
* Voor ALVA BC680 en protocol converter leesregels is het nu mogelijk om verschillende functies toe te wijzen aan de linker en rechter smart pad-, duim- en etouch toetsen. (#8230)
* Voor ALVA BC6 leesregels zal de toetsencombinatie sp2+sp3 de huidige datum en tijd melden, terwijl sp1+sp2 nu de Windows-toets emuleert. (#8230)
* De gebruiker wordt bij het starten van NVDA nu eenmalig gevraagd of hij/zij ermee akkoord gaat dat NVDA gebruiksstatistieken verstuurd naar NV Access bij het automatisch controleren op updates. (#8217)
* Wanneer er gecontroleerd wordt op updates en de gebruiker ermee akkoord is gegaan dat er gebruiksstatistieken worden verstuurd naar NV Access, zal NVDA nu de naam van de huidige synthesizer driver en brailleleesregel versturen om te helpen bij een betere prioritering van toekomstig werk aan deze drivers. (#8217)
* Liblouis braillevertaler bijgewerkt naar versie 3.5.0. (#8365)
* Het pad naar de juiste Russische 8 punt brailletabel is bijgewerkt. (#8446)
* eSpeak-ng is bijgewerkt naar 1.49.3dev commit 910f4c2 (#8561)

### Opgeloste Problemen

* Toegankelijke labels voor elementen in Google Chrome worden nu directer gemeld in bladermodus wanneer het label zelf geen deel uitmaakt van de inhoud. (#4773)
* Notificaties worden nu ondersteund in Zoom. Dit omvat notificaties voor dempen/dempen opheffen en inkomende berichten.(#7754)
* Het wisselen van te tonen focuscontext in braille zorgt er in de bladermodus niet langer voor dat de braille-uitvoer de cursor niet volgt. (#7741)
* ALVA BC680 brailleleesregels hebben niet langer sporadisch moeite met initialiseren. (#8106)
* In de standaardsituatie zullen ALVA BC6 leesregels niet langer geëmuleerde systeemtoetsen uitvoeren bij het indrukken van toetsencombinaties die sp2+sp3 omvatten en gekoppeld zijn aan interne functionaliteit van de leesregel. (#8230)
* Het indrukken van sp2 op een ALVA BC6 leesregel om de alt-toets te emuleren werkt nu daadwerkelijk zoals vermeld. (#8360)
* NVDA meldt niet langer overbodig wijzigingen van de toetsenbordindeling. (#7383, #8419)
* Het volgen van de muis is nu stukken accurater in Kladblok en andere invoervelden voor platte tekst wanneer er sprake is van een document met meer dan 65535 karakters. (#8397)
* NVDA zal meer dialoogvensters herkennen in Windows 10 en andere moderne applicaties. (#8405)
* In de Windows 10 October 2018 Update en Windows Server 2019 en nieuwer zal NVDA niet langer moeite hebben met het volgen van de systeemfocus wanneer een applicatie vastloopt of het systeem overspoelt met gebeurtenissen. (#7345, #8535)
* Gebruikers worden nu geïnformeerd bij een poging tot het lezen of kopiëren van een lege statusbalk. (#7789)
* Een probleem opgelost waarbij de niet ingeschakelde staat van elementen niet door de spraak uitgesproken werd wanneer het element eerder gedeeltelijk ingeschakeld was. (#6946)
* In de lijst met talen in de algemene instellingen van NVDA wordt de naam van de Birmese taal nu correct weergegeven onder Windows 7. (#8544)
* In Microsoft Edge zal NVDA nu notificaties melden zoals over de beschikbaarheid van de leesweergave en de voortghang van het laden van pagina's. (#8423)
* Bij het navigeren naar een lijst op het web meldt NVDA nu het label van de lijst wanneer de web-auteur een label heeft ingesteld. (#7652)
* Bij het handmatig toewijzen van functies aan invoerhandelingen voor een bepaalde leesregel worden deze nu altijd weergegeven als toegewezen aan die leesregel. In het verleden werden ze altijd weergegeven alsof ze waren toegewezen aan de actieve leesregel. (#8108)
* De 64-bit-versie van Media Player Classic wordt nu ondersteund. (#6066)
* Diverse verbeteringen in de braille-ondersteuning in Microsoft Word met UI Automation ingeschakeld:
 * Zoals ook bij andere invoervelden met meerdere regels het geval is, wordt bij documenten het eerste karakter van het document nu aan het begin van de leesregel weergegeven wanneer de cursor zich aan het begin van het document bevindt. (#8406)
 * De in eerdere versies overdreven focusweergave is gereduceerd voor zowel spraak als braille wanneer een Word-document de focus krijgt. (#8407)
 * Cursor routing in braille werkt nu correct bij gebruik in een lijst in een Word-document. (#7971)
 * Nieuw ingevoegde opsommingstekens/nummering in een Word-document worden correct gemeld voor zowel braille als spraak. (#7970)
* In Windows 10 1803 en nieuwer is het nu mogelijk om add-ons te installeren wanneer de optie "Gebruik Unicode UTF-8 voor wereldwijde taalondersteuning" is ingeschakeld. (#8599)
* NVDA maakt het gebruik van iTunes 12.9 en nieuwer niet langer compleet onmogelijk. (#8744)

### Veranderingen voor ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2018.2.1

Deze versie bevat bijgewerkte vertalingen omdat op het laatste moment een functie die problemen opleverde werd verwijderd.

## 2018.2

Hoogtepunten in deze versie zijn ondersteuning voor tabellen in Kindle voor PC, ondersteuning voor HumanWare BrailleNote Touch en BI14 brailleleesregels, verbeteringen aan zowel Onecore als Sapi5 spraaksynthesizers, verbeteringen in Microsoft Outlook en veel meer.

### Nieuwe Functies

* Samengevougde cellen in rijen en kolommen van tabellen worden nu gemeld in spraak en braille. (#2642)
* NVDA tabelnavigatiecommando's worden nu ondersteund in Google Docs (met Braillemodus ingeschakeld). (#7946)
* In Kindle voor PC is er de mogelijkheid om tabellen te lezen en er tussen te navigeren. (#7977)
* Ondersteuning voor de BrailleNote touch en Brailliant BI 14 brailleleesregels via zowel USB als bluetooth. (#6524)
* In de Windows 10 Fall Creators Update en nieuwer kan NVDA nu notificaties melden van apps zoals Rekenmachine en Windows Store. (#8045)
* Nieuwe brailletabellen: Litouws 8 punts, Oekraïns, Mongools graad 2. (#7839)
* Een script toegevoegd om opmaak te melden van de tekst onder een specifieke braillecel. (#7106)
* Bij het updaten van NVDA is er nu de mogelijkheid om de installatie van de update uit te stellen tot een later gekozen moment. (#4263) 
* Nieuwe talen: Mongools, Zwitsers Duits.
* Het is nu mogelijk om control, shift, alt, windows en NVDA in- en uit te schakelen vanaf uw brailletoetsenbord en deze modifiers te combineren met brailleinvoer (bijv. het indrukken van control+s). (#7306) 
 * U kunt deze nieuwe virtuele modifierschakelaars toewijzen met de commando's die te vinden zijn onder Geëmuleerde systeemtoetsen in het dialoogvenster invoerhandelingen.
* Herstelde ondersteuning voor de leesregels Handy Tech Braillino en Modular (met oude firmware). (#8016)
* Datum en tijd voor ondersteunde Handy Tech leesregels (zoals Active Braille en Active Star) worden nu automatisch gesynchroniseerd door NVDA als ze meer dan vijf seconden uit elkaar lopen. (#8016)
* Er kan nu een invoerhandeling toegewezen worden om triggers voor configuratieprofielen tijdelijk uit te schakelen. (#4935)

### Veranderingen

* De statuskolom in het venster voor add-ons beheren is zodanig gewijzigd dat deze nu aangeeft of de add-on in- of uitgeschakeld is in plaats van werkend of onderbroken. (#7929)
* Liblouis braillevertaler bijgewerkt naar 3.5.0. (#7839)
* De Litouwse brailletabel is hernoemd naar Litouws 6 punts om verwarring te vermijden met de nieuwe 8 punts tabel. (#7839)
* De tabellen Frans (Canada) graad 1 en graad 2 zijn verwijderd. In plaats daarvan zullen resp. de Frans (unified) 6 punts computerbraille en Graad 2 tabellen worden gebruikt. (#7839)
* De secundaire cursorroutingtoetsen op Alva BC6, EuroBraille en Papenmeier brailleleesregels melden nu informatie over de opmaak voor de tekst onder de braillecel behorend bij die toets. (#7106)
* Brailletabellen voor kortschrift schakelen nu terug naar onverkort braille in niet-bewerkbare gevallen (d.w.z. bij besturingselementen zonder cursor of in bladermodus). (#7306)
* NVDA is nu minder breedsprakig voor afspraken of tijdsloten in de Outlok agenda die een hele dag betreffen. (#7949)
* Alle voorkeuren van NVDA bevinden zich nu gegroepeerd in één instellingenvenster onder NVDA-menu -> Opties -> Instellingen, in plaats van verspreid in een veelvoud aan dialoogvensters. (#7302)
* De standaard spraaksynthesizer bij het gebruik van Windows 10 is nu oneCore stemmen in plaats van eSpeak. (#8176)

### Opgeloste Problemen

* NVDA heeft niet langer problemen bij het lezen van elementen die de focus hebben in het Microsoft Account inlogscherm in instellingen na het invullen van een e-mailadres. (#7997)
* NVDA heeft niet langer moeite met het lezen van de paginana het teruggaan naar een vorige pagina in Microsoft Edge. (#7997)
* Op het windows 10 inlogscherm spreekt NVDA niet langer het laatst ingevoerde karakter uit van de pincode bij het ontgrendelen van het scherm. (#7908)
* IN Chrome en Firefox worden Labels van selectievakjes en keuzerondjes niet langer twee keer gemeldbij het navigeren met tab of snelnavigatie in de bladermodus. (#7960)
* aria-current waarden met de waarde false worden nu daadwerkelijk behandeld als false in plaats van true. (#7892).
* Het laden van de driver voor Windows Onecore stemmen gaat niet langer verkeerd wanneer de geconfigureerde stem verwijderd is. (#7999)
* Het wijzigen van stemmen voor de Windows Onecore stemmen driver is nu een stuk sneller. (#7999)
* De incorrecte uitvoer voor verschillende brailletabellen, waaronder hoofdletters in 8 punts Deens kortschrift braille, is gecorrigeerd. (#7526, #7693)
* NVDA is nu in staat om meerdere soorten opsommingstekens te melden in Microsoft Word. (#6778)
* Het script voor het melden van opmaak zal de positie van de leescursor niet langer verplaatsen. Daarom zal het meerdere keren indrukken van een toegewezen invoerhandeling niet langer verschillende resultaten geven. (#7869)
* Het is niet langer mogelijk om kortschrift braille in te voeren in situaties waarin dit niet ondersteund wordt (d.w.z. er worden niet langer complete woorden naar het systeem gestuurd buiten tekstinhoud en in de bladermodus). (#7306)
* Problemen in de stabiliteit van de verbinding met Handy Tech Easy Braille en Braille Wave leesregels zijn opgelost. (#8016)
* Onder Windows 8 en nieuwer zal NVDA niet langer "onbekend"melden wanneer het Windows+X snelmenu wordt geopend en items in dit menu worden geselecteerd. (#8137)
* Modelspecifieke toewijzingen aan toetsen voor Hims leesregels functioneren nu daadwerkelijk zoals vermeld in de gebruikershandleiding. (#8096)
* NVDA zal nu proberen om problemen met COM-registraties op het systeem op te lossen die onder andere Firefox en Internet Explorer ontoegankelijk kunnen maken en resulteren in het veelvoudig melden van "onbekend". (#2807)
* Er is een oplossing gerealiseerd voor een probleem in Windows Taakbeheer waardoor NVDA gebruikers niet in staat stelde om de inhoud van specifieke procesdetails te bekijken. (#8147)
* Nieuwere Microsoft SAPI5 stemmen hebben niet langer last van vertraging aan het einde van spraakuitvoer, waardoor het navigeren met deze stemmen veel efficiënter verloopt. (#8174)
* NVDA meldt niet langer links-naar-rechts- en rechts-naar-links-markeringen in braille of bij het navigeren per karakter in spraak wanneer de klok wordt bekeken in recente versies van Windows. (#5729)
* Detectie van de scrolltoetsen op Hims Smart Beetle leesregels is opnieuw niet meer onbetrouwbaar. (#6086)
* In sommige besturingselementen voor tekstinvoer, voornamelijk in Delphi-applicaties, is de informatie over bewerken en navigeren een stuk betrouwbaarder dan voorheen. (#636, #8102)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2018.1.1

Dit is een speciale versie van NVDA die een probleem oplost in de driver voor de Onecore Windows spraaksynthesizer die zorgde voor het afspelen van de spraak op een te hoge toonhoogte bij gebruik vanaf de Windows 10 April Update (1803). (#8082)

## 2018.1

Hoogtepunten in deze versie zijn ondersteuning voor grafieken in Microsoft Word en PowerPoint, toegevoegde ondersteuning voor brailleleesregels waaronder Eurobraille en de Optelec protocol converter, verbeterde ondersteuning voor Hims en Optelec brailleleesregels, prestatieverbeteringen voor Mozilla Firefox 58 en nieuwer, en nog veel meer.

### Nieuwe Functies

* Het is nu mogelijk om te werken met grafieken in Microsoft Word en Microsoft PowerPoint op een vergelijkbare manier als in Microsoft Excel. (#7046)
 * In Microsoft Word: navigeer in bladermodus naar een ingebedde grafiek en druk op enter om interactie met deze grafiek te starten.
 * In Microsoft PowerPoint tijdens het bewerken van een dia: tab naar een grafiekobject en druk op enter of spatie voor interactie met de grafiek.
 * OM de interactie met een grafiek af te breken, druk op escape.
* Nieuwe taal: Kirgizisch.
* Ondersteuning toegevoegd voor VitalSource Bookshelf. (#7155)
* Ondersteuning toegevoegd voor de Optelec protocol converter, een apparaat dat iemand in staat stelt om een Braille Voyager of Satellite leesregel aan te sturen via het ALVA BC6 communicatieprotocol. (#6731)
* Het is nu mogelijk om braille-invoer te gebruiken met een ALVA 640 Comfort brailleleesregel. (#7733) 
 * De braille-invoerfunctionaliteit van NVDA kan gebruikt worden met deze en andere BC6 leesregelsmet firmware 3.0.0 en nieuwer.
* Vroege ondersteuning toegevoegd voor Google Sheets met de braille-modus ingeschakeld. (#7935)
* Ondersteuning voor Eurobraille Esys, Esytime en Iris brailleleesregels. (#7488)

### Veranderingen

* De drivers voor HIMS Braille Sense/Braille EDGE/Smart Beetle en Hims Sync Braille leesregels zijn vervangen door één driver. De nieuwe driver wordt automatisch geactiveerd voor voormalige syncBraille driver gebruikers. (#7459) 
 * Sommige toetsen, met name de scrolltoetsen, zijn opnieuw toegewezen om beter aan te sluiten bij hoe deze toetsen gebruikt worden binnen producten van Hims. Raadpleeg de gebruikershandleiding voor meer details.
* Bij het typen op een schermtoetsenbord via aanraakinteractie is het nu standaard zo dat u dubbel moet tikken op een toets om deze te activeren, op de zelfde manier waarop u een ander element zou activeren. (#7309)
 * Om de bestaande modus ("direct typen met aanraken") te gebruiken waarbij het simpelweg optillen van uw vinger genoeg is om de toets te activeren, moet u deze optie inschakelen in het nieuwe instellingenvenster aanraakinteractie in het optiesmenu.
* Het is niet langer nodig om braille expliciet te koppelen aan de focus of de leescursor, aangezien dit vanaf nu standaard automatisch gebeurd. (#2385) 
 * Houd er rekening mee dat het koppelen aan de leescursor alleen gebeurt bij het gebruik van een commando voor het bedienen van de leescursor of objectnavigatie. Scrollen activeert dit nieuwe gedrag dus niet.

### Opgeloste Problemen

* Het tonen van meldingen in de bladermodus, zoals het bekijken van opmaakinformatie door middel van het twee keer snel indrukken van NVDA+f, gaat niet langer verkeerd wanneer NVDA geïnstalleerd is in een map waarvan de naam niet-ASCII-tekens bevat. (#7474)
* De focus wordt opnieuw correct hersteld bij het terugkeren naar Spotify vanuit een andere applicatie. (#7689)
* In de Windows 10 Fall Creaters Update gaat het bijwerken van NVDA niet langer verkeerd wanneer Beheerde maptoegang is ingeschakeld vanuit het Windows Defender beveiligingscentrum. (#7696)
* Het detecteren van de scrolltoetsen van Hims Smart Beetle leesregels is niet langer onbetrouwbaar. (#6086)
* Een lichte prestatieverbetering bij het weergeven van grote hoeveelheden inhoud in Mozilla Firefox 58 en nieuwer. (#7719)
* In Microsoft Outlook veroorzaakt het lezen van tabellen niet langer fouten. (#6827)
* Invoerhandelingen van brailleleesregels die modifier-toetsen emuleren, kunnen nu ook gecombineerd worden met andere geëmuleerde systeemtoetsen wanneer één van de invoerhandelingen specifiek is voor een bepaald model leesregel. (#7783)
* Bladermodus in Mozilla Firefox werkt nu naar behoren in pop-ups die getoond worden door extensies als LastPass en bitwarden. (#7809)
* NVDA loopt niet langer vast bij iedere focuswijziging wanneer Firefox of Chrome niet meer reageert, bijvoorbeeld vanwege een bevriezingsprobleem of vastloper. (#7818)
* In Twitter-clients zoals Chicken Nugget zal NVDA de laatste 20 karakters niet langer negeren bij het lezen van tweets met 280 karakters. (#7828)
* NVDA gebruikt nu de juiste taal voor het melden van symbolen bij het selecteren van tekst. (#7687)
* In recente versies van Office 365 is het opnieuw mogelijk om door Excel-grafieken te navigeren met de pijltjestoetsen. (#7046)
* In spraak- en braille-uitvoer worden de diverse statusindicatoren nu altijd in de zelfde volgorde getoond, ongeacht of ze positief of negatief zijn. (#7076)
* In apps zoals Windows 10 Mail heeft NVDA bij het gebruik van backspace niet langer problemen met het melden van verwijderde karakters. (#7456)
* Alle toetsen op de Hims Braille Sense Polaris leesregels werken nu zoals verwacht. (#7865)
* NVDA heeft niet langer problemen met starten onder bepaalde versies van Windows 7 vanwege een foutmelding over een interne api-ms dll. Opstartproblemen konden zich voordoen wanneer een bepaalde versie van de Visual Studio 2017 redistributables geÏnstalleerd was door een andere applicatie. (#7975) 

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2017.4

Hoogtepunten in deze versie zijn sterk verbeterde ondersteuning voor het web zoals standaard bladermodus voor dialoogvensters binnen websites, beter melden van labels van gegroepeerde velden in bladermodus, ondersteuning voor nieuwe Windows 10 technologieën zoals Windows Defender Application Guard en Windows 10 met ARM64, en automatisch melden van schermstand en batterijstatus.
Let op: deze versie van NVDA ondersteunt Windows XP en Windows Vista niet meer. De minimumvereiste voor NVDA is nu windows 7 met Service Pack 1.

### Nieuwe Functies

* In bladermodus is het nu mogelijk om voorbij/naar het begin van een oriëntatiepunt te springen met behulp van de commando's ga voorbij/naar het begin van een containerelement (komma/shift+komma). (#5482)
* In Firefox, Chrome en Internet Explorer omvat snelnavigatie naar invoer- en formuliervelden nu ook invoervelden met opmaakondersteuning (D.w.z. contentEditable). (#5534)
* In web browsers kan de elementenlijst nu formuliervelden en knoppen weergeven. (#588)
* Initiële ondersteuning voor Windows 10 op ARM64. (#7508)
* Vroege ondersteuning voor het lezen van en interactief navigeren door wiskundige inhoud voor Kindle boeken, mits deze inhoud toegankelijk is. (#7536)
* Ondersteuning toegevoegd voor Azardi e-book reader. (#5848)
* Bij het updaten van add-ons wordt nu versie-informatie gemeld. (#5324)
* Ondersteuning toegevoegd voor nieuwe commandoregelopties om een draagbare versie van NVDA aan te maken. (#6329)
* Ondersteuning voor Microsoft Edge toegevoegd wanneer dit draait binnen Windows Defender Application Guard (#7600)
* Wanneer NVDA gebruikt wordt op een laptop of tablet wordt het vanaf nu gemeld als er een adapter wordt aangesloten/losgekoppeld en als de schermstand wijzigt. (#4574, #4612)
* Nieuwe taal: Macedonisch.
* Nieuwe brailletabellen: Croatisch graad 1, Viëtnamees graad 1. (#7518, #7565)
* Ondersteuning toegevoegd voor de Handy Tech Actilino brailleleesregel. (#7590)
* Braille-invoer wordt nu ondersteund voor leesregels van Handy Tech. (#7590)

### Veranderingen

* Het miminimaal door NVDA ondersteunde besturingssysteem is nu Windows 7 met Service Pack 1, of Windows Server 2008 R2 met Service Pack 1. (#7546)
* Webdialoogvensters in Firefox en Chrome web browsers gebruiken nu automatisch bladermodus, tenzij binnen een webapplicatie. (#4493)
* In bladermodus meldt het gebruik van tab of snelnavigatiecommando's niet langer het verlaten van containers zoals lijsten en tabellen, waardoor navigatie efficiënter wordt. (#2591)
* In bladermodus voor Firefox en Chrome wordt nu de naam van formulierveldgroeperingen gemeld wanneer daarin genavigeerd wordt met snelnavigatie of tab. (#3321)
* In bladermodusomvat het snelnavigatiecommando voor ingebedde objecten (o en shift+o) nu zowel elementen van het type audio en video als met de aria roles application en dialog. (#7239)
* Espeak-ng is bijgewerkt (naar commit 01919cd48a566cdf34347784b2e74554b376e900), wat enkele problemen oplost met het produceren van release builds. (#7385)
* Bij het derde keer activeren van het 'lees statusbalk' commando wordt de inhoud van de statusbalk naar het klembord gekopieerd. (#1785)
* Bij het toewijzen van invoerhandelingen voor een Baum leesregel is het nu mogelijk om specifieke toewijzingen te doen voor het model van de brailleleesregel die momenteel in gebruik is (bijv. VarioUltra of Pronto). (#7517)
* De sneltoets van het filterveld in de elementenlijst in bladermodus is gewijzigd van alt+f in alt+e. (#7569)
* Er is een niet toegewezen invoerhandeling toegevoegd voor bladermodus om het melden van lay-outtabellen snel in of uit te schakelen. U kunt deze optie vinden in de categorie bladermodus van het dialoogvenster Invoerhandelingen. (#7634)
* Liblouis braillevertaler bijgewerkt naar 3.3.0. (#7565)
* De sneltoets van het keuzerondje reguliere expressie in het dialoogvenster voor uitspraakwoordenboeken is gewijzigd van alt+r in alt+e. (#6782)
* De bestanden voor Stem-afhankelijke woordenboeken hebben vanaf nu een versienummer en zijn verplaatst naar de map 'speechDicts/voiceDicts.v1'. (#7592)
* Aanpassingen in versie-afhankelijke bestanden (gebruikersconfiguratie, stem-afhankelijke woordenboeken) worden niet langer opgeslagen wanneer NVDA gestart is vanuit het installatiebestand. (#7688)
* De Braillino, Bookworm en Modular (met oude firmware) brailleleesregels van Handy Tech worden niet langer standaard ondersteund. Installeer de Handy Tech Universele Driver en NVDA add-on om deze leesregels te gebruiken. (#7590)

### Opgeloste Problemen

* Links worden nu als zodanig weergegeven in braille in applicaties zoals Microsoft Word. (#6780)
* NVDA wordt niet langer merkbaar langzamer wanneer er veel tabbladen geopend zijn in Firefox of Chrome web browsers. (#3138)
* De cursorroutingtoetsen van de MDV Lilli brailleleesregel worden niet langer één cel te ver naar rechts geactiveerd. (#7469)
* In Internet Explorer en andere MSHTML-documenten wordt het HTML5 required attribuut nu ondersteund om de vereiste status van een formulierveld aan te geven. (#7321)
* Brailleleesregels worden nu bijgewerkt bij het typen van Arabische karakters in een WordPad-document dat links uitgelijnd is. (#511).
* Toegankelijke labels voor elementen in Mozilla Firefox worden nu gemeld in bladermodus wanneer het label geen deel uitmaakt van de inhoud. (#4773)
* In de windows 10 Creators Update heeft NVDA na een herstart niet langer problemen met het benaderen van Firefox. (#7269)
* Bij het starten van NVDA terwijl Mozilla Firefox de focus heeft, zou bladermodus nu opnieuw beschikbaar moeten zijn. Wanneer bladermodus nog niet werkt, is dit te verhelpen door met alt+tab uit en terug in het venster te navigeren. (#5758)
* Het is nu mogelijk om wiskundige inhoud te bekijken in Google Chrome op een systeem waarop Mozilla Firefox niet geïnstalleerd is. (#7308)
* In vergelijking met eerdere installaties van NVDA zouden het besturingssysteem en andere applicaties stabieler moeten zijn wanneer u NVDA direct start na de installatie, dus voor u het systeem herstart hebt. (#7563)
* Bij het gebruik van een commando voor tekstherkenning (bijv. NVDA+r) geeft NVDA nu een foutmelding in plaats van geen melding wanneer het navigatorobject verdwenen is. (#7567)
* De functionaliteit om terug te scrollen is hersteld voor Freedom Scientific brailleleesregels die een linker bumperbalk bevatten. (#7713)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2017.3

Hoogtepunten in deze versie zijn invoer van braille kortschrift, ondersteuning voor nieuwe Windows OneCore stemmen beschikbaar in Windows 10, ingebouwde ondersteuning voor Windows 10 OCR, en veel significante verbeteringen voor Braille en het web.

### Nieuwe Functies

* Een Braille-instelling is toegevoegd: "Meldingen voor onbepaalde tijd tonen". (#6669)
* In Microsoft Outlook berichtenlijsten meldt NVDA nu of een bericht een vlag heeft. (#6374)
* In Microsoft PowerPoint wordt nu het exacte soort vorm gemeld bij het bewerken van een slide (zoals driehoek, cirkel, video of pijl), in plaats van enkel "vorm". (#7111)
* Wiskundige inhoud (aangeboden als MathML) wordt nu ondersteund in Google Chrome. (#7184)
* NVDA kan nu spreken met de nieuwe Windows OneCore stemmen (ook bekend als Microsoft Mobile stemmen) inbegrepen in Windows 10. U vindt ze door Windows OneCore stemmen te selecteren in NVDA's Synthesizer dialoogvenster. (#6159)
* De bestanden van de gebruikersconfiguratie van NVDA kunnen nu worden opgeslagen in de local application data map. Dit wordt bepaald via een instelling in het register. Zie "Systeem-brede parameters" in de Gebruikershandleiding voor meer details. (#6812)
* In web browsers meldt NVDA nu placeholder-waarden voor velden (specificiek, aria-placeholder wordt nu ondersteund). (#7004)
* In Bladermodus voor Microsoft Word is het nu mogelijk naar spelfouten te navigeren via snelnavigatie (w en shift+w). (#6942)
* Ondersteuning toegevoegd voor besturingselementen voor datumselectie in dialoogvensters voor afspraken in Microsoft Outlook. (#7217)
* De momenteel geselecteerde suggestie wordt nu gemeld in Windows 10 Mail aan-/cc-velden en het Windows 10 Instellingen zoekveld. (#6241)
* Er wordt een geluid afgespeeld om aan te geven dat suggesties verschenen zijn in bepaalde zoekvelden in Windows 10 (Bijvoorbeeld het startscherm, instellingen zoeken, Windows 10 mail aan-/cc-velden). (#6241)
* NVDA meldt nu automatisch notificaties in Skype voor Business Desktop, zoals wanneer iemand met u een conversatie start. (#7281)
* NVDA meldt nu automatisch binnenkomende chatberichten in een Skype voor Business conversatie. (#7286)
* NVDA meldt nu automatisch notificaties in Microsoft Edge, zoals wanneer een download start. (#7281)
* U kunt nu ook braille typen in kortschrift op een brailleleesregel met een brailletoetsenbord. Dit omvat ook Nederlands literair braille. Zie de sectie Braille-invoer van de Gebruikershandleiding voor details. (#2439)
* U kunt nu Unicode braillekarakters invoeren via het brailletoetsenbord van een brailleleesregel door Unicode braille te selecteren als de invoertabel in Braille-instellingen. (#6449)
* Ondersteuning toegevoegd voor de SuperBraille brailleleesregel die wordt gebruikt in Taiwan. (#7352)
* Nieuwe brailletabellen: Deens 8 punts computer braille, Litouws, Persisch 8 punts computer braille, Persisch graad 1, Sloveens 8 punts computer braille. (#6188, #6550, #6773, #7367)
* Verbeterde Engels (V.S.) 8 punt computerbrailletabel, inclusief ondersteuning voor opsommingstekens, het euroteken en letters met accenten. (#6836)
* NVDA kan nu de OCR functionaliteit gebruiken die is ingebouwd in Windows 10 om de tekst in afbeeldingen of ontoegankelijke applicaties te herkennen. (#7361)
 * De taal kan worden ingesteld in het nieuwe dialoogvenster Windows 10 OCR in in de NVDA Opties.
 * Om de inhoud te herkennen van het huidige navigatorobject, druk NVDA+r.
 * Zie de sectie Inhoudherkenning van de Gebruikershandleiding voor verdere details.
* U kunt nu kiezen welke contextinformatie wordt getoond op een brailleleesregel als een object focus krijgt via de nieuwe instelling "Te tonen Focuscontext" in het dialoogvenster Braille-instellingen. (#217)
 * Bijvoorbeeld, de opties "Leesregel vullen voor contextveranderingen" en "Alleen bij terugscrollen" kunnen het werken met lijsten en menu's efficiënter maken, omdat de items niet continu van plaats veranderen op de leesregel.
 * Zie de sectie over de instelling "Te tonen Focuscontext" in de Gebruikershandleiding voor verdere details en voorbeelden.
* In Firefox en Chrome ondersteunt NVDA nu complexe dynamische grids zoals spreadsheets waar slechts een gedeelte van de inhoud geladen of weergegeven wordt (specifiek,, de attributen aria-rowcount, aria-colcount, aria-rowindex en aria-colindex die zijn ingevoerd in ARIA 1.1). (#7410)

### Veranderingen

* Er is een niet toegewezen invoerhandeling toegevoegd om NVDA op verzoek te herstarten. U kunt deze optie vinden in de categorie Diversen van het dialoogvenster Invoerhandelingen. (#6396)
* De toetsenbordindeling kan nu worden ingesteld in het welkomscherm van NVDA. (#6863)
* Veel meer soorten besturingselementen en bijbehorende status-indicatoren zijn afgekort voor braille. Ook oriëntatiepunten zijn afgekort. Zie "Braille-afkortingen voor besturingselementen, status-indicatoren en oriëntatiepunten" onder Braille in de Gebruikershandleiding voor een volledige lijst. (#7188, #3975)
* In het dialoogvenster Braille-instellingen zijn de lijsten van uitvoer- en invoertabellen nu alfabetisch gerangschikt. (#6113)
* liblouis braille translator bijgewerkt naar 3.2.0. (#6935)
* De standaard brailletabel is nu Uniforme Engelse Braillecode graad 1. (#6952)
* Standaard toont NVDA op een brailleleesregel nu enkel de delen van de inhoudsinformatie die gewijzigd zijn als een object focus krijgt. (#217)
 * Voorheen toonde het altijd zoveel mogelijk contextinformatie, ongeacht of u dezelfde contextinformatie eerder al zag.
 * U kunt terugkeren naar het oude gedrag door de nieuwe instelling "Te tonen Focuscontext" te wijzigen in "Leesregel altijd vullen" in het dialoogvenster Braille-instellingen.
* Bij gebruik van Braille kan de cursor geconfigureerd worden om een andere vorm aan te nemen, afhankelijk van of braille gekoppeld is aan de focus of de leescursor. (#7112)
* Het NVDA logo is bijgewerkt. Het bijgewerkte NVDA logo is een gestileerde mix van de letters NVDA in wit op een paarse achtergrond. Dit garandeeert dat het zichtbaar is tegen elke gekleurde achtergrond, en gebruikt het paars van het NV Access logo. (#7446)

### Opgeloste Problemen

* Bij bewerkbare elementen van het type div wordt in Chrome bladermodus het label niet langer gemeldt als zijnde de waarde. (#7153)
* Het indrukken van end terwijl u zich in bladermodus binnen een leeg Microsoft Word document bevindt, levert niet langer een foutmelding (runtime error) op. (#7009)
* Bladermodus wordt nu correct ondersteund in Microsoft Edge waar een document specifiek voorzien is van de ARIA role document. (#6998)
* In bladermodus kunt u nu selecteren of deselecteren tot het einde van de regel met shift+end, zelfs als de cursor op het laatste karacter van de regel staat. (#7157)
* Als een dialoogvenster een voortgangsbalk bevat, wordt de tekst van het dialoogvenster nu bijgewerkt in braille als de voortgangsbalk wijzigt. Dit betekent bijvoorbeeld dat u nu de resterende tijd kunt lezen in het dialoogvenster dat getoond wordt bij het downloaden van NVDA updates. (#6862)
* NVDA meldt vanaf nu selectiewijzigingen voor bepaalde Windows 10 vervolgkeuzelijsten, zoals Automatisch afspelen in Instellingen. (#6337).
* Er wordt niet langer overtollige informatie gemeld bij het invoeren van afspraken in Microsoft Outlook. (#7216)
* Pieptonen voor bepaalde NVDA dialoogvensters met voortgangsbalken (zoals voor het controleren op updates) worden nu alleen afgespeeld wanneer weergave van voortgangsbalken dusdanig is ingesteld dat pieptonen worden afgespeeld. (#6759)
* In Microsoft Excel 2003 en 2007 worden cellen weer gemeld bij het rondpijlen door een werkblad. (#7243)
* In de Windows 10 Creators Update en nieuwere versies wordt bladermodus opnieuw automatisch ingeschakeld bij het lezen van e-mails in Windows 10 Mail. (#7289)
* Op de meeste brailleleesregels met een brailletoetsenbord verwijdert punt 7 nu het laatst ingevoerde braillekarakter, waar punt 8 zorgt voor een druk op de enter-toets. (#6054)
* Bij het verplaatsen van de cursor in bewerkbare tekst (zoals met de cursortoetsen of backspace) is de gesproken feedback van NVDA in veel gevallen een stuk nauwkeuriger, met name in Chrome en terminal applicaties. (#6424)
* De inhoud van het dialoogvenster om handtekeningen te bewerken in Microsoft Outlook 2016 kan nu worden gelezen. (#7253)
* In Java Swing applicaties is NVDA er niet langer de oorzaak van dat de applicatie crasht bij het navigeren door tabellen. (#6992)
* In de Windows 10 Creators Update zal NVDA Pop-upmeldingen niet langer meerdere keren achter elkaar melden. (#7128)
* In het startmenu in Windows 10 zal NVDA de zoektekst niet langer melden na het indrukken van de Enter-toets om het startmenu te sluiten na een zoekopdracht. (#7370)
* Het uitvoeren van snelnavigatie naar koppen is nu beduidend sneller in Microsoft Edge. (#7343)
* In Microsoft Edge zal het navigeren in bladermodus niet langer grote stukken van bepaalde webpagina's (zoals het Wordpress 2015 thema) overslaan. (#7143)
* In Microsoft Edge worden oriëntatiepunten nu correct vertaald in andere talen dan Engels. (#7328)
* IN braille wordt de selectie nu correct gevolgd wanneer de geselecteerde tekst de leesregelbreedte overschrijdt. Wanneer u bijvoorbeeld meerdere regels selecteert met shift+pijlOmlaag, zal in braille de laatst geselecteerde regel getoond worden. (#5770)
* In Firefox zal NVDA niet langer onnodig meerdere keren "sectie" uitspreken bij het openen van details voor een tweet op twitter.com. (#5741)
* Tabelnavigatiecommando's zijn niet langer beschikbaar voor opmaaktabellen in BladerModus tenzij het melden van lay-outtabellen is ingeschakeld. (#7382)
* In Firefox en Chrome springen tabelnavigatiecommando's in bladermodus nu over verborgen tabelcellen heen. (#6652, #5655)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2017.2

Hoogtepunten in deze versie zijn volledige ondersteuning voor audio-onderdrukking in de Windows 10 Creators Update; oplossingen voor verschillende selectieproblemen in bladermodus, inclusief problemen met Alles Selecteren; significante verbeteringen in de ondersteuning van Microsoft Edge; en verbeteringen op het web zoals aangeven van elementen gemarkeerd als huidig (via aria-current).

### Nieuwe Functies

* Informatie over celranden kan nu worden gemeld in Microsoft Excel via `NVDA+f`. (#3044)
* Ondersteuning toegevoegd voor aria-current attributen. (#6358)
* Automatische taalverandering wordt nu ondersteund in Microsoft Edge. (#6852)
* Ondersteuning toegevoegd voor Windows Rekenmachine op Windows 10 Enterprise LTSB (Long-Term Servicing Branch) en Server. (#6914)
* Als u het commando read current line driemaal snel uitvoert, wordt de regel gespeld met karakterbeschrijvingen. (#6893)
* Nieuwe taal: Burmees.
* Unicode symbolen zoals pijl omhoog, pijl omlaag en breuksymbolen worden nu juist uitgesproken. (#3805)

### Veranderingen

* Bij het navigeren in de simpele leesoverzichtmodus in applicaties die gebruik maken van UI Automation worden bepaalde irrelevante objecten nu genegeerd om de navigatie eenvoudiger te maken. (#6948, #6950) 

### Opgeloste Problemen

* Menu-items op webpagina's kunnen nu geactiveerd worden binnen de bladermodus. (#6735)
* Het drukken van escape in het dialoogvenster configuratieprofielen "Verwijderen bevestigen" zorgt ervoor dat het venster gesloten wordt. (#6851)
* Het mogelijke vastlopen van Mozilla Firefox en andere Gecko-applicaties waar de multi-process-functie is ingeschakeld, is opgelost. (#6885)
* De accuratesse van het melden van de achtergrondkleur in de schermoverzichtmodus is verbeterd bij tekst die getekend is met een transparante achtergrond. (#6467)
* Verbeterde ondersteuning binnen Internet Explorer 11 voor elementbeschrijvingen die beschikbaar zijn op webpagina's (specifiek, ondersteuning voor aria-describedby in iframes en wanneer meerdere ID's zijn opgegeven). (#5784)
* In de Windows 10 Creators Update werkt NVDA's audio-onderdrukking opnieuw zoals in eerdere Windows-versies (d.w.z. Onderdrukken bij spraak- en geluidsuitvoer, Altijd onderdrukken, en geen onderdrukking zijn allemaal beschikbaar). (#6933)
* Bij bepaalde (UIA) controls waarvoor geen toetsenbordsneltoets is gedefineerd, weigert NVDA nniet langer deze te melden of ernaar te navigeren. (#6779)
* In sneltoets-informatie voor bepaalde (UIA) controls worden niet langer twee lege spaties toegevoegd. (#6790)
* Het weigeren van bepaalde toetscombinaties op HIMS leesregels (o.a. spatie+punt4) is opgelost. (#3157)
* Een probleem opgelost bij het openen van een seriële poort op systemen die gebruik maken van bepaalde niet-Engelse talen waarbij het verbinden met brailleleesregels in sommige gevallen mislukte. (#6845)
* De kans dat het configuratiebestand beschadigt bij het afsluiten van Windows is verminderd. Configuratiebestanden worden nu naar een tijdelijk bestand geschreven voordat het eigenlijke configuratiebestand vervangen wordt. (#3165)
* Bij het twee keer uitvoeren van het lees huidige regel commando om de huidige regel te laten spellen, wordt nu de juiste taal gebruikt voor het spellen van karakters. (#6726)
* Het navigeren per regel in Microsoft Edge is nu tot wel drie keer zo snel in de Windows 10 Creators Update. (#6994)
* NVDA meldt niet langer "Web Runtime groepering" wanneer een Microsoft Edge document in de Windows 10 Creators Update de focus krijgt. (#6948)
* Alle bestaande versies van SecureCRT worden nu ondersteund. (#6302)
* Adobe Acrobat Reader loopt niet langer vast in bepaalde PDF-documenten (specifiek, de documenten die lege ActualText attributen bevatten). (#7021, #7034)
* In bladermodus in Microsoft Edge worden interactieve tabellen (ARIA grids) niet langer overgeslagen bij het navigeren naar tabellen met t en shift+t. (#6977)
* In bladermodus zal het indrukken van shift+home na een voorwaardse selectie de selectie zoals verwacht weer ongedaan maken tot het begin van de regel. (#5746)
* In bladermodus gaat het selecteren van alle tekst (control+a) niet langer fout wanneer de cursor zich niet aan het begin van de tekst bevindt (#6909)
* Enkele andere zeldzame selectieproblemen in bladermodus opgelost. (#7131)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2017.1

Hoogtepunten in deze versie zijn melden van secties en tekstkolommen in Microsoft Word; Ondersteuning voor lezen, navigeren en annoteren van boeken in Kindle voor PC; en verbeterde ondersteuning voor Microsoft Edge.

### Nieuwe Functies

* In Microsoft Word kan het soort sectie-einde en het nummer van de sectie nu gemeld worden. Dit schakelt u in met de optie "paginanummers melden" in het dialoogvenster documentopmaak. (#5946)
* In Microsoft Word kunnen de tekstkolommen nu gemeld worden. Dit schakelt u in met de optie "paginanummers melden" in het dialoogvenster documentopmaak. (#5946)
* Automatische taalherkenning wordt nu ondersteund in Wordpad. (#6555)
* Het NVDA-commando om te zoeken (NVDA+control+f) wordt nu ondersteund in bladermodus voor Microsoft Edge. (#6580)
* Snelnavigatie voor knoppen in bladermodus (b en shift+b) worden nu ondersteund in Microsoft Edge. (#6577)
* Bij het kopiëren van een werkblad in Microsoft Excel worden kolom- en rijkoppen onthouden. (#6628)
* Ondersteuning voor lezen en navigeren van boeken in Kindle voor PC versie 1.19, inclusief toegang tot links, voetnoten, afbeeldingen, highlights en gebruikersnotities. Voor meer informatie verwijzen we naar de sectie Kindle voor PC in NVDA handleiding. (#6247, #6638)
* Bladermodus tabel navigatie wordt nu ondersteund in Microsoft Edge. (#6594)
* In Microsoft Excel meldt het commando om de locatie van de leescursor te melden (desktop: NVDA+numpadDelete, laptop: NVDA+delete) nu de naam van het werkblad en de cellocatie. (#6613)
* Een optie toegevoegd aan het Afsluiten dialoogvenster om te herstarten met het loggen van debug-informatie. (#6689)

### Veranderingen

* Het minimum voor de knippersnelheid van de braillecursor is nu 200 ms. Wanneer dit eerder lager was ingesteld, zal dit worden verhoogd naar 200 ms. (#6470)
* Er is een selectievakje toegevoegd aan het dialoogvenster braille-instellingen voor het in/uitschakelen van het knipperen van de braillecursor. Eerder werd een waarde van nul gebruikt om dit te bereiken. (#6470)
* eSpeak NG bijgewerkt (commit e095f008, 10 januari 2017). (#6717)
* Vanwege wijzigingen in de Windows 10 Creators Update is de "Altijd onderdrukken" modus niet meer beschikbaar in de audio-onderdrukkingsinstellingen van NVDA. Deze optie is nog wel beschikbaar bij oudere versies van windows 10. (#6684)
* Vanwege wijzigingen in de Windows 10 Creators Update is het in de "Onderdrukken bij spraak- en geluidsuitvoer" modus niet meer mogelijk om te waarborgen dat de audio volledig onderdrukt is voordat het spreken van de spraak begint. Ook wordt audio na het spreken niet lang genoeg onderdrukt om ervoor te zorgen dat er geen stuitereffect ontstaat in het volume. Deze veranderingen hebben geen effect op oudere versies van windows 10. (#6684)

### Opgeloste problemen

* Een bevriezingsprobleem opgelost in Microsoft Word bij het navigeren per alinea door een groot document in bladermodus. (#6368)
* Tabellen in Microsoft Word die gekopieerd werden uit Microsoft Excel worden niet langer behandeld als lay-outtabellen en worden daardoor niet langer genegeerd. (#5927)
* Wanneer er geprobeerd wordt te typen in de beveiligde weergave van Microsoft Excel maakt NVDA nu een geluid in plaats van het uitspreken van karakters die niet getypt werden. (#6570)
* Het drukken van escape in Microsoft Excel schakelt niet langer onterecht naar bladermodus, tenzij de gebruiker eerder expliciet naar bladermodus is geschakeld met NVDA+spatiebalk en dan focusmodus heeft geactiveerd door enter te drukken op een formulierveld. (#6569) 
* NVDA loopt niet langer vast in Microsoft Excel spreadsheets waarin een gehele rij of kolom is samengevoegd. (#6216)
* Het melden van afgesneden/Overschrijdende tekst in cellen in Microsoft Excel zou nu accurater moeten zijn (#6472)
* NVDA meldt nu wanneer een selectievakje alleen-lezen is. (#6563)
* Het NVDA installatieprogramma laat niet langer een waarschuwing zien dat het logo-geluid niet afgespeeld kan worden omdat er geen audioapparaat beschikbaar is. (#6289)
* Besturingselementen in het lint van Microsoft Excel die niet beschikbaar zijn worden nu als zodanig gemeld. (#6430)
* NVDA zal niet langer "venster" aankondigen bij het minimaliseren van vensters. (#6671)
* Getypte karakters worden nu uitgesproken in Universal Windows Platform (UWP) apps (inclusief Microsoft Edge) in de Windows 10 Creators Update. (#6017)
* De muis wordt nu gevolgd over alle schermen op computers met meerdere monitoren. (#6598)
* NVDA wordt niet langer onbruikbaar na het afsluiten van Windows Media Player als de focus op een schuifbalk staat. (#5467)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2016.4

Hoogtepunten in deze versie zijn verbeterde ondersteuning voor Microsoft Edge; bladermodus in de Windows 10 Mail app; en significante verbeteringen aan de dialoogvensters van NVDA.

### Nieuwe Functies

* NVDA kan nu regelinspringing aangeven met tonen. Dit kunt u instellen met de keuzelijst "Regelinspringing melden" in het dialoogvenster Documentopmaak. (#5906)
* Ondersteuning voor de Orbit Reader 20 brailleleesregel. (#6007)
* Een optie om het spraakweergavevenster te openen bij het opstarten is toegevoegd. Dit kunt u inschakelen via een selectievakje in het spraakweergavevenster. (#5050)
* Bij het opnieuw openen van het spraakweergavevenster, worden de locatie en afmetingen nu teruggezet. (#5050)
* Kruisverwijzingen in Microsoft Word worden nu behandeld als hyperlinks. Ze worden gemeld als links en kunnen geactiveerd worden. (#6102)
* Ondersteuning voor de Baum SuperVario2, Baum Vario 340 en HumanWare Brailliant2 brailleleesregels. (#6116)
* Initiële ondersteuning voor de Verjaardagsupdate van Microsoft Edge. (#6271)
* Bladermodus wordt nu gebruikt bij het lezen van emails in de Windows 10 mail app. (#6271)

### Veranderingen

* Liblouis braillevertaler bijgewerkt naar 3.0.0. Dit geeft significante verbeteringen in de uniforme Engelse braillecode. (#6109, #4194, #6220, #6140)
* In het venster Add-ons Beheren hebben de knoppen Add-on uitschakelen en Add-on inschakelen nu toetsenbordsneltoetsen (resp. alt+u en alt+i). (#6388)
* Verschillende opvullings- en uitlijningsproblemen in dialoogvensters van NVDA zijn opgelost. (#6317, #5548, #6342, #6343, #6349)
* Het dialoogvenster documentopmaak is aangepast zodat de inhoud scrollt. (#6348)
* De layout van het dialoogvenster Uitspraak van symbolen is aangepast zodat de volledige breedte van het dialoogvenster wordt gebruikt voor de symbolenlijst. (#6101)
* In bladermodus in webbrowsers kunt u nu de letttertoetsnavigatiecommando's e en shift+e en f en shift+f gebruiken om naar alleen-lezen invoervelden te gaan. (#4164)
* In de instelllingen voor Documentopmaak is "Wijziging van opmaak achter de cursor weergeven" hernoemd naar "Opmaakwijzigingen achter de cursor melden", omdat dit een invloed heeft op zowel braille als spraak. (#6336)
* Uiterlijk gewijzigd van het NVDA "Welkom dialoogvenster". (#6350)
* In dialoogvensters van NVDA zijn de knoppen "Ok" en "Annuleren" nu rechts uitgelijnd. (#6333)
* Er worden nu draaiknoppen gebruikt voor numerieke invoervelden zoals de instelling "Percentage toonhoogteverandering bij hoofdletters" in het dialoogvenster Stem-instellingen. U kunt de gewenste waarde invoeren of de pijltoetsen omhoog en omlaag gebruiken om de waarde aan te passen. (#6099)
* De manier waarop IFrames worden gemeld, is consistenter gemaakt in alle browsers. IFrames worden nu gemeld als "frame" in Firefox. (#6047)

### Opgeloste problemen

* Een zeldzame fout opgelost bij het afsluiten van NVDA terwijl het spraakweergavevenster open is. (#5050)
* Afbeeldingen maps verschijnen nu zoals verwacht in bladermodus in Mozilla Firefox. (#6051)
* Voorheen gebeurde er niets als u op de Entertoets drukte in het dialoogvenster Woordenboek. Nu worden alle wijzigingen opgeslagen die u hebt aangebracht en wordt het dialoogvenster afgesloten. (#6206)
* Berichten worden nu getoond in braille als u invoermodi wijzigt voor een invoermethode (native invoer/alfanumeriek, halve/volledige xmodus, etc.). (#5892, #5893)
* Als u een add-on uitschakelt en onmiddellijk weer inschakelt of omgekeerd, keert de status van de add-on nu correct terug naar de oorspronkelijke. (#6299)
* In Microsoft Word kunnen velden met paginanummers nu gelezen worden in kopteksten. (#6004)
* In het dialoogvenster symbooluitspraak kan de muis nu worden gebruikt om de focus te verplaatsen tussen de symbolenlijst en de invoervelden. (#6312)
* In bladermodus in Microsoft Word is een probleem opgelost dat de elementenlijst niet liet verschijnen als een document een ongeldige hyperlink bevatte. (#5886)
* Als u het spraakweergavevenster sluit via de taakbalk of de alt+F4 sneltoets, zal het selectievakje in het NVDA-menu nu correct aangeven of het venster al dan niet zichtbaar is. (#6340)
* Het commando Plugins herladen, veroorzaakt niet langer problemen voor getriggerde configuratieprofielen, nieuwe documenten in web browsers en schermoverzichtmodus. (#2892, #5380)
* In de talenlijst van het dialoogvenster Algemene Instellingen, worden talen als Aragonese nu correct getoond in Windows 10. (#6259)
* Geëmuleerde systeemtoetsen (b.v. een knop op een brailleleesregel die een druk op de tabtoets emuleert) worden nu getoond in de gekozen NVDA-taal in invoerhulp en het dialoogvenster Invoerhandelingen koppelen. Voorheen werden ze altijd in het Engels getoond. (#6212)
* Wijzigen van de NVDA-taal (in het dialoogvenster Algemene Instellingen) heeft nu pas effect als NVDA is herstart. (#4561)
* Het is niet langer mogelijk om het Patroonveld leeg te laten voor een nieuwe regel in het spraakwoordenboek. (#6412)
* Een zeldzaam probleem opgelost bij het zoeken naar seriële poorten in sommige systemen wat sommige drivers voor brailleleesregels onbruikbaar maakte. (#6462)
* Genummerde opsommingstekens in tabelcellen worden nu gelezen in Microsoft Word als u per cel navigeert. (#6446)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2016.3

Hoogtepunten in deze versie zijn de mogelijkheid om individuele add-ons uit te schakelen; ondersteuning voor formuliervelden in Microsoft Excel; significante verbeteringen bij het melden van kleuren; correcties en verbeteringen voor verschillende brailleleesregels; en gecorrigeerde en verbeterde ondersteuning voor Microsoft Word.

### Nieuwe Functies

* U kunt nu bladermodus gebruiken om PDF-documenten te lezen in Microsoft Edge, in de windows 10 verjaardagsupdate. (#5740)
* Doorhalen en dubbel doorhalen worden nu gemeld indien van toepassing in Microsoft Word. (#5800)
* In Microsoft Word wordt nu de titel van een tabel gemeld als die beschikbaar is. Als er een beschrijving is, kunt u die bereiken met het commando open lange beschrijving (NVDA+d) in bladermodus. (#5943)
* In Microsoft Word meldt NVDA nu positie-informatie bij wisselen tussen paragrafen (alt+shift+pijlOmlaag en alt+shift+pijlOmhoog). (#5945)
* Als Regelafstand melden is ingeschakeld in NVDA-instellingen voor Documentopmaak, wordt in Microsoft Word regelafstand nu gemeld als u die wijzigt met de voorziene sneltoetsen van Microsoft word, en als u naar tekst gaat met een andere regelafstand. (#2961)
* In Internet Explorer worden HTML5 structuurelementen nu herkend. (#5591)
* Het melden van opmerkingen (zoals in Microsoft Word) kan nu worden uitgeschakeld via het selectievakje Opmerkingen melden in het dialoogvenster met instellingen voor Documentopmaak . (#5108)
* In het venster add-ons beheren kunt u nu individuele add-ons uitschakelen. (#3090)
* Bijkomende toetskoppelingen zijn toegevoegd voor ALVA BC640/680 brailleleesregels. (#5206)
* Er is nu een commando om de brailleleesregel te verplaatsen naar de huidige focus. Momenteel is enkel bij de ALVA BC640/680 serie een toets aan dit commando gekoppeld. Voor andere leeesregels kunt u het zelf koppelen in het dialoogvenster Invoerhandelingen koppelen. (#5250)
* In Microsoft Excel kunt u nu werken met formuliervelden. Ga naar formuliervelden via de elementenlijst of met lettertoetsnavigatie in bladermodus. (#4953)
* In het dialoogvenster invoehrandelingen koppelen kunt U nu een invoerhandeling toewijzen om vereenvoudigde leesmodus in en uit te schakelen. (#6173)

### Veranderingen

* NVDA meldt nu kleuren met een begrijpelijke basisreeks van 9 kleurtinten en 3 schakeringen, met variaties van helderheid en bleekheid. Dit komt in de plaats van de subjectieve en moeilijk te begrijpen kleurnamen. (#6029)
* Het bestaande gedrag van NVDA+F9 en later NVDA+F10 is gewijzigd. Als f10 een eerste keer wordt gedrukt, wordt tekst geselecteerd. Als F10 tweemaal (snel na elkaar) wordt gedrukt, wordt de tekst gekopieerd naar het klembord. (#4636)
* eSpeakNG bijgewerkt naar versie Master 11b1a7b (22 juni 2016). (#6037)

### Opgeloste Problemen

* In bladermodus in Microsoft Word blijft de opmaak nu behouden bij het kopiëren naar het klembord. (#5956)
* In Microsoft Word reageert NVDA nu correct bij gebruik van de tabelnavigatiecommando's van Word zelf (alt+home, alt+end, alt+pageUp en alt+pageDown) en tabelselectiecommando's (navigatiecommando's met shift). (#5961)
* In dialoogvensters van Microsoft Word is de objectnavigatie van NVDA sterk verbeterd. (#6036)
* In sommige toepassingen zoals Visual Studio 2015 worden sneltoetsen (b.v. control+c om te kopiëren) nu gemeld zoals verwacht. (#6021)
* Een zeldzaam probleem opgelost bij het scannen naar seriële poorten dat op sommige systemen sommige drivers voor brailleleesregels onbruikbaar maakte. (#6015)
* Kleuren melden in Microsoft Word is nu meer accuraat omdat er nu rekening wordt gehouden met wijzigingen in Microsoft Office Thema's. (#5997)
* Bladermodus voor Microsoft Edge en ondersteuning voor Start Menu zoeksuggesties is opnieuw beschikbaar in versies van Windows 10 van na april 2016. (#5955)
* In Microsoft Word werkt het automatisch lezen van tabelkoppen beter in het geval van samengevoegde cellen. (#5926)
* In de Windows 10 Mail app weigert NVDA niet langer de inhoud van berichten te lezen. (#5635) 
* Als Commandotoetsen uitspreken is ingeschakeld, worden lock-toetsen zoals caps lock niet langer tweemaal aangekondigd. (#5490)
* Dialoogvensters van Windows Gebruikersaccountbeheer worden opnieuw correct gelezen in de Windows 10 verjaardagsupdate. (#5942)
* In de Web Conference Plugin (zoals gebruikt in de website out-of-sight.net) zal NVDA niet langer piepen en wijzigingen van de voortgangsbalk uitspreken die te maken hebben met invoer via de microfoon. (#5888)
* Als u de commando's Volgende/Vorige zoeken uitvoert in Bladermodus zal er nu een correcte hoofdlettergevoelige zoekopdracht gebeuren als de oorspronkelijke zoekopdracht hoofdlettergevoelig was. (#5522)
* Bij het bewerken van woordenboekregels krijgt u nu feedback als een reguliere expressie fout is. NVDA loopt niet langer vast als een woordenboekbestand een verkeerde reguliere expressie bevat. (#4834)
* Als NVDA niet kan communiceren met een brailleleesregel (b.v. omdat hij werd ontkoppeld), zal dit automatisch het gebruik van de leesregel uitschakelen. (#1555)
* Lichtverbeterde perstaties van filters in de Bladermodus Elementenlijst in sommige gevallen. (#6126)
* In Microsoft Excel meldt NVDA de achtergrondpatronen. De gebruikte namen komen nu overeen met die van Excel. (#6092)
* Verbeterde ondersteuning voor het Windows 10 inlogscherm, inclusief aankondigingen van waarschuwingen en het activeren van het wachtwoordveld via aanraken. (#6010)
* NVDA detecteert nu correct de secundaire routingknoppen van de ALVA BC640/680 brailleleesregels. (#5206)
* NVDA kan opnieuw Windows Pop-upmeldingen weergeven in recente versies van Windows 10. (#6096)
* Het kon gebeuren dat NVDA geen toetsaanslagen meer herkende op Baum compatibele en HumanWare Brailliant B brailleleesregels. Dit is niet langer het geval. (#6035)
* Als het melden van regelnummers is ingeschakeld in NVDA's voorkeuren voor Documentopmaak, dan worden regelnummers nu getoond op een brailleleesregel. (#5941)
* Als spraakmodus uit is, verschijnen gemelde objecten (zoals het drukken van NVDA+tab om de focus te melden) nu in het spraakweergavevenster zoals verwacht. (#6049)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2016.2.1

Deze versie verhelpt het vastlopen van Microsoft Word:

* NVDA veroorzaakt niet langer het vastlopen van Microsoft Word onmiddellijk nadat het wordt gestart in Windows XP. (#6033)
* Melden van grammaticafouten is verwijderd omdat het Microsoft Word liet vastlopen. (#5954, #5877)

## 2016.2

Hoogtepunten in deze versie zijn de mogelijkheid om spelfouten aan te geven tijdens het typen; ondersteuning voor melden van grammaticafouten in Microsoft Word; en verbeteringen en correcties aan de Microsoft Office ondersteuning.

### Nieuwe Functies

* In bladermodus in Internet Explorer en andere MSHTML-elementen, bij gebruik van lettertoetsnavigatie a en shift+a (om naar aantekeningen te springen), gaat u nu ook naar ingevoegde en verwijderde tekst. (#5691)
* In Microsoft Excel meldt NVDA nu het niveau van een groep van cellen, en ook of het is samen- of uitgevouwen. (#5690)
* Het commando Tekstopmaak melden (NVDA+f) tweemaal drukken, toont de informatie in bladermodus zodat u het kan nakijken. (#4908)
* In Microsoft Excel 2010 en hoger worden celschaduw en opvullingen met kleurovergang nu gemeld. Automatisch melden wordt gecontroleerd door de optie Kleuren melden in NVDA-instellingen voor Documentopmaak. (#3683)
* Nieuwe brailletabel: Koine Grieks. (#5393)
* In het dialoogvenster logboek weergeven kunt u de log nu opslaan met de sneltoets control+s. (#4532)
* Als het melden van spelfouten is ingeschakeld en ondersteund in het element dat de focus heeft, zal NVDA een geluid afspelen om u op een spelfout te wijzen tijdens het typen. Dit kunt u uitschakelen met de nieuwe optie "Geluid bij spelfouten tijdens typen" in het dialoogvenster Toetsenbordinstellingen van NVDA. (#2024)
* Grammaticafouten worden nu gemeld in Microsoft Word. Dit kunt u uitschakelen met de nieuwe optie "Grammaticafouten melden" in dialoogvenster met voorkeuren voor Documentopmaak. (#5877)

### Veranderingen

* In bladermodus en invulbare tekstvelden behandelt NVDA de nummerieke enter op de zelfde manier als de gewone entertoets. (#5385)
* NVDA is overgeschakeld naar de eSpeak NG spraaksynthesizer. (#5651)
* In Microsoft Excel negeert NVDA niet langer een kolomkop voor een cel als er een lege rij is tussen de cel en de kop. (#5396)
* In Microsoft Excel worden coördinaten nu aangekondigd voorafgaand aan de koppen om verwarring te voorkomen tussen koppen en inhoud. (#5396)

### Opgeloste Problemen

* Als u in bladermodus lettertoetsnavigatie probeert te gebruiken om naar een element te gaan dat niet is ondersteund voor het document, meldt NVDA dat dit niet ondersteund is in plaats van te melden dat er in die richting geen element is. (#5691)
* Bij het weergeven van de lijst met werkbladen in de Elementenlijst in Microsoft Excel, worden nu ook werkbladen opgenomen die enkel grafieken bevatten. (#5698)
* NVDA meldt niet langer overbodige informatie bij het schakelen tussen vensters in een Java-toepassing met meerdere venster zoals IntelliJ of Android Studio. (#5732)
* In Scintilla-gebaseerde editors zoals Notepad++ wordt braille nu correct bijgewerkt als u de cursor beweegt via een brailleleesregel. (#5678)
* NVDA loopt niet langer soms vast bij het inschakelen van braille-uitvoer. (#4457)
* In Microsoft Word wordt alinea-inspringing nu altijd gemeld in de meeteenheid die de gebruiker kiest (b.v. centimeters of inches). (#5804)
* Bij gebruik van een brailleleesregel worden veel NVDA-berichten die voorheen enkel werden uitgesproken nu ook in braille getoond. (#5557)
* In toegankelijke Java-toepassingen wordt nu het niveau van items in een boomstructuur gemeld. (#5766)
* Vastlopers opgelost in Adobe Flash in Mozilla Firefox in sommige gevallen. (#5367)
* In Google Chrome en Chrome-gebaseerde browsers kunnen documenten binnen dialoogvensters of toepassingen nu gelezen worden in bladermodus. (#5818)
* In Google Chrome en Chrome-gebaseerde browsers kunt u NVDA nu verplichten om naar bladermodus over te schakelen in web-dialoogvensters of toepassingen. (#5818)
* Het verplaatsen van de focus naar bepaalde elementen in Internet Explorer en andere MSHTML-elementen (specifiek waar aria-activedescendant is gebruikt) schakelt niet langer onterecht naar bladermodus. Dit gebeurde bijvoorbeeld als u naar suggesties ging in adresvelden bij het schrijven van een bericht in Gmail. (#5676)
* In Microsoft Word loopt NVDA niet langer vast in grote tabellen als melden van tabelrij/kolomkoppen is ingeschakeld. (#5878)
* In Microsoft word meldt NVDA niet langer onterecht tekst als een kop als die een overzichtsniveau heeft maar geen ingebouwde kopstijl. (#5186)
* In bladermodus in Microsoft Word werken de commando's Achter/Naar begin van containerobject springen (komma en shift+komma) nu voor tabellen. (#5883)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2016.1

Hoogtepunten in deze versie zijn de mogelijkheid om het volume van andere geluiden te verlagen; verbeteringen aan braille-uitvoer en ondersteuning voor brailleleesregels; verschillende belangrijke correcties aan Microsoft Office ondersteuning; en correcties aan bladermodus in iTunes.

### Nieuwe Functies

* Nieuwe brailletabellen: Pools 8 punts computerbraille, Mongools. (#5537, #5574)
* U kunt de braillecursor uitschakelen en zijn vorm veranderen via de nieuwe opties Cursor weergeven en Cursorvorm in het dialoogvenster Braille-instelllingen. (#5198)
* NVDA kan nu via Bluetooth verbinden met een HIMS Smart Beetle brailleleesregel. (#5607)
* NVDA kan het volume verlagen van andere geluiden als het is geïnstalleerd op Windows 8 en hoger. U kunt deze audio-onderdrukkingsmodus instellen in de Synthesizer-instellingen of door NVDA+shift+d te drukken. (#3830, #5575)
* Ondersteuning voor de APH Refreshabraille in HID mode en de Baum VarioUltra en Pronto! via een USB-verbinding. (#5609)
* Ondersteuning voor HumanWare Brailliant BI/B braille leesregels met het protocol ingesteld als OpenBraille. (#5612)

### Veranderingen

* Melden van nadruk is nu standaard uitgeschakeld. (#4920)
* In het dialoogvenster Elementenlijst in Microsoft Excel is de sneltoets voor Formules gewijzigd naar alt+r zodat hij verschilt van de sneltoets voor het Filterveld. (#5527)
* LibLouis braillevertaler bijgewerkt naar 2.6.5. (#5574)
* Het woord "tekst" wordt niet langer gemeld als de focus of de leescursor naar tekstobjecten beweegt. (#5452)

### Opgeloste problemen

* In iTunes 12 update bladermodus nu correct als een nieuwe pagina laadt in de iTunes Store. (#5191)
* In Internet Explorer en andere MSHTML-elementen gedraagt naar specifieke kopniveau's gaan met lettertoetsnavigatie zich nu zoals verwacht als het kopniveau is overschreven voor toegankelijkheidsredenen (specifiek als aria-level het niveau overschrijft van een h-tag). (#5434)
* In Spotify landt de focus minder vaak op "unbekende" objecten. (#5439)
* Focus wordt nu correct teruggezet bij het terugkeren naar Spotify vanuit een andere toepassing. (#5439)
* Bij het schakelen tussen bladermodus en focusmodus wordt de modus zowel in braille als via spraak gemeld. (#5239)
* De Startknop op de Taakbalk wordt niet langer gemeld als een lijst en/of als geselecteerd in sommige versies van Windows. (#5178)
* Berichten als "ingevoegd" worden niet langer gemeld bij het opstellen van berichten in Microsoft Outlook. (#5486)
* Bij gebruik van een brailleleesregel en tekst is geselecteerd op de huidige regel (b.v. bij het zoeken in een tekstverwerker naar tekst die op dezelfde regel voorkomt), zal de brailleleesregel scrollen al sdat nodig is. (#5410)
* NVDA sluit niet langer stil af bij het sluiten van een Windows opdrachtprompt met alt+f4 in Windows 10. (#5343)
* Als u het soort element wijzigt in de Elementenlijst in bladermodus, wordt het filterveld nu leeggemaakt. (#5511)
* Als u de muis beweegt in tekstvelden in Mozilla-toepassingen, leest dit opnieuw de betreffende regel, woord, etc. zoals verwacht in plaats van de hele inhoud. (#5535)
* Bij het bewegen van de muis in tekstvelden in Mozilla-toepassingen stopt het lezen niet langer bij elementen als links binnen het woord of de regel worden gelezen. (#2160, #5535)
* In Internet Explorer kan de shoprite.com website nu worden gelezen in bladermodus. Vroeger werd hij gemeld als leeg. (Specifiek worden misvormde lang-attributen nu keurig opgevangen.) (#5569)
* In Microsoft Word worden bijgehouden wijzigingen zoals "ingevoegd" niet langer gemeld als bijgehouden wijzigingen niet worden weergegeven. (#5566)
* Als een aankruisknop focus krijgt, meldt NVDA nu wanneer hij verandert van ingedrukt naar niet ingedrukt. (#5441)
* Melden van veranderingen van muisvormen werkt opnieuw zoals verwacht. (#5595)
* Als regelinspringing wordt uitgesproken, worden non-breaking spaces nu behandeld als normale spaties. Voorheen kon dit aankondigingen veroorzaken als "spatie spatie spatie" in plaats van "3 spaties". (#5610)
* Bij het sluiten van een moderne Microsoft invoermethode kandidatenlijst wordt de focus correct teruggezet naar ofwel de invoersamenstelling of het onderliggende document. (#4145)
* In Microsoft Office 2013 en later, als het lint is ingesteld om enkel tabs te tonen, worden items in het lint opnieuw gemeld zoals verwacht als een tab wordt geactiveerd. (#5504)
* Oplossingen en verbeteringen voor aanraakscherm gebarendetectie en -koppeling. (#5652)
* Aanraakscherm hovers worden niet langer gemeld in invoerhulp. (#5652)
* NVDA weigert niet langer opmerkingen op te lijsten in de Elementenlijst voor Microsoft Excel als de opmerking op samengevoegde cellen is geplaatst. (#5704)
* In een zeer uitzonderlijk geval weigert NVDA niet langer inhoud te lezen van een werkblad in Microsoft Excel met melden van rij- en kolomkoppen ingeschakeld. (#5705)
* In Google Chrome werkt navigatie binnen een Invoersamenstelling nu zoals verwacht bij het invoeren van Oost-Aziatische karakters. (#4080)
* Bij het zoeken van Apple Music in iTunes wordt bladermodus voor de zoekresultaten nu bijgewerkt zoals verwacht. (#5659)
* Als u in Microsoft Excel shift+f11 drukt om een nieuw werkblad te maken, wordt nu uw nieuwe positie gemeld in plaats van helemaal niets. (#5689)
* Problemen opgelost met de uitvoer op de brailleleesregel bij het ingeven van Koreaanse karakters. (#5640)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2015.4

Hoogtepunten in deze versie zijn prestatieverbeteringen in Windows 10; opname in het Toegankelijkheidscentrum in Windows 8 en hoger; verbeteringen voor Microsoft Excel, zoals een lijst van werkbladen en het hernoemen ervan, en toegang tot vergrendelde cellen in beveiligde werkbladen; en ondersteuning voor het bewerken van rich text in Mozilla Firefox, Google Chrome en Mozilla Thunderbird.

### Nieuwe Functies

* NVDA verschijnt nu in het Toegankelijkheidscentrum in Windows 8 en hoger. (#308)
* Bij het bewegen tussen cellen in Excel, worden veranderingen in de opmaak nu automatisch gemeld als die opties zijn ingeschakeld in het dialoogvenster documentopmaak instellingen van NVDA. (#4878)
* Aan het dialoogvenster documentopmaak instellingen is de optie Nadruk Melden toegevoegd. Ze is standaard ingeschakeld en laat NVDA automatisch melden dat tekst benadrukt is in documenten. Momenteel is dit enkel ondersteund voor em en strong tags in Bladermodus voor Internet Explorer en andere MSHTML-elementen. (#4920)
* De aanwezigheid van ingevoegde en verwijderde tekst wordt nu gemeld in Bladermodus voor Internet Explorer en andere MSHTML-elementen als de optie Aangebrachte wijzigingen in de tekst melden, is ingeschakeld. (#4920)
* Bij het bekijken van gemaakte wijzigingen in de Elementenlijst van NVDA voor Microsoft Word, wordt meer informatie getoond zoals welke opmaakeigenschappen gewijzigd zijn. (#4920)
* In Microsoft Excel zie je een lijst van werkbladen met de mogelijkheid ze te hernoemen via de Elementenlijst (NVDA+f7). (#4630, #4414)
* Je kan nu configureren om symbolen al dan niet naar spraaksynthesizers te sturen (bijvoorbeeld om een pauze in te lassen of de intonatie te wijzigen) in het dialoogvenster Symbooluitspraak. (#5234)
* In Microsoft Excel meldt NVDA nu de invoerberichten die de auteur van het werkblad heeft toegevoegd aan cellen. (#5051)
* Ondersteuning voor de Baum Pronto! V4 en VarioUltra brailleleesregels via Bluetooth-aansluiting. (#3717)
* Ondersteuning voor het bewerken van rich text in Mozilla applicaties zoals Google Docs met braille-ondersteuning ingeschakeld in Mozilla Firefox en HTML-opstelling in Mozilla Thunderbird. (#1668)
* Ondersteuning voor het bewerken van rich text in Google Chrome en Chrome-gebaseerde browsers zoals Google Docs met braille-ondersteuning ingeschakeld. (#2634)
 * Dit vereist Chrome versie 47 of hoger.
* In bladermodus in Microsoft Excel kan je nu navigeren naar vergrendelde cellen in beveiligde werkbladen. (#4952)

### Veranderingen

* De optie Aangebrachte wijzigingen in de tekst melden, is nu standaard ingeschakeld in het dialoogvenster Documentopmaak instellingen. (#4920)
* Tijdens het navigeren per karakter in Microsoft Word met de ingeschakelde optie Aangebrachte wijzigingen in de tekst melden, wordt nu minder informatie gemeld bij wijzigingen, waardoor navigatie efficiënter verloopt. Om de extra informatie te zien, gebruikt u de Elementenlijst. (#4920)
* liblouis braillevertaler bijgewerkt naar 2.6.4. (#5341)
* Heel wat symbolen (waaronder eenvoudige wiskundige symbolen) zijn verplaatst naar het niveau sommige zodat ze standaard worden uitgesproken. (#3799)
* Als de synthesizer het ondersteunt, zou de spraak nu moeten pauzeren voor haakjes en het gedachtenstreepje (–). (#3799)
* Bij het selecteren van tekst, wordt de tekst gemeld voor de aanduiding "geselecteerd" in plaats van erna. (#1707)

### Opgeloste problemen

* Grote performantieverbeteringen bij het navigeren door de berichtenlijst van Outlook 2010/2013. (#5268)
* In een grafiek in Microsoft Excel werkt het navigeren met bepaalde toetsen (zoasl wisselen van werkblad met control+pageUp en control+pageDown) nu correct. (#5336)
* Het visuele uitzicht is gecorrigeerd van de knoppen in het waarschuwingsvenster dat verschijnt als u NVDA probeert te downgraden. (#5325)
* In Windows 8 en hoger start NVDA nu een stuk vroeger als het is geconfigureerd om te starten na het aanmelden bij Windows. (#308)
 * Als u dit heeft ingeschakeld in een vorige versie van NVDA, dan moet u het uitschakelen en het opnieuw inschakelen om deze verandering van kracht te laten worden. Volg deze procedure:
  1. Open het dialoogvenster met Algemene instellingen.
  1. Schakel dit selectievakje uit: NVDA &automatisch starten nadat ik me bij windows heb aangemeld.
  1. Druk op de OK knop.
  1. Open opnieuw het dialoogvenster met Algemene instellingen.
  1. Schakel het selectievakje in: NVDA &automatisch starten nadat ik me bij windows heb aangemeld".
  1. Druk op de OK knop.
* Performantieverbeteringen voor UI Automation inclusief File Explorer en Task Viewer. (#5293)
* NVDA schakelt nu correct naar focusmodus bij het tabben naar alleen-lezen ARIA grid controls in Bladermodus voor Mozilla Firefox en andere Gecko-gebaseerde controls. (#5118)
* NVDA meldt nu correct "geen vorig" in plaats van "geen volgend" als er geen objecten meer zijn bij het vegen naar links op een aanraakscherm.
* Problemen opgelost bij het typen van meerdere woorden in het filterveld in het dialoogvenster Invoerhandelingen koppelen. (#5426)
* NVDA loopt niet langer vast in sommige gevallen bij het opnieuw verbinden via USB met een HumanWare Brailliant BI/B series leesregel. (#5406)
* In talen met samengevoegde karakters werken omschrijvingen van karakters nu zoals verwacht voor Engelse karakters in hoofdletters. (#5375)
* NVDA zou niet langer af en toe mogen vastlopen bij het openen van het Startmenu in Windows 10. (#5417)
* In Skype voor Desktop worden meldingen die verschijnen voor een eerdere melding verdween nu gemeld. (#4841)
* Meldingen worden nu correct gemeld in Skype voor Desktop 7.12 en hoger. (#5405)
* NVDA meldt de focus nu correct bij het sluiten van een contextmenu in sommige toepassingen zoals Jart. (#5302)
* In Windows 7 en hoger wordt Kleur opnieuw gemeld in bepaalde toepassingen zoals Wordpad. (#5352)
* Bij het bewerken in Microsoft PowerPoint meldt een druk op de enter-toets nu automatisch de ingegeven tekst zoals een opsommingsteken of getal. (#5360)

## 2015.3

Hoogtepunten in deze versie zijn initiële ondersteuning voor Windows 10; de mogelijkheid om lettertoetsnavigatie uit te schakelen in bladermodus (nuttig voor sommige web apps); verbeteringen in Internet Explorer; en correcties voor rommelige tekst tijdens het typen in bepaalde toepassingen als braille is ingeschakeld.

### Nieuwe Functies

* De aanwezigheid van spelfouten wordt aangekondigd in bewerkbare velden voor Internet Explorer en andere MSHTML-elementen. (#4174)
* Veel meer unicode wiskunde-symbolen worden nu uitgesproken als ze in tekst voorkomen. (#3805)
* Zoeksuggesties in het Windows 10 startscherm worden automatisch gemeld (#5049)
* Ondersteuning voor de EcoBraille 20, EcoBraille 40, EcoBraille 80 en EcoBraille Plus brailleleesregels. (#4078)
* In bladermodus kunt u nu lettertoetsnavigatie in- en uitschakelen door NVDA+shift+spatiebalk te drukken. Uitgeschakeld betekent dat ingetoetste letters doorgegeven worden aan de applicatie, wat handig is voor sommige webtoepassingen zoals Gmail, Twitter en Facebook. (#3203)
* Nieuwe brailletabellen: Fins 6 punts, Iers graad 1, Iers graad 2, Koreaans graad 1 (2006), Koreaans graad 2 (2006). (#5137, #5074, #5097)
* Het QWERTY toetsenbord van de Papenmeier BRAILLEX Live Plus brailleleesregel wordt nu ondersteund. (#5181)
* Experimentele ondersteuning voor de Microsoft Edge webbrowser en browsing engine in Windows 10. (#5212)
* Nieuwe taal: Kannada.

### Veranderingen

* Liblouis braillevertaler bijgewekrt naar 2.6.3. (#5137)
* Als u een oudere versie van NVDA probeert te installeren dan degene die momenteel is geïnstalleerd, zal u nu gewaarschuwd worden dat dit niet aanbevolen is en dat NVDA helemaal verwijderd moet worden voordat u doorgaat. (#5037)

### Opgeloste problemen

* In bladermodus voor Internet Explorer en andere MSHTML-elementen gaat de snelnavigatie per formulierveld niet langer foutief naar lijstonderdelen die louter visueel zijn. (#4204)
* Voor ARIA tab panels In Firefox probeert NVDA niet langer een beschrijving te maken met alle tekst die ze bevatten. (#4638)
* In Internet Explorer en andere MSHTML-elementen, wordt bij het tabben in secties, artikels of dialoogvensters niet langer alle inhoud van de container als naam gemeld. (#5021, #5025) 
* Bij gebruik van Baum/HumanWare/APH brailleleesregels met een braille toetsenbord stopt de braille-invoer niet langer te werken na het drukken op een andere soort toets op de leesregel. (#3541)
* In Windows 10 wordt niet langer irrelevante informatie gemeld bij het drukken van alt+tab of alt+shift+tab om tussen toepassingen te schakelen. (#5116)
* Getypte tekst is niet langer rommelig bij gebruik van bepaalde toepassingen zoals Microsoft Outlook met een brailleleesregel. (#2953)
* In bladermodus in Internet Explorer en andere MSHTML-elementen, wordt nu de juiste inhoud gemeld als een element verschijnt of wijzigt en krijgt onmiddellijk de focus. (#5040)
* In bladermodus in Microsoft Word, update lettertoetsnavigatie nu de brailleleesregel en de leescursor zoals men verwacht. (#4968)
* In braille worden niet langer overbodige spaties getoond tussen of na indicatoren voor controls en opmaak. (#5043)
* Als een toepassing traag reageert en u schakelt weg van die toepassing, is NVDA in de meeste gevallen nu veel meer responsive in andere toepassingen. (#3831)
* Windows 10 Pop-upmeldingen worden nu gemeld zoals men verwacht. (#5136)
* In bepaalde (UI Automation) keuzelijsten wordt nu de waarde gemeld als ze verandert. Vroeger waren er gevallen waar dit niet werkte.
* In bladermodus in web browsers werkt tabben nu zoals men verwacht na het tabben naar een frame document. (#5227)
* Het Windows 10 lock screen kan nu weggestuurd worden bij gebruik van een aanraakscherm. (#5220)
* In Windows 7 en hoger is tekst niet langer rommelig bij het typen in bepaalde toepassingen zoals Wordpad en Skype met een brailleleesregel. (#4291)
* Op het Windows 10 lock screen is het niet langer mogelijk het klembord te lezen, draaiende toepassingen te bereiken met de leescursor, de NVDA-configuratie te wijzigen, etc. (#5269)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2015.2

Hoogtepunten in deze versie zijn de mogelijkheid om grafieken te lezen in Microsoft Excel en ondersteuning voor lezen van, interageren met, en navigeren in wiskundige inhoud.

### Nieuwe Functies

* Per zin vooruit en achteruit bewegen is nu mogelijk in Microsoft Word met respectievelijk alt+pijlOmlaag en alt+pijlOmhoog. (#3288)
* Nieuwe brailletabellen voor verschillende Indische talen. (#4778)
* In Microsoft Excel meldt NVDA nu als de inhoud van een cel is overschreden of afgesneden. (#3040)
* In Microsoft Excel kunt u nu de Elementenlijst (NVDA+f7) gebruiken voor een lijst van grafieken, opmerkingen en formules. (#1987)
* Ondersteuning voor het lezen van grafieken in Microsoft Excel. Selecteer de grafiek via de Elementenlijst (NVDA+f7) en gebruik dan de pijltoetsen om tussen de gegevenspunten te bewegen. (#1987)
* Als u MathPlayer 4 van Design Science gebruikt, kan NVDA nu wiskundige inhoud lezen en ermee interageren in internetbrowsers en in Microsoft Word en PowerPoint. Voor meer details verwijzen we naar het hoofdstuk "Inhoud van wiskundige aard lezen" van de gebruikershandleiding. (#4673)
* Via het dialoogvenster Invoerhandelingen koppelen, is het nu mogelijk om invoerhandelingen (toetsenbordsneltoetsen, aanraakgebaren, enz.) te koppelen aan alle dialoogvensters met instellingen van NVDA en opties voor documentopmaak. (#4898)

### Veranderingen

* In het dialoogvenster Documentopmaak zijn de sneltoetsen gewijzigd voor het melden van lijsten, links, regelnummers en lettertypes. (#4650)
* In het dialoogvenster Muisinstellingen zijn sneltoetsen toegevoegd voor "Geluidscoördinatie gebruiken bij verplaatsen van muis" en "Schermhelderheid bepaalt Volume audio-coördinatie". (#4916)
* Melden van kleurnamen is aanzienlijk verbeterd. (#4984)
* Liblouis braillevertaler bijgewerkt naar 2.6.2. (#4777)

### Opgeloste Problemen

* In bepaalde Indische talen worden omschrijvingen van karakters nu correct behandeld voor samengevoegde karakters. (#4582)
* Als de optie "Vertrouw taal van stem bij het verwerken van karakters en symbolen" ingeschakeld is, zal het dialoogvenster Uitspraak van interpunctie en symbolen nu correct de stemtaal gebruiken. Ook wordt de taal waarvoor de uitspraak gewijzigd wordt getoond als titel van het dialoogvenster. (#4930)
* In Internet Explorer en andere MSHTML-elementen worden getypte karakters niet langer foutief aangekondigd in bewerkbare keuzelijsten zoals het zoekveld op de Google homepage. (#4976)
* Als u in Microsoft Officetoepassingen kleuren selecteert, worden de kleurnamen nu gemeld. (#3045)
* Deense brailleweergave hersteld. (#4986)
* U kunt opnieuw PageUp/pageDown gebruiken om dia's te wisselen in een PowerPoint presentatie. (#4850)
* In Skype voor Desktop 7.2 en hoger worden typing meldingen nu gemeld en er zijn problemen opgelost onmiddellijk nadat de focus uit een conversatie beweegt. (#4972)
* Problemen opgelost bij het typen van bepaalde leestekens/symbolen zoals haken in het filterveld in het dialoogvenster Invoerhandelingen koppelen. (#5060)
* Als u in Internet Explorer en andere MSHTML-elementen g of shift+g drukt om te navigeren naar afbeeldingen komt u nu ook bij elementen die gemarkeerd zijn als afbeelding via ARIA role img. (#5062)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2015.1

Hoogtepunten in deze versie zijn bladermodus voor Microsoft Word en Outlook documenten; drastisch verbeterde ondersteuning voor de Desktop client van Skype; en aanzienlijke verbeteringen aan Microsoft Internet Explorer.

### Nieuwe Functies

* U kunt nu nieuwe symbolen toevoegen in het dialoogvenster Uitspraak van interpunctie en symbolen. (#4354)
* In het dialoogvenster INvoerhandelingen koppelen kunt u nu het veld "Filter op" gebruiken om enkel invoerhandelingen weer te geven die bepaalde woorden bevatten. (#4458)
* NVDA meldt nu automatisch nieuwe tekst in mintty. (#4588)
* In het zoekvenster van de bladermodus bevindt zich nu een optie voor het uitvoeren van een hoofdlettegevoelige zoekopdracht. (#4584)
* Lettertoetsnavigatie (h om per kop te navigeren, etc.) en de lijst met elementen (NVDA+f7) zijn nu beschikbaar in Microsoft Word documenten door het inschakelen van bladermodus met NVDA+spatie. (#2975)
* De mogelijkheid tot het lezen van HTML-berichten in Microsoft Outlook 2007 en nieuwer heeft belangrijke verbeteringen ondergaan. Bladermodus wordt automatisch geactiveerd voor deze berichten. Wanneer bladermodus in bepaalde zeldzame situaties niet geactiveerd wordt, kunt u activatie forceren met NVDA+spatie. (#2975)
* Tabel kolomkoppen in Microsoft word worden automatisch gemeld bij tabellen waarbij expliciet een rij met koppen is ingesteld door de auteur via de Microsoft word tabeleigenschappen. (#4510)
 * Dit werkt echter niet automatisch voor tabellen waarbij rijen samengevoegd zijn. In deze situaties kunt u de kolomkoppen handmatig instellen in NVDA met NVDA+shift+c.
* In Skype voor Desktop worden notificaties nu gemeld. (#4741)
* In Skype voor Desktop kunt u nu een overzicht van de meest recente berichten krijgen door gebruik te maken van NVDA+control+1 tot en met NVDA+control+0; bijv. NVDA+control+1 voor het meest recente bericht en NVDA+control+0 voor het tiende meest recente bericht. (#3210)
* In een conversatie in Skype voor Desktop zal NVDA nu melden wanneer een contactpersoon aan het typen is. (#3506)
* NVDA kan nu stil geïnstalleerd worden via de commandoregel zonder de geïnstalleerde versie automatisch te starten na de installatie. Om dit te doen gebruikt u de optie --install-silent. (#4206)
* Ondersteuning voor de Papenmeier BRAILLEX Live 20, BRAILLEX Live en BRAILLEX Live Plus brailleleesregels. (#4614)

### Veranderingen

* In het NVDA instellingenvenster Documentopmaak heeft de optie voor het melden van spellingsfouten nu een sneltoets (alt+f). (#793)
* NVDA zal nu de taal van de synthesizer/stem gebruiken voor het uitspreken van karakters en symbolen (inclusief interpunctie en symboolnamen), ongeacht automatisch van taal wisselen is ingeschakeld. Om deze optie uit te schaklen zodat NVDA de interfacetaal weer gebruikt schakelt u de nieuwe optie Vertrouw taal van stem bij het verwerken van karakters en symbolen uit in de steminstellingen. (#4210)
* Ondersteuning voor de Newfon-synthesizer is verwijderd. Newfon is nu beschikbaar als een add-on. (#3184)
* Skype voor Desktop 7 of nieuwer is nu vereist voor gebruik met NVDA; eerdere versies worden niet ondersteund. (#4218)
* Het downloaden van NVDA updates is nu veiliger. (Concreet wordt de update-informatie nu opgevraagd via https en wordt de hash van het bestand gecontroleerd nadat het bestand gedownload is.) (#4716)
* eSpeak heeft een upgrade gekregen naar versie 1.48.04 (#4325)

### Opgeloste Problemen

* In Microsoft Excel worden samengevoegde cellen met rij- en kolomkoppen nu correct afgehandeld. Als bijvoorbeeld A1 en B1 zijn samengevoegd, worden bij B2 zowel A1 en B1 gemeld als kolomkop in plaats van helemaal niets. (#4617)
* Bij het bewerken van de inhoud van een tekstvak in Microsoft PowerPoint 2003 zal NVDA nu de inhoud van iedere regel correct melden. (#4619)
* Alle dialoogvensters van NVDA worden nu op het midden van het scherm weergegeven om visuele presentatie en bruikbaarheid te verbeteren. (#3148)
* Wanneer er in Skype voor desktop bij het toevoegen van een contactpersoon een introducerend bericht wordt ingetypt, werkt het invoeren van en navigeren door de tekst nu correct. (#3661)
* Wanneer de focus verplaatst naar een nieuw item in boomstructuren in de Eclipse IDEen het eerder geselecteerde item een selectivakje is, wordt het niet langer onterecht gemeld. (#4586)
* In het venster voor spellingscontrole van Microsoft Word zal de volgende fout automatisch gemeld moeten worden wanneer de laatste fout veranderd of genegeerd is met gebruik van de daarvoor bedoelde sneltoetsen. (#1938)
* Tekst kan weer correct worden gelezen in plaatsen zoals het terminalvenster van Tera Term Pro en documenten in Balabolka. (#4229)
* Wanneer u in het dialoogvenster Invoerhandelingen koppelen tijdens het selecteren van een toetsenbordindeling voor een toetsenbordsneltoets op escape drukt, zal het menu gesloten worden in plaats van het hele venster. (#3617)
* Bij het verwijderen van een add-on wordt de map van de add-on nu correct verwijderd na het herstarten van NVDA. Voorheen moest NVDA twee keer herstart worden. (#3461)
* Er zijn belangrijke problemen opgelost bij het gebruik van Skype voor Desktop 7. (#4218)
* Bij het versturen van een bericht in Skype voor Desktop wordt het niet langer twee keer gelezen. (#3616)
* In Skype voor Desktop zou NVDA niet langer af en toe onterecht een grote berichtenstroom moeten voorlezen (mogelijk zelfs een hele conversatie). (#4644)
* Er is een probleem opgelost waarbij het NVDA-commando voor het melden van de datum/tijd de regionale instellingen van de gebruiker in sommige gevallen niet respecteerde. (#2987)
* In de bladermodus wordt onzinnige tekst (die soms zelfs meerdere regels omvat) niet langer gepresenteerd voor bepaalde afbeeldingen zoals te vinden op Google Groups. Dit gebeurde specifiek met base64 gecodeerde afbeeldingen.) (#4793)
* NVDA zou niet langer na enkele seconden moeten bevriezen wanneer de focus verplaatst wordt uit een app uit de Windows Store. (#4572)
* Verschillende verbeteringen voor Mozilla Firefox, Internet Explorer en andere MSHTML elementen, onder andere voor ondersteuning van aria. Zie voor details [het Engelstalige document](../en/changes.html). (#4045, #4794, #4798, #4800, #4575, #4839, #3776, #4491, #4667)
* Bij de spellingscontrole in Microsoft Outlook 2013 wordt het verkeerd gespelde woord nu gemeld. (#4848)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2014.4

### Nieuwe Functies

* Nieuwe talen: Colombiaans Spaans, Punjabi.
* Het is nu mogelijk om NVDA te herstarten of NVDA te herstarten met add-ons uitgeschakeld vanuit het afsluitvenster van NVDA. (#4057)
 * NVDA kan ook worden gestart met add-ons uitgeschakeld via de --disable-addons commandoregeloptie.
* In uitspraakwoordenboeken is het nu mogelijk om in te stellen dat een patroon alleen gebruikt wordt wanneer het een heel woord betreft, d.w.z. het vervangen vindt niet plaats wanneer het woord een deel van een langer woord is. (#1704)

### Veranderingen

* Wanneer u met objectnavigatie naar een object genavigeerd bent en dit object zich wel en het vorige object zich niet in een bladermodusdocument bevindt, zal de leesoverzichtsmodus automatisch ingesteld worden op document. Dit gebeurde voorheen alleen wanneer het navigatorobject veranderde door een focusverandering. (#4369)
* De lijsten voor brailleleesregels en synthesizers in de respectievelijke instellingsvensters zijn nu alfabetisch gesorteerd, behalve geen braille/geen spraak die zich nu onderaan de lijst bevinden. (#2724)
* Liblouis braillevertaler bijgewerkt naar 2.6.0. (#4434, #3835)
* Het navigeren naar tekstvelden in bladermodus door het indrukken van e en shift+e omvat nu bewerkbare keuzelijsten. Dit omvat ook het zoekvak in de nieuwste versie van Google Zoeken. (#4436)
* Het klikken op het NVDA-pictogram in het systeemvak met de linker muisknop opent nu het NVDA-menu. (#4459)

### Opgeloste Problemen

* Verschillende probleemoplossingen voor bladermodusdocumenten en de werking van NVDA op het internet. Zie voor details [het Engelstalige document](../en/changes.html). (#4369, #4169, #4418, #4405, #3494, #4173)
* In Powerpoint-presentaties volgt de leescursor nu de virtuele cursor op een correcte manier. (#4370)
* NVDA loopt in sommige gevallen niet langer vast bij het gebruik van een Handy Tech brailleleesregel. (#3709)
* Het in een aantal gevallen weergeven van een foutmelding in Windows Vista, bijv. bij het starten van NVDA via de bureaubladsnelkoppeling of via de sneltoets, is opgelost.(#4235)
* Er zijn ernstige problemen met tekstinvoer opgelost in dialoogvensters in recente versies van Eclipse. (#3872)
* In Outlook 2010 werkt het verplaatsen van de cursor in het locatieveld van afspraken en vergaderverzoeken nu naar behoren. (#4126)
* Bij het melden van de tekst van een statusbalk met een naam wordt de naam nu correct gescheiden van het eerste woord van de statusbalktekst. (#4430)
* Bij het invoeren van wachtwoorden met het uitspreken van woorden ingeschakeld worden er niet langer nodeloos meerdere sterretjes uitgesproken bij het beginnen aan een nieuw woord. (#4402)
* In de berichtenlijst van Microsoft Outlook worden items niet langer nodeloos benoemd als data-items. (#4439)
* Bij het selecteren van tekst in het codevenster van de Eclipse IDE wordt de hele selectie niet langer iedere keer uitgesproken bij een selectieverandering. (#2314)
* Verschillende versies van Eclipse worden nu als zodanig herkend en behandeld. (#4360, #4454)
* Bij het gebruik van een Papenmeier BRAILLEX brailleleesregel met BrxCom werken de toetsen op de leesregel nu als verwacht. (#4614)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2014.3

### Nieuwe Functies

* De geluiden die worden gespeeld bij het starten en afsluiten van NVDA kunnen uitgeschakeld worden via een nieuwe optie in het dialoogvenster met Algemene instellingen. (#834)
* Hulp voor add-ons is bereikbaar vanuit de Add-ons Manager voor add-ons die dit ondersteunen. (#2694)
* Ondersteuning voor de Agenda in Microsoft Outlook 2007 en hoger (#2943) inclusief:
 * Aankondiging van de huidige tijd tijdens het bewegen met de pijltjestoetsen,
 * Aanduiding of de geselecteerde tijd overlapt pet een afspraak,
 * Aankondiging van de geselecteerde afspraak als men op tab drukt
 * Smart filtering van de datum zodat de datum enkel wordt aangekondigd als de nieuw geselecteerde tijd of afspraak op een andere dag is dan de vorige.
* Ondersteuning uitgebreid voor de Inbox en andere berichtenlijsten in Outlook 2010 en hoger (#3834) inclusief:
 * De mogelijkheid om kolomkoppen te onderdrukken (van, onderwerp enz.) door de optie Rij- en kolomkoppen melden uit te schakelen in Documentopmaak instellingen,
 * De mogelijkheid om tabelnavigatiecommando's te gebruiken (control + alt + pijltjestoetsen) om door individuele kolommen te bewegen. 
* Microsoft word: als een inline afbeelding geen alternatieve tekst heeft, zal NVDA in plaats daarvan de titel van de afbeelding melden als de auteur deze heeft opgegeven. (#4193)
* Microsoft Word: melden van Alinea inspringing met het commando opmaak melden (NVDA+f) en automatisch als de nieuwe instelling Melden van alinea inspringing is ingeschakeld bij Documentopmaak instellingen. (#4165).
* Automatisch melden van ingevoegde tekst zoals een nieuw opsommingsteken, getal of tabsprong bij het drukken op enter in bewerkbare documenten en tekstvelden. (#4185)
* Microsoft word: NVDA+alt+c meldt de tekst van een opmerking als de cursor binnen een opmerking staat. (#3528)
* Verbeterde ondersteuning voor het automatisch lezen van kolom- en rijkoppen in Microsoft Excel (#3568) inclusief:
 * Ondersteuning voor Excel defined name ranges om kopcellen te identificeren (compatibel met de Jaws screenreader) 
 * De commando's kolomkoppen instellen (NVDA+shift+c) en rijkoppen instellen (NVDA+shift+r) bewaren de instelllingen nu in het werkblad zodat ze beschikbaar zijn de volgende keer dat het blad wordt geopend, en zo zullen ze ook beschikbaar zijn voor andere schermlezers die het defined name range schema ondersteunen.
 * Deze commando's kunnen nu ook meerdere keren per blad worden gebruikt om verschillende koppen in te stellen voor verschillende gebieden.
* Ondersteuning voor het automatisch lezen van kolom- en rijkoppen in Microsoft Word (#3110) inclusief:
 * Ondersteuning van MS Word bookmarks om kopcellen te identificeren (compatibel met de Jaws screenreader) 
 * De commando's kolomkoppen instellen (NVDA+shift+c) en rijkoppen instellen (NVDA+shift+r) laten u in de eerste kopcel van een tabel toe om NVDA te laten weten dat deze koppen automatisch gemeld moeten worden. De instellingen worden in het document bewaard zodat ze beschikbaar zijn de volgende keer dat het document wordt geopend, en ze zullen beschikbaar zijn voor andere schermlezers die het bookmark schema ondersteunen.
* Microsoft Word: meld de afstand van de linkerrand van de pagina als men op de tabtoets drukt. (#1353)
* Microsoft Word: geeft feedback in spraak en braille voor de meest beschikbare opmaaksneltoetsen (vet, cursief, onderlijnen, uitlijning en kopniveau's). (#1353)
* Microsoft Excel: als de geselecteerde cel opmerkingen bevat, kunnen deze nu gemeld worden via NVDA+alt+c (#2920)
* Microsoft Excel voorziet een NVDA-specifiek dialoogvenster om de opmerkingen te bewerken bij de momenteel geselecteerde cel als u het Excel-commando shift+f2 drukt om in de modus te komen voor het bewerken van opmerkingen. (#2920)
* Microsoft Excel: feedback in spraak en braille voor veel meer sneltoetsen die de selectie verplaatsen (#4211) inclusief:
 * Verticale paginaverplaatsing (pageUp en pageDown)
 * Horizontale paginaverplaatsing (alt+pageUp en alt+pageDown)
 * Selectie uitbreiden (bovengenoemde toetsen samen met Shift).
 * Selecteren van het huidige gebied (control+shift+8)
* Microsoft Excel: meld verticale en horizontale uitlijning voor cellen met het commando opmaak melden (NVDA+f) en automatisch als de optie voor het melden van uitlijning is ingeschakeld in de Documentopmaak instellingen. (#4212)
* Microsoft Excel: de stijl van een cel kan nu worden gemeld met het commando opmaak melden (NVDA+f). Ze kan ook automatisch worden gemeld als in Documentopmaak instellingen de optie Stijl melden is ingeschakeld. (#4213)
* Microsoft Powerpoint: bij het verplaatsen van vormen binnen een dia met de pijltoetsen wordt nu de huidige locatie van de vorm gemeld (#4214) inclusief:
 * De afstand tussen de vorm en elke diarand wordt gemeld
 * Als de vorm overlapt met een andere vorm of erdoor wordt overlapt, dan wordt de overlapte afstand en de andere vorm gemeld. 
 * Om deze informatie op te vragen zonder een vorm te verplaatsen, drukt u het commando locatie melden (NVDA+delete)
 * Bij het selecteren van een vorm, if it is covered by een andere vorm, zal NVDA melden dat it is obscured.
* Het commando Locatie melden (NVDA+delete) is in sommige situaties meer inhoudsafhankelijk. (#4219):
 * In standaard invoervelden en bladermodus wordt de cursorpositie gemeld als een percentage through de content, samen met zijn schermcoördinaten.
 * Bij vormen in Powerpoint Presentaties wordt positie van de vorm gemeld relatief ten opzichte van de dia en andere vormen.
 * Dit commando tweemaal drukken, resulooteert in het oudere gedrag dat de locatie-informatie meldt voor de hele control.
* Nieuwe taal: Catalaans.

### Veranderingen

* Liblouis braillevertaler bijgewerkt naar 2.5.4. (#4103)

### Opgeloste Problemen

* In Google Chrome en Chrome-gebaseerde browsers worden bepaalde stukken tekst (bvb. als ze beklemtoond zijn) niet langer herhaald bij het melden van de tekst van een waarschuwing of dialoogvenster. (#4066)
* Als u in bladermodus in Mozilla applicaties enter drukte op een knop etc. werd die niet altijd geactiveerd (of de verkeerde control werd geactiveerd). Dit was enkel in sommige gevallen zoals de knoppen bovenaan Facebook. Dit probleem is verholpen. (#4106)
* Nutteloze informatie wordt niet langer aangekondigd bij het tabben door iTunes. (#4128)
* In bepaalde lijsten in iTunes zoals de Muzieklijst, werkt het bewegen naar het volgende item nu correct via gebruik van objectnavigatie. (#4129)
* HTML-elementen die via WAI ARIA markup worden veranderd in koppen zijn nu opgenomen in de Bladermodus Elementenlijst en snelnavigatie voor Internet Explorer documenten. (#4140)
* Als u, in bladermodus documenten, binnen pagina links volgt in recente versies van Internet Explorer verplaatst de focus nu correct naar doelpositie en dit wordt ook gemeld. (#4134)
* Microsoft Outlook 2010 en hoger: overall access to secure dialogs zoals de Nieuwe profielen en mail setup dialogs is verbeeterd. (#4090, #4091, #4095)
* Microsoft Outlook: Useless verbosity has been decreased in command toolbars when navigating through certain dialogs. (#4096, #3407)
* Microsoft Word: tabben naar een lege cel in een tabel kondigt niet langer foutief aan dat de tabel wordt verlaten. (#4151)
* Microsoft Word: het eerste teken na het einde van een tabel (inclusief een nieuwe lege regel) wordt niet langer foutief als onderdeel van de tabel beschouwd. (#4152)
* In de spellingcontrole van Microsoft Word 2010 wordt het eigenlijke foutief gespelde woord gemeld in plaats van onterecht enkel het eerste vette woord te melden. (#3431)
* In bladermodus in Internet Explorer en andere MSHTML-elementen, tabbing of gebruik van lettertoetsnavigatie om naar formuliervelden te gaan, meldt opnieuw het label in veel gevallen waar dat vroeger niet gebeurde (specifiek waar HTML label elements zijn gebruikt). (#4170)
* Microsoft Word: Reporting de aanwezigheid en placement of comments is more accurate. (#3528)
* Navigatie in bepaalde dialoogvensters in MS Office producten zoals Word, Excel en Outlook is verbeterd door niet langer bepaalde control container toolbars te melden die niet nuttig zijn voor de gebruiker. (#4198) 
* Task panes zoals clipboard manager of File recovery lijken niet langer per ongeluk focus te krijgen bij het openen van een toepassing als Microsoft Word of Excel, waardoor de gebruiker soms heen en weer moest schakelen naar de toepassing om het document of werkblad te gebruiken. (#4199)
* NVDA weigert niet langer te werken op recente Windows besturingssystemen als de taal van Windows is ingesteld als Servisch (Latin). (#4203) 
* Pressing numlock in invoerhulp nu correctly toggles numlock, rather than causing het toetsenbord en het besturingssysteem to become out of sync in regards to de status van deze toets. (#4226)
* In Google Chrome wordt de titel van het document opnieuw gemeld bij het wisselen van tabblad. In NVDA 2014.2 gebeurde dit in sommige gevallen niet. (#4222)
* In Google Chrome en Chrome-gebaseerde browsers wordt het webadres van het document niet langer gemeld bij het lezen van het document. (#4223)
* When running say all als de No speech synthesizer is geselecteerd (nuttig voor automated testing), say all will nu complete in plaats van te stoppen na de eerste regels. (#4225)
* Microsoft Outlook's Signature dialog: het Signature editing veld is nu toegankelijk, wat full cursor tracking en format detection mogelijk maakt. (#3833) 
* Microsoft Word: bij het lezen van de laatste regel van een tabelcel, wordt niet langer de hele tabelcel gelezen. (#3421)
* Microsoft Word: bij het lezen van de eerste of de laatste regel van een inhoudsopgave, wordt niet langer de hele inhoudsopgave gelezen. (#3421)
* Bij het uitspreken van woorden en in sommige andere gevallen, worden woorden niet langer onterecht onderbroken bij markeringen zoals klinkertekens en virama in Indische talen. (#4254)
* Invoervelden voor getallen worden nu correct behandeld in GoldWave. (#670)
* Microsoft Word: als u per alinea navigeert met control+pijlOmlaag / control+pijlOmhoog is het niet langer nodig de toetscombinatie tweemaal te drukken als u door een lijst gaat. (#3290)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2014.2

### Nieuwe Functies

* Aankondiging van tekstselectie is nu mogelijk in sommige custom invoervelden waar display information wordt gebruikt. (#770)
* In toegankelijke Javatoepassingen wordt informatie over de positie nu aangekondigd voor keuzerondjes en andere controls die groepsinformatie weergeven. (#3754)
* In toegankelijke Javatoepassingen worden sneltoetsen nu aangekondigd voor controls die hiervan voorzien zijn. (#3881)
* In bladermodus worden nu labels bij oriëntatiepunten gemeld. Ze zijn ook opgenomen in het dialoogvenster van de Elementenlijst. (#1195)
* In bladermodus worden gelabelde gebieden nu behandeld als oriëntatiepunten. (#3741)
* In Internet Explorer documenten en toepassingen worden Live Regions (onderdeel van de W3c ARIA standaard) nu ondersteund. Deze laten auteurs van webpagina's toe om bepaalde gebieden te markeren als veranderlijk. Als de inhoud van zo een gebied verandert, zal die automatisch worden voorgelezen. (#1846)

### Veranderingen

* Bij het afsluiten van een dialoogvenster of toepassing in een bladermodus document, wordt de naam en het type van het bladermodus document niet langer aangekondigd. (#4069)

### Opgeloste problemen

* Het standaard Windows Systeemmenu wordt niet langer onverwacht geblokkeerd in Javatoepassingen (#3882)
* Bij het kopiëren van tekst van Schermoverzichtmodus, worden lijnsprongen niet langer genegeerd. (#3900)
* Nutteloze objecten met witruimte worden niet langer gemeld in sommige toepassingen als de focus verandert of bij gebruik van objectnavigatie met eenvoudige leesoverzichtmodus ingeschakeld. (#3839)
* Berichtvakken en andere dialoogvensters van NVDA veroorzaken opnieuw dat eerdere spraak wordt geannuleerd vooraleer het dialoogvenster aan te kondigen.
* In bladermodus worden de labels van controls zoals links en knoppen nu correct weergegeven als de auteur het label heeft overschreven om de toegankelijkheid te verbeteren (meer bepaald door aria-label of aria-labelledby te gebruiken). (#1354)
* In Bladermodus in Internet Explorer wordt tekst in een element met aria-presentation niet langer genegeerd. (#4031)
* Het is nu opnieuw mogelijk Viëtnamese tekst te typen met de Unikey software. Schakel hiervoor het selectievakje Behandel toetsen van andere toepassingen uit, dat is toegevoegd aan het dialoogvenster Toetsenbordinstellingen. (#4043) 
* In bladermodus worden menu items van keuzerondjes en selectievakjes gemeld als controls in plaats van gewone klikbare tekst. (#4092)
* NVDA schakelt niet langer foutief van focusmodus naar bladermodus als een menu item van een keuzerondje of selectievakje focus krijgt. (#4092)
* Als in Microsoft PowerPoint "getypte woorden uitspreken is ingeschakeld, worden karakters die worden verwijderd met backspace niet langer aangekondigd als deel van het getypte woord. (#3231)
* In de dialoogvensters met opties van Microsoft Office 2010 worden de labels van vervolgkeuzelijsten correct gemeld. (#4056)
* Als u in bladermodus in Mozillatoepassingen de snelnavigatiecommando's gebruikt om naar volgende/vorige knop of formulierveld te springen, worden nu ook aankruisknoppen meegenomen. (#4098)
* De inhoud van alerts in Mozillatoepassingen wordt niet langer tweemaal gemeld. (#3481)
* In bladermodus worden containers en oriëntatiepunten niet langer herhaald als u erbinnen navigeert terwijl de pagina-inhoud wijzigt (b.v. bij het navigeren op de websites van Facebook en Twitter). (#2199)
* NVDA herstelt zich vaker als u wegschakelt van toepassingen die niet meer reageren. (#3825)
* The caret (insertion point) opnieuw correctly updates when doing een sayAll command while in tekstvelden drawn directly to het scherm. (#4125)

## 2014.1

### Nieuwe Functies

* Ondersteuning voor Microsoft PowerPoint 2013. Merk op dat beveiligde weergave niet wordt ondersteund. (#3578)
* In Microsoft word en Excel kan NVDA nu het geselecteerde symbool lezen bij het kiezen van symbolen uit het dialoogvenster Symbolen Invoegen. (#3538)
* U kunt nu kiezen of inhoud in documenten als klikbaar moet worden aangegeven via een nieuwe optie in het dialoogvenster Documentopmaak. Deze optie is standaard ingeschakeld overeenkomstig het vroegere gedrag. (#3556)
* Ondersteuning voor brailleleesregels die via Bluetooth zijn verbonden met een computer die met de Widcomm Bluetooth Software werkt. (#2418)
* Bij het bewerken van tekst in PowerPoint worden hyperlinks nu gemeld. (#3416)
* In ARIA-toepassingen of dialoogvensters op internet kunt u nu NVDA naar bladermodus laten schakelen met NVDA+spatiebalk. Dit laat documentachtige navigatie toe in de toepassing of het dialoogvenster. (#2023)
* In Outlook Express, Windows Mail en Windows Live Mail meldt NVDA het nu als een bericht een bijlage heeft of gemarkeerd is. (#1594)
* Bij het navigeren door tabellen in toegankelijke Java toepassingen worden rij- en kolomcoördinaten nu gemeld, inclusief kolom- en rijkoppen als die er zijn. (#3756)

### Veranderingen

* Voor Papenmeier brailleleesregels is het commando move to flat review/focus verwijderd. Gebruikers kunnen de gewenste toetsen toekennen via het dialoogvenster Invoerhandelingen koppelen. (#3652)
* NVDA vereist nu Microsoft VC runtime versie 11, wat inhoudt dat het niet langer kan werken op besturingssystemen ouder dan Windows XP Service Pack 2 of Windows Server 2003 Service Pack 1.
* Als het interpunctieniveau is ingesteld op Sommige, zullen nu de asterisk (*) en het plusteken (+) worden uitgesproken. (#3614)
* eSpeak bijgewerkt naar versie 1.48.04 die veel taalverbeteringen bevat en die een aantal vastlopers oplost. (#3842, #3739, #3860)

### Opgeloste problemen

* Bij het navigeren tussen of het selecteren van cellen in Microsoft Excel zou NVDA niet langer foutief de oude cel mogen aankondigen in plaats van de nieuwe cel als Microsoft Excel traag is bij het verplaatsen van de selectie. (#3558)
* NVDA werkt nu correct als u via het contextmenu een keuzelijst opent binnen een cel in Microsoft Excel. (#3586)
* In winkelpagina's van iTunes 11 wordt nieuwe pagina-inhoud nu juist getoond in bladermodus als u een link volgt in de winkel of bij het initieel openen van de winkel. (#3625)
* Knoppen om een preview van nummers te krijgen in de iTunes 11 winkel tonen nu hun label in bladermodus. (#3638)
* In bladermodus in Google Chrome worden de labels van selectievakjes en keuzerondjes nu correct weergegeven. (#1562)
* In Instantbird meldt NVDA niet langer nutteloze informatie elke keer u naar een contact gaat in de Contactenlijst. (#2667)
* In bladermodus in Adobe Reader wordt de juiste tekst nu weergegeven voor knoppen, etc. waar het label werd overschreven via een tooltip of op andere manieren. (#3640)
* In bladermodus in Adobe Reader zullen overbodige afbeeldingen die de tekst "mc-ref" bevatten niet langer worden weergegeven. (#3645)
* NVDA meldt niet langer alle cellen in Microsoft Excel als onderlijnd bij hun opmaakinformatie. (#3669)
* Toont niet langer betekenisloze karakters in bladermodus documenten zoals die in de Unicode-reeks voor privé-gebruik. In sommige gevallen verhinderden deze dat zinvoller labels werden getoond. (#2963)
* Invoersamenstelling voor het invoeren van Oost-Aziatische karakters weigert niet langer in PuTTY. (#3432)
* Navigeren door een document na afgebroken automatisch lezen leidt er niet langer toe dat NVDA soms foutief aankondigde dat u een veld verliet (zoals een tabel) lager in het document dat het automatisch lezen eigenlijk nooit had uitgesproken. (#3688)
* Bij gebruik van bladermodus snelnavigatiecommando's tijdens automatisch lezen met doorbladeren ingeschakeld, kondigt NVDA accurater het nieuwe veld aan; b.v. zegt nu dat een kop een kop is, in plaats van enkel zijn tekst. (#3689)
* De snelnavigatiecommando's om te springen naar het einde of begin van een container werken nu met doorbladeren tijdens automatisch lezen; d.w.z. dat ze niet langer het huidige automatisch lezen zullen afbreken. (#3675)
* Benamingen van invoerhandelingen die voorkomen in het dialoogvenster Invoerhandelingen koppelen zijn nu duidelijker en vertaald. (#3624)
* NVDA veroorzaakt niet langer het vastlopen van bepaalde programma's bij het bewegen van de muis over hun rich edit (TRichEdit) controls. Het gaat o.a. om de programma's Jarte 5.1 en BRfácil. (#3693, #3603, #3581)
* In Internet Explorer en andere MSHTML-elementen worden containers zoals tabellen die zijn gemarkeerd met de ARIA presentation role niet langer gemeld aan de gebruiker. (#3713)
* In Microsoft Word herhaalt NVDA op de brailleleesregel niet langer meermaals de informatie over rijen en kolommen voor een tabelcel. (#3702)
* In talen zoals Frans en Duits die een spatie gebruiken om duizendtallen te scheiden, worden de cijfers van aparte groepjes niet langer uitgesproken als een enkel getal. Dit was vooral problematisch voor tabelcellen die getallen bevatten. (#3698)
* Braille weigert niet langer soms te vernieuwen als de systeemcursor beweegt in Microsoft Word 2013. (#3784)
* Als u gepositioneerd bent op het eerste karakter van een kop in Microsoft Word, verdwijnt de tekst die de kop en zijn niveau aankondigt niet langer van de brailleleesregel. (#3701)
* Als een programma wordt afgesloten waarvoor een configuratieprofiel actief is, weigert NVDA niet langer soms het profiel uit te schakelen. (#3732)
* Bij Aziatische invoer in een control binnen NVDA zelf (b.v. het bladermodus dialoogvenster om te zoeken), wordt niet langer foutief "NVDA" gemeld in plaats van de kandidaat. (#3726)
* De tabbladen in het opties-dialoogvenster van Outlook 2013 worden nu gemeld. (#3826)
* Verbeterde ondersteuning voor ARIA live regions in Firefox en andere Mozilla Geckotoepassingen:
 * Ondersteuning voor aria-atomic updates en filtering van aria-busy updates (#2640)
 * Alternatieve tekst (zoals alt-attribuut of aria-label) wordt gebruikt als er geen andere nuttige tekst is. (#3329)
 * Live region updates worden niet langer onderdrukt als ze gebeuren terwijl de focus beweegt. (#3777)
* Bepaalde presentatie-elementen worden niet langer foutief getoond in Firefox en andere Mozilla Geckotoepassingen in bladermodus (meer bepaald als het element is gemarkeerd met aria-presentation maar ook focus kan krijgen). (#3781)
* Een performantieverbetering bij het navigeren door een document in Microsoft Word als melden van spelfouten is ingeschakeld. (#3785)
* Verschillende verbeteringen aan de ondersteuning voor toegankelijke Java toepassingen:
 * De control die initieel focus had in een frame of dialoogvenster weigert niet langer gemeld te worden als het frame of dialoogvenster op de voorgrond komt. (#3753)
 * Overbodige positie-informatie wordt niet langer aangekondigd voor keuzerondjes (b.v. 1 van 1). (#3754)
 * Beter melden van JComboBox controls (html niet langer gemeld, beter melden van de statussen uitgevouwen en samengevouwen). (#3755)
 * Bij het melden van de tekst van dialoogvensters ontbrak soms tekst. Die is nu inbegrepen. (#3757)
 * Veranderingen aan de naam, waarde of beschrijving van de control die focus heeft worden nu accurater gemeld. (#3770)
* Een vastloper opgelost in NVDA in Windows 8 als de focus gaat naar bepaalde RichEdit controls die grote hoeveelheden tekst bevatten (b.v. NVDA's log viewer, windbg). (#3867)
* Op systemen met een hoge DPI display setting (wat standaard het geval is bij veel moderne schermen), stuurt NVDA de muis niet langer naar de verkeerde plaats in sommige toepassingen. (#3758, #3703)
* Een probleem opgelost dat zich soms voordeed bij het surfen waarbij NVDA niet langer correct werkte totdat het werd herstart, zelfs als het niet was vastgelopen. (#3804)
* Een Papenmeier brailleleesregel kan nu gebruikt worden zelfs als er nooit een Papenmeier leesregel aangesloten was via USB. (#3712)
* NVDA loopt niet langer vast als een ouder model Papenmeier BRAILLEX brailleleesregel wordt geselecteerd zonder dat er een leesregel is aangesloten.

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2013.3

### Nieuwe Functies

* Formuliervelden worden nu gemeld in Microsoft word documenten. (#2295)
* NVDA kan nu aangebrachte wijzigingen in de tekst aankondigen in Microsoft Word als Wijzigingen Bijhouden is ingeschakeld. Merk op dat u hiervoor in NVDA ook het selectievakje "Aangebrachte wijzigingen in de tekst melden" moet inschakelen in het dialoogvenster documentinstellingen (standaard is het uitgeschakeld). (#1670)
* In Microsoft Excel 2003 tot 2010 worden keuzelijsten nu aangekondigd bij het openen en navigeren. (#3382)
* Een nieuwe optie 'Doorbladeren tijdens automatisch lezen toestaan' in het dialoogvenster Toetsenbordinstellingen laat toe door een document te navigeren met de navigatietoetsen van bladermodus en de commando's om naar paragrafen of regels te gaan, terwijl u automatisch blijft lezen. Deze optie is standaard uitgeschakeld. (#2766) 
* Er is nu een dialoogvenster Invoerhandelingen koppelen, dat u eenvoudiger toelaat om snelkoppelingen (zoals toetsen op het toetsenbord) toe te kennen aan NVDA-commando's. (#1532)
* U kan nu verschillende instellingen hebben voor verschillende situaties door configuratieprofielen te gebruiken. Profielen kunnen manueel of automatisch geactiveerd worden (v.b. voor een bepaalde toepassing). (#87, #667, #1913)
* In Microsoft Excel worden cellen die links zijn nu als links aangekondigd. (#3042)
* In Microsoft Excel wordt het nu gemeld als een cel opmerkingen bevat. (#2921)

### Opgeloste problemen

* Zend Studio werkt nu hetzelfde als Eclipse. (#3420)
* Als de status verandert van bepaalde selectievakjes in het dialoogvenster Berichtregels van Microsoft Outlook 2010 wordt dat nu automatisch gemeld. (#3063)
* NVDA meldt nu de status "vastgemaakt" voor vastgemaakte items zoals tabs in Mozilla Firefox. (#3372)
* Het is nu mogelijk scripts te koppelen aan toetsenbordsneltoetsen in combinatie met de Alt- en/of de Windowstoetsen. Als dit voorheen gebeurde, werd bij het oproepen van het script ofwel het Startmenu ofwel de menubalk geactiveerd. (#3472)
* Het selecteren van tekst in bladermodusdocumenten (v.b. met control+shift+end) veroorzaakt geen verandering meer van de toetsenbordindeling op systemen waarop meerdere toetsenbordindelingen zijn geïnstalleerd. (#3472)
* Internet Explorer zou niet langer mogen vastlopen of onbruikbaar worden bij het afsluiten van NVDA. (#3397)
* Fysieke beweging en andere activiteiten op sommige nieuwere computers worden niet langer behandeld als ongeldige toetsaanslagen. Voorheen konden deze ertoe leiden dat de spraak stopte en soms activeerden ze NVDA-commando's. (#3468)
* NVDA gedraagt zich nu zoals verwacht in Poedit 1.5.7. Gebruikers van oudere versies zullen moeten updaten. (#3485)
* NVDA kan nu beveiligde documenten lezen in Microsoft Word 2010 en zal Word niet langer doen vastlopen. (#1686)
* Een onbekende commandline swiwtch bij het starten van het installatiebestand voor NVDA veroorzaakt niet langer een eindeloze loop van dialoogvensters met foutboodschappen. (#3463)
* NVDA weigert niet langer de alt-tekst te melden van afbeeldingen en objecten in Microsoft Word als de alt-tekst aanhalingstekens bevat of andere karakters die niet standaard zijn. (#3579)
* Het juiste aantal items wordt nu gemeld in bepaalde horizontale lijsten in Bladermodus. Voorheen werd soms het dubbele gemeld van het werkelijke aantal. (#2151)
* Als u control+a drukt in een Microsoft Excel werkblad wordt nu de bijgewerkte selectie gemeld. (#3043)
* NVDA kan nu XHTML-documenten correct lezen in Microsoft Internet Explorer en andere MSHTML-elementen. (#3542)
* Bij het afsluiten van het dialoogvenster Toetsenbordinstellingen krijgt de gebruiker nu een foutmelding als hij geen toets heeft gekozen als NVDA-toets. Voor een correcte werking van NVDA moet er minstens één toets gekozen worden. (#2871)
* In Microsoft Excel kondigt NVDA samengevoegde cellen nu anders aan dan meerdere geselecteerde cellen. (#3567)
* De bladermoduscursor wordt niet langer foutief gepositioneerd bij het verlaten van een dialoogvenster of toepassing binnen het document. (#3145)
* Een probleem opgelost waarbij op sommige systemen de driver voor de HumanWare Brailliant BI/B serie brailleleesregel niet als optie verscheen in het Braille-instellingen dialoogvenster, zelfs als de leesregel was verbonden via USB.

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2013.2

### Nieuwe Functies

* Ondersteuning voor het Chromium Embedded Framework, een webbrowser control die gebruikt wordt in meerdere toepassingen. (#3108)
* Nieuwe eSpeak stemvariant: Iven3.
* In Skype worden nieuwe chatberichten automatisch gemeld als de conversatie focus krijgt. (#2298)
* Ondersteuning voor Tween, inbegrepen het melden van tabnamen en minder breedsprakigheid bij het lezen van tweets.
* U kan nu het tonen van NVDA-berichten uitschakelen op een brailleleesregel door de Time-out voor berichten op 0 te zetten in het dialoogvenster Braille Instellingen. (#2482)
* Bij het beheren van Add-ons is er nu een knop "Download Add-ons" om de NVDA Add-ons-website te openen waar u beschikbare add-ons kan bekijken en downloaden. (#3209)
* In het NVDA Welkom dialoogvenster dat altijd verschijnt bij de eerste keer dat u NVDA gebruikt, kunt u nu aangeven of NVDA automatisch moet starten nadat u inlogt bij Windows. (#2234)
* Slaapmodus is automatisch ingeschakeld als u Dolphin Cicero gebruikt. (#2055)
* De Windows x64 versie van Miranda IM/Miranda NG wordt nu ondersteund. (#3296)
* Zoeksuggesties in het Windows 8.1 Startscherm worden automatisch gemeld. (#3322)
* Ondersteuning voor het navigeren in en bewerken van rekenbladen in Microsoft Excel 2013. (#3360)
* De Freedom Scientific Focus 14 Blue en Focus 80 Blue brailleleesregels, evenals de Focus 40 Blue in bepaalde configuraties die eerder waren ondersteund, zijn nu ondersteund als ze aangesloten zijn via Bluetooth. (#3307)
* Autocomplete suggesties worden nu gemeld in Outlook 2010. (#2816)
* Nieuwe brailletabellen: Engels (U.K.) computerbraille, Koreaans graad 2, Russisch braille voor computercode.
* Nieuwe taal: Farsi. (#1427)

### Veranderingen

* Als u in de objectmodus op een aanraakscherm met één vinger naar links of rechts veegt, beweegt u nu naar het vorige of volgende object, niet enkel deze in de huidige container. Veegt u met twee vingers naar links of rechts dan voert u de originele actie uit of beweegt u naar het vorige of volgende object binnen de huidige container.
* Het selectievakje "Lay-outtabellen melden" in het dialoogvenster "bladermodus instellingen" is hernoemd naar "Lay-outtabellen opnemen" om aan te geven dat snelnavigatie ze ook niet zal localiseren als het selectievakje is uitgeschakeld. (#3140)
* Platte overzichtsmodus is vervangen door object-, document en schermoverzichtmodi. (#2996)
 * Objectoverzichtmodus bekijkt tekst enkel in het navigatorobject, documentoverzicht bekijkt alle tekst in een bladermodusdocument (indien beschikbaar) en schermoverzicht bekijkt tekst op het scherm voor de huidige applicatie.
 * De commando's die vroeger overgingen naar/van platte overzichtsmodus schakelen nu tussen deze nieuwe overzichtsmodi.
 * Het navigatorobject volgt automatisch de leescursor zodat het het laagste object blijft op de positie van de leescursor als u in document- of schermoverzichtmodus bent.
 * Na het schakelen naar schermoverzichtmodus, zal NVDA in deze modus blijven totdat u expliciet terugschakelt naar document- of objectoverzichtmodus.
 * Als u in document- of objectoverzichtmodus bent, kan NVDA automatisch schakelen tussen deze twee modi afhankelijk of u al dan niet in een bladermodusdocument navigeert.
* Liblouis braillevertaler bijgewerkt naar 2.5.3. (#3371)

### Opgeloste Problemen

* Het activeren van een object kondigt nu de actie voor de activatie aan, in plaats van de actie na de activatie (b.v. uitvouwen bij het uitvouwen in plaats van invouwen). (#2982)
* Meer accuraat lezen en volgen van de cursor in verschillende invoervelden voor recente versies van Skype, zoals chat- en zoekvelden. (#1601, #3036)
* In de lijst met recente conversaties in Skype, wordt nu het aantal nieuwe gebeurtenissen gelezen voor elke conversatie, indien van toepassing. (#1446)
* Verbeteringen aan cursor tracking en leesvolgorde voor rechts-naar-links tekst die naar het scherm wordt geschreven; b.v. bewerken van Arabische tekst in Microsoft Excel. (#1601) 
* Snelnavigatie naar knoppen en formuliervelden zal nu links aangeven die gemarkeerd zijn als knoppen voor toegankelijkheidsredenen in Internet Explorer. (#2750)
* In bladermodus wordt de inhoud binnen boomstructuren niet langer weergegeven omdat een platte weergave niet bruikbaar is. U kan Enter drukken op een boomstructuur om ermee te interageren in focusmodus. (#3023)
* Het drukken van alt+pijlOmlaag of alt+PijlOmhoog, om een vervolgkeuzelijst uit te klappen in focusmodus, schakelt niet langer foutief over naar bladermodus. (#2340)
* In Internet Explorer 10 activeren tabelcellen niet langer focusmodus, tenzij de auteur van de webpagina ze expliciet focuseerbaar heeft gemaakt (#3248)
* NVDA weigert niet langer te starten als de systeemtijd eerder is dan de laaste controle op updates. (#3260)
* Als een voortgangsbalk wordt getoond op een brailleleesregel, wordt de brailleleesregel bijgewerkt als de voortgangsbalk verandert. (#3258)
* In bladermodus in Mozillatoepassingen, worden tabelbijschriften niet langer tweemaal weergegeven. Bovendien wordt de samenvatting weergegeven als er ook een bijschrift is. (#3196)
* Als u de invoertaal verandert in Windows 8, spreekt NVDA nu de juiste taal in plaats van de vorige.
* NVDA kondigt nu IME conversie mode veranderingen aan in Windows 8.
* NVDA kondigt niet langer rommel aan op het bureaublad als de Google Japanese of Atok IME invoermethodes gebruikt worden. (#3234)
* In Windows 7 en hoger, kondigt NVDA niet langer foutief spraakherkenning of aanraakinvoer aan als een toetsenbordtaalverandering.
* NVDA kondigt niet langer een specifiek speciaal karakter (0x7f) aan als u control+backspace drukt in sommige editors als "getypte karakters uitspreken" is ingeschakeld. (#3315)
* espeak verandert niet langer foutief van toonhoogte, volume, etc. als NVDA tekst leest die bepaalde XML controlekarakters bevat. (#3334) (regressie van #437)
* In Javatoepassingen worden veranderingen aan het label of waarde van de control die de focus heeft nu automatisch aangekondigd, en weergegeven bij herhaaldelijk bevragen van de control. (#3119)
* In Scintilla controls worden regels nu correct gemeld als automatische terugloop is ingeschakeld. (#885)
* In Mozillatoepassingen wordt de naam van alleen-lezen lijstitems nu correct gemeld; b.v. bij het navigeren door tweets in focusmodus op twitter.com. (#3327)
* De inhoud van bevestigingsdialoogvensters in Microsoft Office 2013 wordt nu automatisch gelezen als ze verschijnen. 
* Performantieverbeteringen bij het navigeren in bepaalde tabellen in Microsoft Word (#3326)
* NVDA's tabelnavigatiecommando's (control+alt+pijltjes) werken beter in bepaalde Microsoft Word tabellen waar een cel meerdere rijen overspant.
* Als de Add-ons Manager geopend is en u activeert hem nogmaals (ofwel vanuit het menu Extra of door een add-on-bestand te openen) weigert hij niet langer dienst. Het is nu mogelijk de Add-ons Manager te sluiten. (#3351)
* NVDA loopt niet langer vast in bepaalde dialoogvensters als Japanse of Chinese Office 2010 IME in gebruik is. (#3064)
* Meerdere spaties worden niet langer samengetrokken tot één spatie op brailleleesregels. (#1366)
* Zend Eclipse PHP Developer Tools werkt nu hetzelfde als Eclipse. (#3353)
* In Internet Explorer is het opnieuw niet nodig tab te drukken om te interageren met een ingebed object (zoals Flash content) nadat u er enter op heeft gedrukt. (#3364)
* Bij het bewerken van tekst in Microsoft PowerPoint wordt de laatste regel niet langer gemeld als de vorige regel, als de laatste regel leeg is. (#3403)
* In Microsoft PowerPoint worden objecten niet langer soms tweemaal uitgesproken als u ze selecteert of ervoor kiest om ze te bewerken. (#3394)
* NVDA veroorzaakt niet langer het vastlopen van Adobe Reader bij bepaalde slecht opgemaakte PDF-documenten die rijen bevatten die geen deel uitmaken van een tabel. (#3399)
* NVDA detecteert nu correct welke de volgende dia is die focus heeft na het verwijderen van een dia in de miniaturen-weergave van Microsoft PowerPoint. (#3415)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2013.1.1

Deze versie lost het probleem op waarbij NVDA vastliep als Iers als taal werd ingesteld. De vertalingen zijn bijgewerkt en enkele andere problemen zijn opgelost.

### Opgeloste Problemen

* De juiste karakters worden geproduceerd bij het typen in NVDA's eigen gebruikersinterface als u een Koreaanse of Japanse invoermethode als standaardmethode gebruikt. (#2909)
* In Internet Explorer en andere MSHTML-elementen worden velden met een ongeldige invoer nu correct behandeld. (#3256)
* NVDA loopt niet langer vast bij het starten als Iers is ingesteld als taal.

## 2013.1

Hoogtepunten in deze versie zijn een meer intuïtieve en consistente laptop toetsenbordindeling; basisondersteuning voor Microsoft PowerPoint; ondersteuning voor lange beschrijvingen in webbrowsers; en ondersteuning voor invoer van computerbraille voor brailleleesregels met een brailletoetsenbord.

### Belangrijk

#### Nieuwe Laptop Toetsenbordindeling

De laptop toetsenbordindeling is helemaal herzien om ze intuîtiever en consistenter te maken.
De nieuwe indeling gebruikt de pijltjestoetsen in combinatie met de NVDA-toets en andere modifiers voor leescommando's.

Let op de volgende veranderingen aan veelgebruikte commando's:

| Naam |Toets|
|---|---|
|Alles voorlezen |NVDA+a|
|Deze regel lezen |NVDA+l|
|Geselecteerde tekst lezen |NVDA+shift+s|
|Statusbalk voorlezen |NVDA+shift+end|

Bovendien zijn, samen met andere veranderingen, alle commando's veranderd voor objectnavigatie, tekstreview, muisklik en synth-instellingenring.
Bekijk het [Overzicht van Commando's](keyCommands.html) voor de nieuwe toetsen.

### Nieuwe Functies

* Basisondersteuning voor bewerken en lezen van Microsoft PowerPoint presentaties. (#501)
* Basisondersteuning voor lezen en schrijven van berichten in Lotus Notes 8.5. (#543)
* Ondersteuning voor automatische taalverandering bij het lezen van documenten in Microsoft Word. (#2047) 
* In bladermodus voor MSHTML (b.v. Internet Explorer) en Gecko (b.v. Firefox) wordt de aanwezigheid van lange beschrijvingen nu aangekondigd. Het is ook mogelijk de lange beschrijving te openen in een nieuw venster door op NVDA+d te drukken. (#809)
* Meldingen in Internet Explorer 9 en hoger worden nu uitgesproken (zoals geblokkeerde inhoud of bestandsdownloads). (#2343)
* Automatisch melden van rij- en kolomkoppen van een tabel wordt nu ondersteund voor bladermodusdocumenten in Internet Explorer en andere MSHTML-elementen. (#778)
* Nieuwe talen: Aragonees, Iers
* Nieuwe brailletabellen: Deens graad 2, Koreaans graad 1. (#2737)
* Ondersteuning voor brailleleesregels verbonden via bluetooth op een computer met de Toshiba Bluetooth Stack voor Windows. (#2419)
* Ondersteuning voor poortselectie bij gebruik van Freedom Scientific leesregels (Automatisch, USB of Bluetooth).
* Ondersteuning voor de BrailleNote familie van notitietoestellen van HumanWare, gebruikt als een brailleleesregel voor een screenreader. (#2012)
* Ondersteuning voor oudere modellen van Papenmeier BRAILLEX brailleleesregels. (#2679)
* Ondersteuning voor invoer van computerbraille voor brailleleesregels met een brailletoetsenbord. (#808)
* Nieuwe toetsenbordinstellingen die de keuze geven of NVDA de spraak moet onderbreken voor getypte karakters en/of de Entertoets. (#698)
* Ondersteuning voor verschillende browsers gebaseerd op Google Chrome: Rockmelt, BlackHawk, Comodo Dragon en SRWare Iron. (#2236, #2813, #2814, #2815)

### Veranderingen

* Liblouis braillevertaler bijgewerkt naar 2.5.2. (#2737)
* De laptop toetsenbordindeling is helemaal herzien om ze intuïtiever en consistenter te maken. (#804)
* eSpeak speech synthesizer bijgewerkt naar 1.47.11. (#2680, #3124, #3132, #3141, #3143, #3172)

### Opgeloste Problemen

* De snelnavigatietoetsen om te springen naar de volgende of vorige scheiding in bladermodus werken nu in Internet Explorer en andere MSHTML-elementen. (#2781)
* Als NVDA terugvalt naar eSpeak of als er geen spraak is omdat de gekozen spraaksynthesizer dienst weigert bij het starten van NVDA, dan wordt niet meer automatisch de fallback synthesizer teruggezet. Dit betekent dat nu, de originele synthesizer opnieuw geprobeerd wordt volgende keer dat NVDA start. (#2589)
* Als NVDA terugvalt op geen braille omdat de gekozen brailleleesregel dienst weigerde bij het starten van NVDA, dan wordt de brailleleesregel niet meer automatisch terug ingesteld op geen braille. Dit betekent dat nu, de originele leesregel opnieuw wordt geprobeerd bij de volgende keer dat NVDA start. (#2264)
* In bladermodus in Mozillatoepassingen worden updates aan tabellen nu correct weergegeven. Bijvoorbeeld, in bijgewerkte cellen worden rij- en kolomcoördinaten gemeld en tabelnavigatie werkt zoals het moet. (#2784)
* In bladermodus in web browsers werden bepaalde klikbare niet-gelabelde afbeeldingen vroeger niet weergegeven. Nu werkt dit correct. (#2838)
* Eerdere en latere versies van SecureCRT worden nu ondersteund. (#2800)
* Voor invoermethodes zoals Easy Dots IME onder XP worde de leesreeks nu correct gemeld.
* De kandidatenlijst in de Chinese Simplified Microsoft Pinyin invoermethode onder Windows 7 wordt nu correct gelezen bij het veranderen van pagina met pijl links en rechts, en bij de eerste keer dat het met Home wordt geopend.
* Als gepersonaliseerde uitspraakinformatie voor symbolen wordt opgeslagen, wordt het geavanceerde "preserve" veld niet langer verwijderd. (#2852)
* Als u "automatisch controleren op updates" uitschakelt, moet NVDA niet langer herstarten om de wijziging door te voeren.
* NVDA weigert niet langer te starten als een add-on niet kan worden verwijderd omdat zijn map momenteel in gebruik is door een andere applicatie. (#2860)
* Tablabels in het dialoogvenster met DropBox-instellingen kunnen nu gezien worden met platte overzichtzsmodus.
* Als de invoertaal wordt veranderd naar iets anders dan de standaard, detecteert NVDA nu correct de toetsen voor commando's en invoerhelpmodus.
* Voor talen zoals Duits waar het + (plus)teken een enkele toets op het toetsenbord is, is het nu mogelijk er commando's aan te binden door het woord "plus" te gebruiken. (#2898)
* In Internet Explorer en andere MSHTML-elementen worden citaten nu gemeld indien van toepassing. (#2888)
* De HumanWare Brailliant BI/B series brailleleesregel driver kan nu worden geselecteerd als de leesregel verbonden is via Bluetooth maar nooit verbonden was via USB.
* Het filteren van elementen in de Elementenlijst van de bladermodus met hoofdlettertekstfilter geeft nu niet-hoofdlettergevoelige resultaten net zoals kleine letters in plaats van helemaal niets. (#2951)
* In Mozilla browsers kan bladermodus opnieuw worden gebruikt als Flash content focus krijgt. (#2546)
* Bij gebruik van een kortschrift brailletabel en als "Naar computerbraille uitbreiden voor het woord onder de cursor" is ingeschakeld, wordt de braillecursor nu correct gepositioneerd na een woord waarin een karakter is voorgesteld door meerdere braillecellen (b.v. hoofdletterteken, letterteken, cijferteken, etc.). (#2947)
* Tekstselectie wordt nu correct getoond op een brailleleesregel in toepassingen zoals Microsoft Word 2003 en Internet Explorer invoercontrols.
* Het is opnieuw mogelijk tekst achterwaarts te selecteren in Microsoft Word terwijl Braille is ingeschakeld.
* Bij het lezen en verwijderen van karakters In Scintilla invoercontrols, kondigt NVDA correct multibyte karakters aan. (#2855)
* NVDA weigert niet langer te installeren als het pad naar het gebruikersprofiel bepaalde multibyte karakters bevat. (#2729)
* Het melden van groepen voor Lijstbeeldcontrols (SysListview32) in 64-bit toepassingen veroorzaakt niet langer een fout.
* In bladermodus in Mozillatoepassingen wordt tekstcontent niet langer foutief behandeld als bewerkbaar in sommige zeldzame gevallen. (#2959)
* Als u in IBM Lotus Symphony en OpenOffice de systeemcursor beweegt, beweegt nu de leescursor indien van toepassing.
* Adobe Flash content is nu toegankelijk in Internet Explorer in Windows 8. (#2454)
* Bluetooth ondersteuning gecorrigeerd voor Papenmeier Braillex Trio. (#2995)
* Onmogelijkheid opgelost om bepaalde Microsoft Speech API versie 5 stemmen te gebruiken zoals Koba Speech 2 stemmen. (#2629)
* In toepassingen die de Java Access Bridge gebruiken, worden brailleleesregels nu correct bijgewerkt als de systeemcursor beweegt in bewerkbare tekstvelden. (#3107)
* Ondersteunt het formulier oriëntatiepunt in bladermodusdocumenten die oriëntatiepunten ondersteunen. (#2997) 
* De eSpeak synthesizer driver behandelt het lezen per karakter nu correcter (b.v. aankondigen van de naam of de waarde van een vreemde letter in plaats van enkel zijn geluid of generieke naam). (#3106)
* NVDA weigert niet langer gebruikersinstellingen te kopiëren voor gebruik op inlog- en andere beveiligde schermen als het pad naar het gebruikersprofiel non-ASCII karakters bevat. (#3092)
* NVDA loopt niet langer vast bij gebruik van Aziatische karakterinvoer in sommige .NET-toepassingen. (#3005)
* Het is nu mogelijk bladermodus te gebruiken voor pagina's in Internet Explorer 10 als u in standaardmodus bent; b.v. [www.gmail.com](http://www.gmail.com) login-pagina. (#3151)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2012.3

Hoogtepunten in deze versie zijn ondersteuning voor Aziatische karakterinvoer; experimentele ondersteuning voor aanraakschermen op Windows 8; melden van paginanummers en verbeterde ondersteuning voor tabellen in Adobe Reader; tabelnavigatiecommando's in tabelrijen en Windows lijstbeeldcontrols die focus krijgen; ondersteuning voor verschillende brailleleesregels; en het melden van rij- en kolomkoppen in Microsoft Excel.

### Nieuwe Functies

* NVDA ondersteunt nu Aziatische karakterinvoer bij gebruik van IME en text service invoermethodes in alle toepassingen, Inbegrepen:
 * Melden van en navigatie in kandidatenlijsten;
 * Melden van en navigatie in samenstellingsreeksen; en
 * Melden van leesreeksen.
* De aanwezigheid van onderlijning en doorstrepen wordt nu gemeld in Adobe Reader documenten. (#2410)
* Als de Windowsfunctie Plaktoetsen is ingeschakeld, zal de NVDA modifier toets zich nu gedragen als andere modifier toetsen. Dit laat u toe de NVDA modifier toets te gebruiken zonder dat u deze ingedrukt moet houden terwijl u andere toetsen indrukt. (#230)
* Automatisch melden van kolom- en rijkoppen wordt nu ondersteund in Microsoft Excel. Druk NVDA+shift+c om de rij in te stellen die kolomkoppen bevat en NVDA+shift+r om de kolom in te stellen die rijkoppen bevat. Druk een van beide commando's tweemeel snel na elkaar om de instelling ongedaan te maken. (#1519)
* Ondersteuning voor HIMS Braille Sense, Braille EDGE en SyncBraille brailleleesregels. (#1266, #1267)
* Als Windows 8 Pop-upmeldingen verschijnen, zal NVDA deze melden als "helpballonnen weergeven" is ingeschakeld. (#2143)
* Experimentele ondersteuning voor aanraakschermen in Windows 8, inclusief:
 * Lezen van tekst direct onder uw vinger terwijl u hem beweegt
 * Veel gebaren voor objectnavigatie, text review, en andere NVDA commando's.
* Ondersteuning voor VIP Mud. (#1728)
* Als in Adobe Reader een tabel een samenvatting heeft, wordt die nu weergegeven. (#2465)
* In Adobe Reader kunnen rij- en kolomkoppen van een tabel nu worden gemeld. (#2193, #2527, #2528)
* Nieuwe talen: Amharisch, Koreaans, Nepalees, Sloveens.
* NVDA kan nu autocomplete suggesties lezen bij het ingeven van emailadressen in Microsoft Outlook 2007. (#689)
* Nieuwe eSpeak stemvarianten: Gene, Gene2. (#2512)
* In Adobe Reader kunnen nu paginanummers worden weeergegeven. (#2534)
 * In Reader XI worden paginalabels gemeld waar aanwezig. Deze kunnen wijzen op veranderingen van paginanummering in verschillende secties, etc. In eerdere versies is dit niet mogelijk en worden enkel sequentiële paginanummers gemeld.
* Het is nu mogelijk om NVDA's configuratie terug te zetten naar fabrieksinstellingen ofwel door NVDA+control+r drie keer snel in te drukken of door te kiezen voor "zet de configuratie terug naar fabrieksinstellingen" in het NVDA menu. (#2086)
* Ondersteuning voor de Seika Versie 3, 4 en 5 en Seika80 brailleleesregels van Nippon Telesoft. (#2452)
* De eerste en laatste top routing knoppen op Freedom Scientific PAC Mate en Focus Brailleleesregels kunnenn nu gebruikt worden om achterwaarts en voorwaarts te scrollen. (#2556)
* Veel meer features zijn ondersteund op Freedom Scientific Focus Brailleleesregels zoals advance bars, rocker bars en bepaalde puntcombinaties voor veelgebruikte acties. (#2516)
* In toepassingen die IAccessible2 gebruiken "zoals Mozillatoepassingen) kunnen rij- en kolomkoppen van een tabel nu worden gemeld buiten bladermodus. (#926)
* Vroegtijdige ondersteuning voor de document control in Microsoft Word 2013. (#2543)
* Tekstuitlijning kan nu worden gemeld in toepassingen die IAccessible2 gebruiken zoals Mozillatoepassingen. (#2612)
* Als een tabelrij of standaard Windows lijstbeeld control met meerdere kolommen focus krijgt, kunt u nu de tabelnavigatiecommando's gebruiken om toegang te krijgen tot individuele cellen. (#828)
* Nieuwe brailletabellen: Ests graad 0, Portugees 8 punt computerbraille, Italiaans 6 punt computerbraille. (#2319, #2662)
* Als NVDA op het systeem is geïnstalleerd, kunt u een NVDA add-on package direct openen om te installeren (b.v. vanuit Windows Explorer of na het downloaden in een web browser). (#2306)
* Ondersteuning voor nieuwere modellen van Papenmeier BRAILLEX brailleleesregels. (#1265)
* Positie informatie (b.v. 1 van 4) wordt nu gemeld voor Windows Explorer lijstitems op Windows 7 en hoger. Dit omvat ook alle UIAutomation controls die de itemIndex en itemCount custom eigenschappen ondersteunen. (#2643)

### Veranderingen

* In het NVDA leescursor dialoogvenster is de Follow toetsenbord focus optie hernoemd naar Follow systeem focus voor consistentie met terminologie die elders in NVDA voorkomt.
* Als braille aan de leescursor gekoppeld is en de cursor is op een object dat geen tekstobject is (b.v. een bewerkbaar tekstveld), activeren cursor routing toetsen nu het object. (#2386)
* De optie "instellingen opslaan bij afsluiten" is nu standaard ingeschakeld voor nieuwe configuraties.
* Bij het updaten van een geïnstalleerde versie van NVDA wordt de bureaublad-sneltoets niet langer teruggezet naar control+alt+n als de gebruiker hem manueel had veranderd in iets anders. (#2572)
* De add-ons lijst in de Add-ons Manager toont nu de package naam voorafgaand aan zijn status. (#2548)
* Als u dezelfde of een andere versie van een momenteel geïnstalleerde add-on installeert, zal NVDA vragen of u de add-on wilt bijwerken in plaats van enkel een fout te tonen en de installatie af te breken. (#2501)
* Objectnavigatiecommando's (behalve het meld huidig object commando) melden nu met minder breedsprakigheid. U kan de extra informatie nog steeds krijgen door het meld huidig object commando te gebruiken. (#2560)
* Liblouis braillevertaler bijgewerkt naar 2.5.1. (#2319, #2480, #2662, #2672)
* Het NVDA Key Commands Quick Reference document is hernoemd naar Commands Quick Reference omdat het nu zowel aanraakgebaren bevat als toetsenbordcommando's.
* De Elementenlijst in bladermodus onthoudt nu het laatst getoonde elementtype (b.v. links, koppen of oriëntatiepunten) elke keer het dialoogvenster wordt getoond tijdens dezelfde sessie van NVDA. (#365)
* De meeste Metro apps in Windows 8 (b.v. Mail, Calendar) activeren niet langer de bladermodus voor de volledige app.
* Handy Tech BrailleDriver COM-Server bijgewerkt naar 1.4.2.0.

### Opgeloste Problemen

* In Windows Vista en later behandelt NVDA de Windowstoets niet langer foutief als ingedrukt bij het unlocken van Windows nadat het is gelocked door Windows+l te drukken. (#1856)
* In Adobe Reader worden rijkoppen nu correct herkend als tabelcellen; i.e. coördinaten worden gemeld en ze kunnen benaderd worden met tabelnavigatiecommando's. (#2444)
* In Adobe Reader worden tabelcellen die meer dan één kolom en/of rij overspannen nu correct behandeld. (#2437, #2438, #2450)
* Het NVDA distributiepakket controleert nu zijn integriteit voordat het wordt uitgevoerd. (#2475)
* Tijdelijke downloadbestanden worden nu verwijderd als het downloaden van een NVDA update mislukt is. (#2477)
* NVDA loopt niet langer vast als het draait als een administrator tijdens het kopiëren van de gebruikersconfiguratie naar de systeemconfiguratie (voor gebruik op Windows logon en andere beveiligde schermen). (#2485)
* Tegels op het Windows 8 Startscherm worden nu beter getoond in spraak en braille. De naam wordt niet langer herhaald, Niet Geselecteerd wordt niet langer gemeld op alle tegels, en live status informatie wordt getoond als de beschrijving van de tegel (b.v. huidige temperatuur voor de Weather tegel).
* Paswoorden worden niet langer aangekondigd bij het lezen van paswoordvelden in Microsoft Outlook en andere standaard invoercontrols die gemarkeerd zijn als beveiligd. (#2021)
* In Adobe Reader worden veranderingen aan formuliervelden nu correct weergegeven in bladermodus. (#2529)
* Verbeterde ondersteuning voor de Microsoft Word spellingscontrole, inclusief meer accuraat lezen van de huidige spellingsfout, en de mogelijkheid om de spellingscontrole te ondersteunen als u een geïnstalleerde kopie van NVDA gebruikt in Windows Vista of hoger.
* Add-ons die bestanden bevatten met niet-Engelse karakters kunnen nu in de meeste gevallen correct worden geïnstalleerd. (#2505)
* In Adobe Reader gaat de taal van de tekst niet langer verloren als ze wordt bijgewerkt of als ernaar gescrolld wordt. (#2544)
* Bij het installeren van een add-on, toont het bevestigingsdialoogvenster nu correct de vertaalde naam van de add-on indien beschikbaar. (#2422)
* In toepassingen die UI Automation gebruiken (zoals .net en Silverlight-toepassingen), is de berekening van numerieke waarden voor controls zoals sliders gecorrigeerd. (#2417)
* De configuratie voor het melden van voortgangsbalken is nu erkend voor de onbepaalde voortgangsbalken, getoond door NVDA bij het installeren, maken van een draagbare kopie, etc. (#2574)
* NVDA-commando's kunnen niet langer uitgevoerd worden vanop een brailleleesregel als een secure Windows scherm (zoals het Lock scherm) actief is. (#2449)
* In bladermodus wordt braille nu bijgewerkt als de tekst die getoond wordt verandert. (#2074)
* Als op een secure Windows scherm zoals het Lock scherm, berichten van toepassingen speaking of displaying braille direct via NVDA worden nu genegeerd.
* In bladermodus is het niet langer mogelijk buiten de onderkant van het document te gaan met pijl rechts als u op het laatste karakter bent, of bij het springen naar het einde van een container als die container het laatste item is in het document. (#2463)
* Onbelangrijke inhoud wordt niet langer foutief inbegrepen bij het melden van de tekst van dialoogvensters in webtoepassingen (specifiek in ARIA dialoogvensters zonder aria-describedby attribuut). (#2390)
* NVDA meldt of localiseert niet langer foutief bepaalde invoervelden in MSHTML documenten (b.v. Internet Explorer), specifiek waar de auteur van de webpagina een expliciete ARIA role heeft gebruikt. (#2435)
* De backspace-toets wordt nu correct behandeld bij het uitspreken van getypte woorden in Windows command consoles. (#2586)
* Celcoördinaten in Microsoft Excel worden nu opnieuw in Braille getoond.
* In Microsoft Word laat NVDA u niet langer in de steek in een alinea met lijstopmaak als u probeert te navigeren over een opsommingsteken of getal met pijl links of control + pijl links. (#2402)
* In bladermodus in Mozillatoepassingen worden de items in bepaalde lijstboxes (meer bepaald, ARIA list boxes) niet langer foutief weergegeven.
* In bladermodus in Mozillatoepassingen worden bepaalde controls, die werden weergegeven met een fout label of met enkel witruimte, nu weergegeven met het correcte label.
* In bladermodus in Mozillatoepassingen, is sommige overbodige witruimte weggelaten.
* In bladermodus in web browsers worden bepaalde afbeeldingen, die expliciet zijn gemarkeerd als decoratief (meer bepaald, met een alt="" attribuut), nu correct genegeerd.
* In webbrowsers verbergt NVDA nu inhoud die is gemarkeerd als verborgen voor schermlezers (specifiek bij gebruik van het aria-hidden attribuut). (#2117)
* Negatieve bedragen (b.v. -$123) worden nu correct uitgesproken als negatief, onafhankleijk van symboolniveau. (#2625)
* Tijdens het automatisch lezen zal NVDA niet langer foutief terugkeren naar de standaardtaal waar een regel geen zin beëindigt. (#2630)
* Lettertype informatie wordt nu correct gedetecteerd in Adobe Reader 10.1 en later. (#2175)
* Als in Adobe Reader alternatieve tekst beschikbaar is, zal enkel die tekst worden weergegeven. Vroeger bevatte die soms ook onbelangrijke tekst. (#2174)
* Waar een document een applicatie bevat, wordt de inhoud van de applicatie niet langer inbegrepen in bladermodus. Dit voorkomt onverwacht bewegen binnen de applicatie bij het navigeren. U kan interageren met de applicatie op dezelfde manier als voor embedded objecten. (#990)
* In Mozillatoepassingen wordt de waarde van spin knoppen nu correct gemeld als ze verandert. (#2653)
* Verbeterde ondersteuning voor Adobe Digital Editions zodat het werkt in versie 2.0. (#2688)
* Als u NVDA+PijlOmhoog drukt op een vervolgkeuzelijst in Internet Explorer en andere MSHTML documenten worden niet langer foutief alle items gelezen. Enkel het actieve item zal worden gelezen. (#2337)
* Spraakwoordenboeken slaan nu juist op als u een #-teken gebruikt in het patroon voor vervanging. (#961)
* Bladermodus voor MSHTML documenten (b.v. Internet Explorer) nu correct displays visible content contained binnen verborgen content (specifiek, elementen met een style of visibility:visible binnen een element met style visibility:hidden). (#2097)
* Links in Windows XP's Security Center melden niet langer random junk na hun namen. (#1331)
* UI Automation text controls (b.v. het zoekveld in het Windows 7 Startmenu) worden nu correct aangekondigd als u de muis erover beweegt in plaats van stil te blijven.
* Veranderingen van toetsenbordindeling worden niet langer gemeld tijdens automatisch lezen, wat vooral problematisch was voor meertalige documenten die Arabische tekst bevatten. (#1676)
* De hele inhoud van sommige UI Automation bewerkbare tekstcontrols (b.v. het zoekvak in het Windows 7/8 Startmenu) wordt niet langer aangekondigd elke keer dat het verandert.
* Bij het schakelen tussen groepen op het Windows 8 startscherm, kondigen ongelabelde groepen niet langer hun eerste tegel aan als de naam van de groep. (#2658)
* Bij het openen van het Windows 8 startscherm wordt de focus correct op de eerste tegel geplaatst, in plaats van te springen naar de root van het startscherm wat het navigateren verwarrend kan maken. (#2720)
* NVDA weigert niet langer te starten als het pad naar het gebruikersprofiel bepaalde multibyte karakters bevat. (#2729)
* In bladermodus in Google Chrome wordt de tekst van tabs nu correct weergegeven.
* In bladermodus worden menuknoppen nu correct weergegeven.
* In OpenOffice.org/LibreOffice Calc, werkt het lezen van rekenbladcellen nu correct. (#2765)
* NVDA kan opnieuw functioneren in de Yahoo! Mail berichtenlijst in Internet Explorer. (#2780)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2012.2.1

Deze versie pakt verschillende potentiële beveiligingszaken aan (door een upgrade naar Python 2.7.3).

## 2012.2

Hoogtepunten in deze versie zijn een ingebouwd installatieprogramma en het aanmaken van een draagbare kopie, automatische updates, eenvoudig beheer van nieuwe NVDA add-ons, aankondiging van afbeeldingen in Microsoft Word, ondersteuning voor Windows 8 Metro style apps, en verschillende belangrijke opgeloste problemen. 

### Nieuwe Functies

* NVDA kan nu automatisch controleren op updates, ze downloaden en installeren. (#73)
* Het uitbreiden van NVDA's functionaliteit is vereenvoudigd door de toevoeging van een Add-ons Manager (die u vindt in Extra in het NVDA menu). Deze laat u toe nieuwe NVDA add-on packages (.nvda-addon bestanden) die plugins en drivers bevatten te installeren en verwijderen. Merk op dat de Add-on manager geen oudere custom plugins en drivers toont die manueel zijn gekopieerd naar uw configuratiemap. (#213)
* Veel meer algemene NVDA-functies werken nu in Windows 8 Metro style apps als u een geïnstalleerde versie van NVDA gebruikt, inclusief het uitsprkeen van getypte karakters, en bladermodus voor webdocumenten (inclusief ondersteuning voor de metro versie van Internet Explorer 10). Draagbare kopieën of NVDA hebben geen toegang tot metro style apps. (#1801) 
* In bladermodus documenten (Internet Explorer, Firefox, etc.) kunt u nu springen naar het begin en voorbij het einde van bepaalde containing elementen (zoals lijsten en tabellen) met respectievelijk shift+, en ,. (#123)
* Nieuwe taal: Grieks.
* Afbeeldingen en alt-tekst worden nu gemeld in Microsoft Word Documenten. (#2282, #1541)

### Veranderingen

* Het aankondigen van celcoördinaten in Microsoft Excel gebeurt nu nà de inhoud in plaats van ervoor, en dit gebeurt nu enkel als de meld tabellen en meld tabelcelcoördinaten instellingen zijn ingeschakeld in het Documentopmaak instellingen dialoogvenster. (#320)
* NVDA is nu gedistribueerd in één pakket. In plaats van aparte draagbare en installeerbare versies, is er nu slechts één bestand dat een tijdelijke kopie van NVDA zal starten en die u toelaat het programma te installeren of een draagbare kopie aan te maken. (#1715)
* NVDA wordt nu altijd geïnstalleerd in Program Files op alle systemen. Als u een vorige installatie bijwerkt zal het ook automatisch worden verplaatst als het niet vroeger daar was geïnstalleerd.

### Opgeloste Problemen

* Met auto taalverandering ingeschakeld, wordt inhoud zoals alt-tekst voor afbeeldignen en labels voor andere bepaalde controls in Mozilla Gecko (b.v. Firefox) nu gemeld in de aangegeven taal.
* SayAll in BibleSeeker (en andere TRxRichEdit controls) stopt niet langer in het midden van een passage.
* Lijsten in de Windows 8 Explorer bestandseigenschappen (permitions tab) en in Windows 8 Windows Update worden nu correct gelezen.
* Mogelijke vastlopers opgelost in MS Word die konden voorkomen als het meer dan 2 seconden duurde om tekst van een document te verkrijgen (extreem lange regels of inhoudsopgaves). (#2191)
* Detectie van word breaks werkt nu correct waar witruimte wordt gevolgd door bepaalde leestekens. (#1656)
* In bladermodus in Adobe Reader is het nu mogelijk om te navigeren naar koppen zonder een niveau gebruik makend van snelnavigatie en de Elementenlijst. (#2181)
* In Winamp wordt braille nu correct bijgewerkt als u beweegt naar een ander item in de Playlist Editor. (#1912)
* De boom in de elementenlijst (beschikbaar voor bladermodus documenten) heeft nu de juiste afmetingen om de tekst te tonen van elk element. (#2276)
* In toepassingen die de Java Access Bridge gebruiken, worden bewerkbare tekstvelden nu correct in braille getoond. (#2284)
* In toepassingen die de java Access Bridge gebruiken, melden bewerkbare tekstvelden niet langer vreemde karakters in bepaalde omstandigheden. (#1892)
* In toepassingen die de Java Access Bridge gebruiken, wordt, als men aan het einde van een bewerkbaar tekstveld is, de huidige regel nu correct gemeld. (#1892)
* In bladermodus in toepassingen die Mozilla Gecko 14 en later gebruiken (b.v. Firefox 14), werkt snelnavigatie nu voor citaten en embedded objecten. (#2287)
* In Internet Explorer 9 leest NVDA niet langer ongewilde inhoud als de focus beweegt binnen bepaalde oriëntatiepunten of focuseerbare elementen (specifiek, een div element dat focuseerbaar is of een ARIA landmark role heeft).
* Het NVDA-icoon voor de NVDA Desktop en Startmenu snelkoppelingen wordt nu correct getoond in 64 bit versies van Windows. (#354)

### Veranderingen voor Ontwikkelaars

Deze zijn niet vertaald. We verwijzen naar [de Engelstalige versie van dit document](../en/changes.html).

## 2012.1

Hoogtepunten in deze versie zijn functies voor vlotter lezen van braille; aanduiding van documentopmaak in braille; toegang tot veel meer opmaakinformatie en verbeterde performantie in Microsoft Word; en ondersteuning voor de iTunes Store.

De rest van dit document is niet vertaald. Voor informatie over oudere versies verwijzen we naar [het Engelstalige document](../en/changes.html).

