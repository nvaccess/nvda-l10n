# ﻿NVDA NVDA_VERSION Handbuch für Entwickler

[TOC]



## Einleitung {#toc2}

Dieses Handbuch stellt informationen zur Entwicklung von NVDA und dessen Komponenten sowie ihre Übersetzungen bereit.
(HINWEIS: Dies ist lediglich eine Einführung. Für die komplette Referenz ist es für Entwickler empfehlenswert sich die Code-Dokumentation durchzulesen.)

### Eine Anmerkung zu Python {#toc3}

NVDA und dessen Erweiterungen werden in der Programmiersprache Python geschrieben.
Das Ziel dieses Handbuches ist nicht, Ihnen Python beizubringen, lediglich stellt es Beispiele zur Veranschaulichung der Syntax in Python bereit.
Die Dokumentationen und weitere Materialien sind einer oder mehreren der folgenden Bezugsquellen zu finden:

* Einen guten Einstieg in Python bietet das Buch [Python](http://openbook.galileocomputing.de/python/index.htm#_top) von Galileo computing.
* Ein sehr gutes Nachschlagewerk bietet außerdem das [deutsche Python-Wiki](http://wiki.python.de/)
* Mit Hilfe der Python-Konsole können weitere Informationen über ein bestimmtes Objekt gewonnen werden. Wenn Sie den Navigator auf das fragliche Objekt gesetzt und die Python-Konsole aufgerufen haben, können Sie mit den folgenden Befehlen weitere Informationen über dieses Objekt erhalten:
 * Um die Code-Dokumentation und die Online-Hilfe zu dem aktuellen Navigator-Objekt anzuzeigen, verwenden Sie den folgenden Befehl: help(nav) Die ausgabe des Befehls kann sehr umfangreich sein, weil nicht nur Informationen über das Navigator-Objekt selbst, sondern auch über alle seine Vorfahren angezeigt werden. Es ist daher zu empfehlen, sich den Inhalt des ausgabefensters in einer Textdatei zu speichern, um bei der weiteren Entwicklungsarbeit darauf zurückgreifen zu können.
 * Um alle Eigenschaften und Methoden des aktuellen Navigator-Objekts als Python-Wörterbuch anzuzeigen, verwenden Sie den folgenden Befehl: dir(nav)

## Übersetzung {#toc4}

Damit NVDA mehrere Sprachen bzw. Sprachräume unterstützt, muss es übersetzt und sprachspezifische Daten müssen zur Verfügung gestellt werden.

### Beschreibungen der Sonderzeichen {#toc5}

Manchmal kann es schwierig bis unmöglich sein, zwei Zeichen voneinander zu unterscheiden. 
Zwei Zeichen können beispielsweise identisch ausgesprochen werden, auch wenn es eigentlich völlig unterschiedliche Zeichen sind.
Um dieses problem zu lösen, können Zeichenbeschreibungen bereitgestellt werden, die jedes Zeichen eindeutig beschreiben.

Zeichenbeschreibungen für einen Sprachraum können in einer Datei characterDescriptions.dic bereitgestellt werden, die sich im Verzeichnis des jeweiligen Sprachraums befinden muss.
Die Datei muss im UTF-8 kodiert werden.
Leerzeilen und Zeilen, die mit einem "#" beginnen, werden ignoriert.
Alle anderen Zeilen müssen ein Zeichen gefolgt von einem Tabulator und dessen Beschreibung enthalten.

zum Beispiel:

    # Dies ist ein Kommentar
    a	Anton
    b	Berta

Ein vollständiges Beispiel finden Sie in der Datei "locale\de\characterDescriptions.dic".

### Aussprache der Symbole {#toc6}

Für Sprachausgabennutzer ist es oft sinnvoll, beim zeichenweisen Navigieren Sonderzeichen als Wörter angesagt zu bekommen.
Unglücklicherweise sprechen verschiedene Sprachausgaben die Sonderzeichen sehr unterschiedlich aus. Manche Sprachausgaben erlauben keine Kontrolle über die Aussprache von Sonderzeichen.
Hierfür können Informationen über die Aussprache von Sonderzeichen in NVDA mitgegeben werden.

Dieses kann sprachspezifisch in der im UTF-8 kodierten Datei namens "Symbols.dic" im Verzeichnis des jeweiligen Sprachraums erfolgen.
Leerzeilen und Zeilen, die mit einem "#" beginnen, werden ignoriert.
Alle Sprachräume erben die Sonderzeichenaussprache des Englischen.

Die Datei enthält dabei zwei Abschnitte.

#### Komplexe Symbole definieren {#toc7}

Der erste Abschnitt ist optional und enthält Definitionen komplexer Symbole in Form regulärer Ausdrücke.
Komplexe Symbole sind nicht einfach nur Sonderzeichen oder Sequenzen von Sonderzeichen, die durch Wörter ersetzt werden sollen. Stattdessen erfordern sie eine kompliziertere Überprüfung auf Übereinstimmung.
Ein Beispiel ist der Punkt als Satzzeichen im Deutschen.
Da der Punkt mehrere Bedeutungen hat, ist eine komplexere Überprüfung erforderlich um zu bestimmen, ob er sich auch tatsächlich am Ende eines Satzes befindet.

Der Abschnitt für komplexe Symbole beginnt mit der folgenden Zeile:

    complexSymbols:

Die einzelnen Zeilen innerhalb dieses Abschnittes enthalten einen Namen für ein Symbol, ein Tab-Zeichen und einen Regulären Ausdruck für ein Symbol.

Zum Beispiel:

    . Satzende	(?<=[^\s.])\.(?=[\"')\s]|$)

Da ein jeder Sprachraum die komplexen Symbole des englischen Sprachraumes erbt, brauchen Sie diese in Ihrer Symboldefinition nicht noch einmal aufzuführen.

#### Symbol-Informationen definieren {#toc8}

Der zweite Abschnitt enthält Informationen darüber, ob und wie Symbole ausgesprochen werden. 
Er beginnt mit der Zeile:

    symbols:

Die Zeilen dieses Abschnitts enthalten mehrere Felder, die durch Tabstopps getrennt sind.
Die einzigen Pflichtfelder sind der Name des Symbols und der Ersatztext.
Für leere Felder wird der Standardwert verwendet.

Folgende Felder sind verfügbar:

* Name: Der Name eines Symbols
Meistens wird hier das zu verarbeitende Sonderzeichen oder der name eines komplexen Symbols angegeben. Einige Sonderzeichen können nicht eingegeben werden. Hierfür können die folgenden Sequenzen verwendet werden:
* \0: Null
* \t: Tabulator
* \n: Zeilenumbruch
* \r: Wagenrücklauf
* \f: Seitenvorschub
* \#: #-Zeichen (benötigt einen Backslash, da dieses #-Zeichen sonst als Kommentar angesehen wird)
* Ersatztext: der Text, der anstelle des Symbols ausgesprochen werden soll.
* Ebene: die Symbolebene, ab der das Symbol gesprochen werden soll.

Die Symbolebene kann vom Anwender konfiguriert werden und gibt die Menge an auszusprechenden Sonderzeichen an. 
Dieses Feld sollte einen der Werte  "none", "some", "most", "all" oder  "char" enthalten oder "-", um den Standardwert zu erzwingen.
Die Spezifikation "char" bedeutet, dass das Symbol nur bei der zeichenweisen Navigation verarbeitet wird. 
Standardmäßig wird hier der vom Englischen geerbte Wert verwendet oder "all", falls es nichts zu erben geben sollte.
* Beibehalten: Dieses Feld muss immer dann belegt sein, wenn ein bestimmtes Symbol unverarbeitet an den Synthesizer weitergegeben werden soll, um eine korrekte Aussprache zu ermöglichen. 
Beispiele hierfür sind Sonderzeichen, die Sprachpausen verursachen, wie z.B. der Punkt, das Komma etc.
Dieses Feld kann die folgenden Werte enthalten:
* never: Das Symbol wird nie beibehalten.
* always: das Symbol wird immer beibehalten.
* norep: Das Symbol wird nur dann beibehalten, wenn es nicht ersetzt wird (z.B. wenn der Anwender die Satzzeichen- und Symbolebene niedriger eingestellt hat, als für das betreffende Symbol.
* -: verwendet den Standardwert.
Standardmäßig wird der Wert vom englischen Sprachraum vererbt oder "never" verwendet, falls es nichts zu erben geben sollte.

Am ende der Zeile kann schließlich noch ein Anzeigename für ein Symbol vergeben werden.
Dieser Name wird Anwendern angezeigt, wenn sie die komplexen Symbole bearbeiten wollen. Er kann auch von übersetzern verwendet werden, um übersetzte Namen für die englischen komplexen Symbole bereitzustellen.

Hierzu einige Beispiele:

    (	runde Klammer auf	most

Dies bedeutet, dass das Zeichen "(" als "Runde Klammer auf" gesprochen werden soll, wenn der Anwender die Satzzeichen- und Symbolebene auf "meiste" oder "alle" eingestellt hat.

    ,	Komma	all	always

Dies bedeutet, dass das Zeichen "," als "Komma" gesprochen werden soll, wenn als Satzzeichen- und Symbolebene "all" eingestellt ist. Außerdem wird das Zeichen immer unverändert an den Synthesizer übergeben, um Sprechpausen korrekt zu setzen.

    . sentence ending	point	# . fin de phrase

Diese Zeile stammt aus der französischen Datei symbols.dic.
Sie besagt, dass das komplexe Symbol ". sentence ending" als "point" gesprochen werden soll..
Ebene und Einstellung zum Beibehalten des Symbols sind hier nicht angegeben, werden also vom englischen Sprachraum geerbt.
Ein anzeigename wird ebenfalls angegeben, sodass französische nvda-Nutzer wissen, was dieses Symbol bedeutet.

Bitte sehen Sie sich die Datei locale\en\symbols.dic für die englischsprachigen Symboldefinitionen an.

## Plugins {#toc9}
### Übersicht {#toc10}

Mittels der Plugins erhalten Sie die Möglichkeit, das Verhalten global oder in bestimmten Anwendungen nach Ihren Wünschen anzupassen.
Das sind unter anderem:

* Auf bestimmte Ereignisse reagieren, wenn sich zum Beispiel der Fokus verschiebt oder wenn sich die Eigenschaften eines Objekts ändern.
* Befehle implementieren, die an bestimmte Tastendrücke oder andere Eingabemethoden gebunden werden können.
* Das Verhalten bestimmter Steuerelemente beeinflussen oder weitere Funktionen hinzufügen.
* Unterstützung für Textinhalte oder komplexe Dokumente anpassen oder hinzufügen.

Dieser Abschnitt enthält lediglich eine Einführung in die Entwicklung von Plug-ins. Schauen Sie sich die Code-Dokumentation für eine komplette Referenz an.

### Typen der Plugins {#toc11}

Folgende zwei Typen der Plugins gibt es:

* Anwendungsmodule: Enthalten speziellen Code für eine bestimmte Anwendung.
Ein Anwendungsmodul nimmt Ereignisse für eine bestimmte Anwendung entgegen, auch wenn die Anwendung momentan nicht fokussiert ist.
Wenn eine Anwendung fokussiert ist, kann der Nutzer sämtliche Befehle ausführen, die im Anwendungsmodul definiert und an Eingabemethoden zugewiesen wurden.
* Allgemeine Plugins: Diese enthalten Code, die überall, auch in allen Anwendungen funktionieren. 
Dabei nehmen Sie alle Ereignisse von allen Elementen im Betriebssystem entgegen.
Befehle, die in allgemeinen Plugins an Eingabemethoden zugewiesen wurden, können unabhängig davon ausgeführt werden, welche Anwendung grade aktiv ist.

Wenn Sie vorhaben die Zugänglichkeit von NVDA für bestimmte Anwendungen zu verbessern, sind die Anwendungsmodule empfehlenswert.
Im Gegensatz, wenn Sie vorhaben globalen Code für NVDA zu entwickeln, der systemweit zugänglich sein soll, zum Beispiel um sich die Signalstärke von Funknetzwerken anzeigen zu lassen, ist ein allgemeines Plugin empfehlenswert.

Anwendungsmodule und die allgemeinen Plugins sind sehr ähnlich.
Dies sind beides Python-Quelldateien (mit der Erweiterung .py), die dabei eine spezielle Klasse definieren, die sämtliche Ereignisse, Skripte und Komponenten beinhalten und die Zugriffssteuerung der eigenen Klassen, Textpassagen und komplexen Dokumenten definieren.
Dabei unterscheiden sie sich jedoch in einigen Punkten.

Die folgenden Abschnitte beschreiben separat die Anwendungsmodule und die allgemeinen Plugins Anschließend werden wieder allgemeinere Punkte erläutert.

### Grundlagen eines Anwendungsmoduls {#toc12}

Anwendungsmodule besitzen die Erweiterung .py und haben den gleichen Namen wie die Anwendungen, für die sie verwendet werden sollen.
Ein Anwendungsmodul für den Editor müsste zum Beispiel notepad.py heißen, weil die ausführbare Datei des Editors notepad.exe heißt.

Anwendungsmodule müssen im Unterordner "appModules" der Benutzerkonfiguration von nvda liegen. 
Weitere Informationen über den Standort Ihres benutzerspezifischen Konfigurationsverzeichnisses finden Sie im Benutzerhandbuch von NVDA.

Anwendungsmodule müssen eine Klasse "appModule" definieren, die alle Eigenschaften und Methoden von appModuleHandler.AppModule erbt.
Diese Klasse kann dann Ereignisse, Scripte, Eingabemethodenzuweisungen und anderen Code enthalten.
Details hierzu lesen Sie weiter unten.

Sobald NVDA erkennt, dass eine bestimmte Anwendung gestartet wird, wird das jeweilige Anwendungsmodul geladen.
Wenn die betreffende Anwendung oder NVDA beendet wird, wird auch das Anwendungsmodul wieder aus dem Speicher entfernt.

### Beispiel 1: Ein Anwendungsmodul erzeugt Signaltöne bei Ereignissen, wenn sich der Fokus verändert {#Example1}

Das folgende anwendungsmodul gibt jedes mal einen Signalton wieder, wenn sich innerhalb des Editors der Fokus ändert.
Dieses Beispiel veranschaulicht den grundsätzlichen Aufbau eines Anwendungsmoduls.

Fügen Sie den Folgenden Code zwischen den Start- und Endmarken (jedoch nicht die Marken selbst) in eine Datei mit dem Namen notepad.py und speichern Sie diese im Unterverzeichnis appmodules in ihrer benutzerspezifischen nvda-Konfiguration.
Übernehmen Sie hierbei auch alle Tab- und Leerzeichen.

Starten Sie anschließend NVDA neu oder wählen Sie Plugins neu laden" aus dem Menü Extras, damit die Änderungen wirksam werden.

Öffnen Sie zu guter Letzt den Editor und bewegen Sie den Fokus innerhalb der Anwendung (z.B. innerhalb des Menüs, innerhalb von Dialogfeldern, etc.).
Sie sollten nun jedes Mal einen Signalton hören, wenn sich der Fokus ändert.
Wenn Sie sich jedoch außerhalb des Editors (z. B. im Explorer) befinden, sollten Sie keine Signaltöne hören.

    --- Beginn ---
    # NVDA-Anwendungsmodul für den Editor
    # Beispiel 1 aus dem Entwicklerhandbuch
    
    import appModuleHandler
    
    class AppModule(appModuleHandler.AppModule):
    
    	def event_gainFocus(self, obj, nextHandler):
    		import tones
    		tones.beep(550, 50)
    		nextHandler()
    
    --- Ende ---

Dieses Anwendungsmodul beginnt mit zwei Kommentarzeilen, die den Zweck des Anwendungsmoduls beschreiben.

Anschließend wird das Modul "appmodule" importiert, welches die Basisklasse für Anwendungsmodule zur Verfügung stellt.

Als nächstes wird eine Klasse namens AppModule definiert, die von appModuleHandler.AppModule abgeleitet ist.

Innerhalb der Klasse werden ein oder mehr Ereignisse, scripte oder Eingabemethodenzuweisungen definiert.
Dieses Beispiel definiert ein Ereignis namens gainfocus (event_gainFocus), das bei jeder Ausführung einen kurzen Signalton abspielt.
Die Implementierung des Ereignisses ist für dieses Beispiel noch nicht wichtig, wichtig ist lediglich die Definition der Klasse.

Ereignisse werden weiter unten in diesem Handbuch näher erläutert.

Denken Sie - wie bei anderen Beispielen in diesem handbuch - daran, das erstellte anwendungsmodul zu löschen und NVDA neu zu starten bzw. die Plugins neuzuladen, wenn Sie Ihre Tests abgeschlossen haben, um das ursprüngliche Verhalten von NVDA wiederherzustellen.

### Grundlagen der Allgemeinen Plugins {#toc14}

Globale Plug-ins sollten die Erweiterung .py besitzen und einen kurzen Namen haben, der ihren Zweck beschreibt.

Globale Plugins müssen im unterordner "GlobalPlugins" des benutzerspezifischen Konfigurationsverzeichnisses liegen. 
Weitere Informationen darüber, wo Sie das benutzerspezifische Konfigurationsverzeichnis finden, finden Sie im NVDA-Benutzerhandbuch.

Globale Plugins müssen eine Klasse namens GlobalPlugin, definieren, die ein direkter Nachkomme von globalPluginHandler.GlobalPlugin ist.
Diese klasse kann anschließend Ereignisse, Script-Methoden, Eingabemethoden-zuweisungen und anderen Code enthalten.
All dies wird im Folgenden behandelt.

NVDA lädt alle globalen Plug-ins, sobald er gestartet wird und entlädt sie beim Beenden wieder.

### Beispiel 2: Eine Standarderweiterung - Ein Skript zur Ansage der NVDA-Version {#toc15}

Das folgende Beispiel erlaubt Ihnen, sich von überall im System aus mit der Tastenkombination NVDA+Umschalt+V die NVDA-Version anzeigen zu lassen.
Das Beispiel dient lediglich dazu, den grundlegenden Aufbau globaler Plugins zu veranschaulichen.

Kopieren sie den folgenden Text zwischen den Anfangs- und Endmarkern (jedoch nicht die Marker selbst), in eine Datei namens beispiel2.py und speichern Sie diese im Unterofdner "GlobalPlugins" Ihres NVDA-Konfigurationsverzeichnisses.
Lassen Sie dabei alle Tabs und Leerzeichen stehen.

Starten Sie nach dem Speichern entweder NVDA neu oder wählen aus dem menü Extras des nvda-Menüs den Befehl Plug-ins neu laden.

Von nun an können Sie NVDA+Umschalt+V drücken, um die NVDA-Version angesagt und in Braille angezeigt zu bekommen.

    --- Beginn ---
    # Plugin zur Ausgabe der Versionsinformationen in NVDA
    # Beispiel 2 aus dem Entwicklerhaldbuch
    
    import globalPluginHandler
    import ui
    import versionInfo
    
    class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    
    	def script_announceNVDAVersion(self, gesture):
    		ui.message(versionInfo.version)
    
    	__gestures={
    		"kb:NVDA+Shift+V": "announceNVDAVersion",
    	}
    
    --- Ende ---

Dieses globale Plugin beginnt mit zwei Kommentarzeilen, die den Zweck der Datei kurz beschreiben.

Anschließend wird das Modul globalPluginHandler importiert, sodass das Plug-in Zugriff auf die Basisklasse GlobalPlugin hat. 

Außerdem werden noch die Module UI und Versioninfo importiert, damit das Plugin die Versionsinformationen ausgeben kann. 

Als nächstes wird eine Klasse GlobalPlugin, definiert, die ein Nachkomme von globalPluginHandler.GlobalPlugin ist.

Innerhalb dieser Klasse werden ein oder mehrere Ereignisse, Scripte oder Eingabemethoden-Zuweisungen definiert.
In diesem Beispiel enthält die Klasse ein Script, das die Versionsinformationen ausgibt und eine eingabemethoden-Zuweisung, die dieses Script an NVDA+Umschalt+V zuweist.
Die Details des Scripts und der Eingabemethodenzuweisung sind für dieses Beispiel jedoch nicht von Belang.
Das wichtigste ist die Klasse selbst.

Um das urspründliche Verhalten von NVDA wiederherzustellen, müssen Sie die globale Plugin-Datei löschen und NVDA anschließend neu starten oder die Plugins neu laden.

### NVDA-Objekte {#toc16}

NVDA stellt Steuerelemente und andere Bestandteile von Benutzeroberflächen in Form von NVDA-Objekten dar.
Diese Objekte enthalten standardisierte Eigenschaften wie name, Typ, Wert, Status und Beschreibung. Dies erlaubt anderen Teilen von NVDA, diese Informationen über ein Objekt in verallgemeinerter Form abzufragen oder darzustellen.
Die Schaltfläche "OK" in einem Dialogfeld wird beispielsweise den Namen "OK" und den Steuerelementtyp "Schaltfläche" besitzen.
So ähnlich würde beispielsweise ein Kontrollkästchen mit der Beschriftung "Ich stimme zu" den Namen "Ich stimme zu", den Typ Kontrollkästchen und - falls aktiviert - den Status aktiviert besitzen.

Auch wenn es unterschiedliche Komponentenbausätze für Benutzeroberflächen und Zugänglichkeitsschnittstellen gibt,  abstrahieren NVDA-Objekte diese unterschiede zu einer einheitlichen Form, gleichgültig, mit welchem Komponentenbausatz ein Steuerelement erzeugt wurde oder über welche ugänglichkeitsschnittstelle darauf zugegriffen wird. 
Der oben angesprochene Schalter "OK" könnte also beispielsweise ein Java-Objekt sein. Genauso gut könnte er aber auch ein MSAA-Objekt, ein iAccessible2-Objekt oder ein UIA-Element sein.

NVDA-Objekte haben viele Eigenschaften.
einige der nützlichsten sind:

* name: Die Beschriftung des Steuerelements
* role: Der Typ des Steuerelements, repräsentiert durch eine der ROLE_*-Konstanten aus dem Anwendungsmodul controltypes
Schaltfläche, Dialogfeld, Eingabefeld, Fenster und Kontrollkästchen sind nur einige Beispiele für Steuerelementtypen.
* states: Status des Steuerelements, repräsentiert durch einen Satz von 0 oder mehr STATE_*-Konstanten as dem Modul controltypes.
hervorhebbar, hervorgehoben, ausgewählt, auswählbar, erweitert, reduziert und aktiviert sind nur einige Beispiele für den Status.
* value: Der Wert des Steuerelements z.B. der aktuelle Stand einer Fortschrittsanzeige oder der aktuelle gewählte Eintrag in einem Kombinationsfeld.
* description: Eine kurze Beschreibung, die den Zweck des Steuerelements erläutert (üblicherweise identisch mit der Minihilfe).
* location: Der Abstand eines Objektes von der oberen linken Ecke des Bildschirms sowie dessen Breite und Höhe in Form von Bildschirmkoordinaten.
* parent: Das übergeordnete Objekt
Das Übergeordnete Objekt eines Listeneintrags ist beispielsweise die Liste, die ihn enthält.
* next: Das nächste Objekt in der logischen Reihenfolge
* previous: Das vorherige Objekt in der logischen Reihenfolge
* firstChild: Der erste direkte Nachkomme eines Objekts.
Der erste Nachkomme einer Liste ist beispielsweise deren erster Eintrag.
* lastChild: Der letzte Nachkomme eines Objekts.
  * children: Eine Liste aller Nachkommen eines Objekts (beispielsweise alle Einträge eines Menüs).
-

Es gibt auch noch Eigenschaften, die sich auf die vereinfachte Navigation beziehen wie "simpleParent", "simpleNext", "simpleFirstChild" und "simpleLastChild".
Diese entsprechen den oben beschriebenen Eigenschaften, NVDA filtert hier jedoch nutzlose Objekte aus.
Diese eigenschaften werden immer dann verwendet, wenn der vereinfachter Darstellungsmodus in NVDA aktiviert ist, was der Normalfall ist.
Die vereinfachten Eigenschaften sind zwar leichter zu verwenden, die komplexeren Eigenschaften spiegeln jedoch diezugrundeliegende Objektstruktur des Betriebsystems wesentlich besser wieder.

Wenn Sie NVDA-Plugins entwickeln, spielt es meistens keine Rolle, mit welchem Komponentenbausatz die Benutzeroberfläche erstellt wurde oder mit welcher Zugänglichkeitsschnittstelle Sie darauf zugreifen müssen. Meistens können sie mit Standardeigenschaften auf die Objekte zugreifen wie z. B. dessen Namen, Wert oder Status.
Wenn Plug-ins komplexer werden, kann es jedoch erforderlich werden tiefer in die Objekte abzusteigen, um Komponentenbausatz- oder zugänglichkeitsschnittstellen-spezifische Informationen zu erhalten.

Es gibt drei Möglichkeiten, wie Plug-ins nvda-Objekte verwenden können:
* Die meisten Ereignisse verarbeiten ein Argument, das dasjenige Objekt angibt, auf das sich das Ereignis bezieht.
Das Ereignis event_gainfocus übernimmt beispielsweise dasjenige Objekt als Parameter, das soeben den Fokus bekommen hat.
* Skripte und Ereignisse können Objekte verarbeiten Wie z. B. das aktuell hervorgehobene Objekt, das aktuelle navigatorobjekt oder den Desktop.
Anschließend könnte auf andere Objekte bezug genommen und Informationen von ihnen abgerufen werden.
* Das Plug-in könnte auch eine eigene NVDA-Objektklasse definieren, um ein bestimmtes Steuerelement darin einzuschließen. Solche benutzerdefinierten NVDA-Objekte können einem NVDA-Objekt neue Fnktionalität geben, dessen Eigenschaften umwandeln, etc.

Ebenso wie Anwendungsmodule oder globale Plug-ins können nvda-Objekte Scripte, Ereignisse und Eingabemethoden-zuweisungen enthalten.

### Skripte und Tastenanbindung {#toc17}

Anwendungsmodule, globale Plugins und NVDA-Objekte können Methoden enthalten, die an Ereignisse wie z.B. Tastendrücke zugewiesen werden können.
Auf solche Methoden greift NVDA mit Hilfe von Skripten zu.

Ein Skript ist eine standard-Python-Instanzmethode, deren Name mit "Script_" beginnt, wie z. B. "script_sayDateTime".

Eine Skriptmethode verarbeitet zwei Argumente:

* self: Eine Referenz auf das Anwendungsmodul, globale Plugin oder NVDA-Objekt, von dem aus das Skript aufgerufen wird.
* gesture: Ein Eingabemethoden-Objekt, das die Ausführung des Script verursacht hat.

Neben dem eigentlichen Skript muss noch ein Eingabemethoden-Objekt definiert werden, damit NVDA bekannt ist, durch welches Ereignis das Script aufgerufen werden soll.

Um eine Eingabemethode an ein Skript zuzuweisen,  kann ein spezielles Python-Wörterbuch namens "__gestures" als Klassenvariable definiert werden. Dies kann innerhalb eines anwendungsmoduls, eines globalen Plug-ins oder eines NVDA-Objekts geschehen.
Diese Wörterbücher sollten Einträge mit den Eingabemethoden enthalten, die auf die entsprechenden Scripts zeigen. Der name muss hierbei ohne das Präfix "Script_" angegeben werden.

Es gibt zwar noch kompliziertere und dynamischere Methoden, Eingabemethoden zuzuweisen, das Wörterbuch __gestures ist jedoch der einfachste Weg.

Der Bezeichner für eine Eingabemethode ist eine einfache Zeichenfolge, die die Eingabemethode repräsentiert.
Er enthält einen zweistelligen Code, der die Eingabequelle beschreibt, einen optionalen Gerätenamen in Klammern, einen Doppelpunkt und eine oder mehrere Tastenbezeichnungen, die durch ein Pluszeichen voneinander getrennt werden.

Einige Beispiele für eingabemethodenbezeichner sind:

* "kb:NVDA+Shift+V"
* "br(freedomScientific):leftWizWheelUp"
* "kb(laptop):NVDA+T"

Aktuell werden folgende Eingabequellen unterstützt:

* kb: Tastatureingaben
* br: Tastendrücke und andere navigierende Eingaben an Braillezeilen

Wenn NVDA eine Tastatureingabe registriert, sucht es in eine bestimmten Reihenfolge nach einr entsprechenden Eingabemethoden-Zuweisung.
Wurde eine Zuweisung gefunden, so wird das entsprechende Skript ausgeführt. Weder wird weiter nach Eingabemethoden-Zuweisungen gesucht, noch wird der Tastendruck ans Betriebssystem weitergereicht.

Folgende Reihenfolge wird bei der Suche nach Eingabemethodenzuweisungen verwendet:

* Geladene globale Plugins
* Anwendungsmodul der aktiven Anwendung
* Der Interceptor des NVDA-Objekts, das den Fokus hat (wie beispielsweise ein virtueller Puffer).
* Das NVDA-Objekt, welches den Fokus besitzt
* Globale, eingebaute Befehle wie beispielsweise das Beenden von NVDA, die Objektnavigation, usw.

### Beispiel 3: Ein globales Plugin zum Aufspüren von FensterKlassen und Steuerelementen {#toc18}

Das folgende globale Plugin bewirkt, dass Sie NVDA+Pfeil_links drücken können, um die Fensterklasse des aktuellen Fensters zu erfahren. Ebenso können Sie NVDA+Pfeil_rechts drücken, um die Steuerelement-id des aktuellen Objekts zu erfahren.
Das Beispiel veranschaulicht, wie Sie ein Skript und eine Eingabemethodenzuweisung in einem globalen Plugin definieren.

Speichern Sie den Text innerhalb der Start- und Endmarken (jedoch nicht die Marken selbst) in einer Datei beispiel3.py im Unterverzeichnis "globalPlugins" ab.
Achten Sie dabei darauf, alle Tabs und Leerzeichen exakt zu übernehmen.

Starten Sie nach dem Speichern entweder NVDA neu oder wählen Sie im NVDA-Menü den Befehl "Plugins neu laden" aus dem Menü "Extras".

    --- Beginn ---
    # Hilfs-Skript für NVDA
    # Beispiel 3 aus dem Entwicklerhandbuch
    
    import globalPluginHandler
    import ui
    import api
    
    class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    
    	def script_announceWindowClassName(self, gesture):
    		focusObj = api.getFocusObject()
    		name = focusObj.name
    		windowClassName = focusObj.windowClassName
    		ui.message("Das Fenster %s besitzt die Fensterklasse %s" % (name, windowClassName))
    
    	def script_announceWindowControlID(self, gesture):
    		focusObj = api.getFocusObject()
    		name = focusObj.name
    		windowControlID = focusObj.windowControlID
    		ui.message("Das Fenster %s hat die Steuerelementnummer %d" % (name, windowControlID))
    
    	__gestures = {
    		"kb:NVDA+leftArrow": "announceWindowClassName",
    		"kb:NVDA+rightArrow": "announceWindowControlID",
    	}
    
    --- Ende ---
### Ereignisse {#toc19}

wenn NVDA ein Betriebssystemereignis erkennt, so wird dieses abstrahiert und ein eignes Ereignis bei nvda-Objekten ausgelöst.

Wenngleich die meisten Ereignisse zu bestimmten NVDA-Objekte gehören  (wie z. B. Umbenennungen, Fokuserhalt, Statusänderung, etc.), können sie auf unterschiedlichen Ebenen verarbeitet werden.
Wird ein Ereignis behandelt, so wird es nicht mehr weitergereicht.
Das Weiterreichen des Ereignsses kann jedoch durch Code innerhalb der Ereignisbehandlungsroutine erzwungen werden, falls nötig.

Ereignisse werden in folgender Reihenfolge abgearbeitet:

* Durch geladene globale Plugins.
* Durch das Anwendungsmodul, das dem Objekt zugeordnet wurde, bei dem das Ereignis eintrat.
* Durch den Interceptor (falls vorhanden) der dem Objekt zugeordnet wurde, bei dem das Ereignis eintrat.
* Durch das NVDA-Objekt selbst.

Ereignisse sind Python-Instanzmethoden, deren namen mit event_ beginnen, gefolgt von dem Namen des eigentlichen Ereignisses   (wie z. B. gainFocus).

Diese Ereignismethoden verarbeiten unterschiedliche Argumente, abhängig davon, auf welcher Ebene sie aufgerufen werden.

Wenn ein Ereignis, das sich auf ein NVDA-Objekt bezieht im NVDA-Objekt selbst definiert wird, akzeptiert es ein Argument namens "self", das die Instanz des NVDA-Objekts darstellt.
einige Ereignisse verarbeiten noch zusätzliche Argumente, dies ist allerdings ziemlich selten.

Wird ein Ereignis, das sich auf ein NVDA-Objekt bezieht, in einem globalen Plug-in, in einem Anwendungsmodul oder in einem Interceptor definiert, verarbeitet es die folgenden Argumente:

* self: Die Instanz des Anwendungsmoduls, des globalen Plugins oder des Interceptors.
* obj: Das NVDA-Objekt, welches das Ereignis ausgelöst hat.
* nextHandler: Eine Funktion, die bei ihrem Aufruf das Ereignis weiter durchreicht.

einige häufig verwendete NVDA-Objektereignisse sind:

* foreground: Dieses Objekt wurde zum neuen Vordergrundfenster d.h. zur neuen aktiven Anwendung.
* gainFocus: Das Objekt erhielt soeben den Fokus.
* loseFocus: Das Objekt hat den Fokus verloren.
* nameChange: Das Objekt wurde umbenannt.
* valueChange: In dem Objekt wurde der Wert geändert (z. B., wenn in einem Kombinationsfeld ein neuer Eintrag ausgewählt wurde).
* stateChange: Das Objekt änderte seinen Status (aktivieren / deaktivieren von Kontrollfeldern, etc.).
* caret: Wird ausgelöst, sobald sich der System-Cursor innerhalb des Objektes bewegt.
* locationChange: Wird ausgelöst, sobald ein Objekt physisch auf dem Bildschirm verschoben wird.

Es gibt zwar noch viel mehr, die oben aufgeführten Ereignisse sind jedoch die gebräuchlichsten.

Ein Beispiel für eine Ereignisbehandlungsroutine finden Sie im Beispiel 1.

### Die Schlafmodus-Variablen der Anwendungsmodule {#toc20}

Anwendngsmodule besitzen eine sehr nützliche Eigenschaft namens "aleepmode". Diese Eigenschaft deaktiviert, wenn sie auf True gesetzt wird, fast alle Funktionen von NVDA.
Der Schlafmodus ist nützlich für anwendung, die eigene Bildschirmlese-Funktionen besitzen oder für Spiele, bei denen man volle Kontrolle über die Tastatur benötigt.

Obwohl der Anwender den Schlafmodus mit NVDA+Umschalt+S ein- und ausschalten kann, kann der Entwickler trotzdem die Standardeinstellung des Schlafmodus vorgeben.
Dies geschied einfach durch setzen der Eigenschaft sleepMode auf True in der Klasse des Anwendungsmoduls.

### Beispiel 4: Ein Schlafmodus-Anwendungsmodul {#toc21}

Der folgende Code kann kopiert und im Anwendungsmodul-Verzeichnis in einer Datei für eine Anwendung gespeichert werden, für die Sie den Schlafmodus aktivieren möchten.
Die Datei muss, wie immer, die Endung .py erhalten.

    --- Beginn ---
    import appModuleHandler
    
    class AppModule(appModuleHandler.AppModule):
    
    	sleepMode = True
    
    --- Ende ---
### Eigene NVDA-Objektklassen angeben {#toc22}

Um die Zugänglichkeit von anwendungen mit NVDA zu verbessern, ist das Definieren von eigenen NVDA-Objektklassen der effektivste Weg.
Dies erlaubt Ihnen, die gesamte für ein Steuerelement relevante Logik an einer einzigen Stelle zusammenzufassen, anstatt sie auf verschiedene Plugin-Ereignisse aufzuteilen.

die definition einer eigenen Objektklasse erfolgt in zwei Schritten:

* Definieren der NVDA-Objektklasse und deren Skripte, Ereignisse, Eigenschaften und Eingabemethoden-Zuweisungen
* NVDA mitteilen, dass diese Klasse in bestimmten Situationen zu verwenden ist, indem sie  sie mit Hilfe der Methode "chooseNVDAObjectOverlayClasses" auf Plugin-Ebene einbinden.

Wenn Sie eigene NVDA-Objektklassen definieren, haben Sie viele NVDA-Objekt-basisklassen zur Auswahl.
Diese Basisklassen enthalten die grundlegene Unterstützung von Betriebssystem- oder Zugänglichkeitsschnittstellen wie win32, MSAA oder Java Access Bridge.
Sie sollten in der benutzerdefinierten Objektklasse üblicherweise die höchste Basisklasse erben.
Wenn Sie beispielsweise eine benutzerdefinierte Fensterklasse bei einem Steuerelement verwenden wollen, dessen Fensterklasse "edit" ist und dessen Steuerelement-ID 15 ist, werden Sie vermutlich von der Klasse "NVDAObjects.Window.Window" erben wollen, weil es sich bei dem besagten Objekt um ein Fenster handelt.
so ähnlich werden Sie Ihr Objekt von der Klasse "NVDAObjects.IAccessible.IAccessible" ableiten, wenn Sie nach der Eigenschaft "accrole" suchen wollen.
Außerdem sollten Sie genau wissen, welche Eigenschaften Sie bei Ihrer benutzerdefinierten Klasse überschreiben wollen.
Wenn Sie beispielsweise eine iAccessible-spezifische Eigenschaft wie "shouldAllowIAccessibleFocusEvent" überschreiben wollen, müssen Sie Ihr Objekt von  "NVDAObjects.IAccessible.IAccessible" ableiten.

Die Methode "chooseNVDAObjectOverlayClasses" kann in Anwendungsmodulen oder globalen Plugins eingesetzt werden.
Dabei verarbeitet sie drei Argumente:

1. self: Die Instanz des anwendungsmoduls oder des globalen Plugins.
1. obj: Das Objekt, für das eine neue Klasse ausgewählt werden soll.
1. clsList: Eine Python-Liste mit Klassen, die für das Objekt benutzt werden sollen.

Innerhalb dieser Methode sollten Sie entscheiden, welche benutzerdefinierten Objektklasse(n) das objekt verwenden soll, indem Sie dessen Eigenschaften prüfen.
Wenn eine benutzerdefinierte Klasse verwendet werden soll, können Sie sie in die Klassenliste (üblicherweise vorn) einfügen. Sie können auch von NVDA ausgewählte Klassen aus der Liste entfernen, dies ist jedoch selten erforderlich.

### Beispiel 5: Das Eingabefeld im Editor beschriften, welches ein eigenes NVDA-Objekt verwendet {#toc23}

Dieses Anwendungsmodul bringt NVDA dazu, das Haupt-eingabefeld des Editors mit "Inhalt" zu benennen.
Das bedeutet, dass NVDA "Inhalt Eingabefeld" sagen wird, sobald das Editorfenster den Fokus erhält.

Der folgende Code kann kopiert und in eine Textdatei eingefügt werden, welche den Namen notepad.py tragen muss und im Ordner AppModules gespeichert wird.

    --- Beginn ---
    import appModuleHandler
    from NVDAObjects.window import Window
    
    class AppModule(appModuleHandler.AppModule):
    
    	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
    		if isinstance(obj, Window) and obj.windowClassName == "Edit" and obj.windowControlID == 15:
    			clsList.insert(0, LabelledEditField)
    
    class LabelledEditField(Window):
    
    	name = "Inhalt"
    
    --- Ende ---
## Verpacken von Code als NVDA-Erweiterungen {#toc24}

Um das Verteilen und die Installation von Plug-ins und Treibern zu erleichtern, können diese in einzelne Paketdateien verpackt werden, die dann mit Hilfe der Funktion "Erweiterungen verwalten" installiert werden können. Diese Funktion ist im Menü "Extras" zu finden. 
Erweiterungspakete werden nur von NVDA 2012.2 und neuer unterstützt.
Ein Paket ist einfach eine Datei im Zip-Format mit der Erweiterung .nvda-addon, die folgende Dateien und Verzeichnisse enthalten kann:

* Eine Manifest-Datei mit grundlegenden Informationen über das Paket.
* Ordner mit Plugins und Treibern, die in NVDA installiert werden sollen.
* Zusätzlichen Code, der bei der Installation bzw. der Deinstallation des Pakets ausgeführt werden soll.
* Übersetzungen der in Ihren Plugins und Treibern verwendeten Meldungen für unterschiedliche Srachräume.

++ Nicht-ASCII-Dateinamen in Zip-Archiven ++
wenn Ihr Archiv Dateien enthält, in deren Namen Zeichen vorkommen, die nicht zum Ascii-Zeichensatz gehören, muss das Archiv so erstellt werden, dass die Dateinamen utf-8-codiert werden. 
Dies ermöglicht ein Entpacken des Archivs unabhängig davon, für welche Sprache das Zielsystem ausgelegt ist.
Unglücklicherweise unterstützen viele Archivierungsprogramme (einschließlch Windows-Explorer) diese Methode nicht.
Generell mss die utf8-Codierung von Datinamen asdrücklich aktiviert werden, auch wenn das Archivierungsprogramm dies von hause aus unterstützt.
In [http://www.7-zip.org/](7-Zip) können Sie die utf-8-Codierung von Dateinamen beispielsweise durch Angabe des Parameters "cu=on" beim Erstellen des Archivs einschalten.

++ Manifest-Dateien ++
Jedes Paket muss eine Manifest-Datei namens "manifest.ini" enthalten.
Diese Datei enthält Zeilen der Form "Name = Wert", die grundlegende Informationen über ein Paket bereitstellen wie z. B. den Namen, den Autor oder eine kurze Beschreibung.
Die Datei muss im UTF-8 kodiert sein.

+++ Verfügbare Felder +++
Auch wenn empfohlen wird, alle Felder auszufüllen, müssen lediglich diejenigen Felder Daten enthalten, die in der nachfolgenden Übersicht als Pflichtfelder markiert sind.
Anderenfalls wird das Paket nicht installiert.
* name: Ein kurzer eindeutiger Name für die Erweiterung, dieser wird benutzt, um die Erweiterungen intern voneinander zu unterscheiden (Pflichtfeld).
* summary: Eine kurze Beschreibung des Pakets im Telegrammstil, dies wird dem Anwender als Name angezeigt (Pflichtfeld).
* version: Die Version der Erweiterung z. B. 2.0 (Pflichtfeld).
* author: Der Autor des Pakets, vorzugsweise in der Form "Voller Name <E-Mail-Adresse>" (Pflichtfeld)
* description: Eine längere Beschreibung über den Sinn und Zweck der Erweiterung.
* url: Eine Internetadresse, unter der die Erweiterung, weitere Informationen oder Aktualisierungen zu finden sind.

#### Beispiel für eine Manifest-Datei {#toc25}
    --- start ---
    name = mentestpaket
    summary = Coole Erweiterung zum Testen
    version = 1.0
    description = Eine Beispielerweiterung die zeigt, wie Erweiterungen erstellt werden
    author = Michael Curran <mick@kulgan.net>
    url = http://www.nvda-project.org/wiki/Development
    --- end ---
### Plugins und Treiber {#toc26}

Die folgenden Plugins und Treiber können in einer Erweiterung enthalten sein:

* Anwendungsmodule: Diese müssen in einem Ordner namens "appModules" innerhalb des Archivs liegen.
* Braillezeilentreiber: Diese müssen in einem Ordner namens "brailleDisplayDrivers" innerhalb des Archivs liegen.
* globale Plug-ins: Diese müssen in einem Ordner namens "globalPlugins" innerhalb des archivs liegen.
* Treiber für Sprachausgaben: Diese müssen in einem Ordner namens "synthDrivers" innerhalb des Archivs liegen.

### Zusätzlicher Code zur Installation / deinstallation {#toc27}

Falls Sie während der Installation oder der Deinstallation des Pakets zusätzlichen Code ausführen möchten, um z. B. Lizenzinformationen zu prüfen oder Dateien an einen benutzerdefinierten Ort zu kopieren, können Sie in ihrem Paket eine Datei namens installTasks.py bereitstellen, die spezielle Funktionen enthält. Diese Funktionen werden immer dann aufgerufen, wenn die Erweiterung installiert/deinstalliert wird.
Sie sollten unbedingt das unnötige Laden von Modulen vermeiden (Insbesondere Python-C-Erweiterungen oder dlls ihrer eigenen Erweiterung), weil dies sonst die Deinstalation des Pakets verhindern könnte.
Sollte dies jedoch vorkommen, so wird das Verzeichnis der Erweiterung umbenannt und erst beim nächsten Start von NVDA gelöscht.

#### Die Funktion onInstall {#toc28}

Nachdem die Dateien der Erweiterung aus dem Paket entpackt und in NVDA integriert wurden, wird NVDA die Datei installtasks.py nach einer Funktion namens onInstall durchsuchen und diese ausführen.
Auch wenn die Erweiterung zu diesem Zeitpunkt bereits entpackt wurde, besitzt das Verzeichnis immer noch den Namenszusatz .pendinginstall. Dieser wird erst nach einem Neustart von NVDA entfernt und die Erweiterung wird zum ersten Mal geladen.
Wenn die Funktion einen Ausnahmefehler auslöst, wird die Installation abgebrochen und das Verzeichnis gelöscht.

#### Die Funktion onUninstall {#toc29}

Wenn NVDA nach der Deinstallation eines Pakets neu gestartet wird, wird die Datei InstallTasks.py nach einer Funktion onUninstall durchsucht und diese ausgeführt.
Wurde diese Funktion erfolgreich ausgeführt, wird das Verzeichnis der Erweiterung automatisch entfernt.
Da dies zu einem Zeitpunkt geschieht, noch bevor andere Komponenten von NVDA geladen wurden, kann die funktion keinerlei Eingaben vom Benutzer entgegennehmen.

### Erweiterungen lokalisieren {#toc30}

Sie können für Ihre Erweiterung sprachspezifische Informationen hinterlegen.
Diese werden im Ordner "locale" innerhalb des Archivs gespeichert.
Der Ordner sollte Unterordner für jeden Sprachraum enthalten, für den Sie Meldungen hinterlegen wollen. Hierbei muss dasselbe Namensformat benutzt werden, wie bei den Kernkomponenten von NVDA so z. B. "en" für Englisch oder "de" für deutsch.

#### Sprachspezifische Manifest-Dateien {#toc31}

Jedes Sprachenverzeichnis kann eine sprachspezifische Manifest.ini enthalten, die einige der oben beschriebenen Manifest-Felder in übersetzter Form bereitstellt.
Dies sind die Felder Summary und Description.
Alle anderen Felder werden ignoriert.

#### Sprachspezifische Meldungen {#toc32}

Jedes sprachverzeichnis kann auch GetText-kompatible Kataloge mit Übersetzungen von Meldungen enthalten.
Wie bei den NVDA-Kernkomponenten auch, sollten Sie die Meldungsdatei in kompilierter Form unter dem Namen "nvda.mo" im Unterverzeichnis LC_MESSAGES des Sprachenverzeichnisses ablegen.
Um Ihren Plugins zu erlauben, mittels der Funktion _() auf GetText-Katalogdateien zuzugreifen, müssen Sie die Übersetzung am Beginn eines jeden Python-Moduls initialisieren. Rufen Sie hierzu die Funktion addonHandler.initTranslations() auf.
Weitere Informationen über gettext und allgemeine Informationen über die Übersetzung von NVDA finden Sie in folgendem Artikel:
http://www.nvda-project.org/wiki/TranslatingNVDA

## Die Python-Konsole von NVDA {#toc33}

Die Python-Konsole emuliert innerhalb von NVDA den interaktiven Python-Interpreter.
Sie ist zur Fehlerbehebung oder zum Erkunden von NVDA's Interna oder zum Erkunden von Zugänglichkeitsschnittstellen nützlich.

### Verwendung {#toc34}

Die Konsole kann auf zwei Arten aktiviert werden:

* Durch Drücken von NVDA+Steuerung+Z.
Wenn Sie die Konsole auf diese Art aktivieren, werden Informationen über den Zustand von NVDA in Variablen gespeichert, die über die Konsole verfügbar sind.
Lesen Sie den Abschnitt zu  [Schnappschuss-Variablen](#PythonConsoleSnapshotVariables) für weitere Informationen.
* Durch Aufrufen des Befehls Extras --> Python-Konsole aus dem NVDA-Menü.

Die Konsole ähnelt dem Standard-Python-Interpreter.
Die Eingabe wird zeilenweise abgearbeitet.
Die aktuelle Zeile wird durch Drücken von Eingabe abgearbeitet.
Mit den Pfeiltasten können Sie durch die Ausgaben von ausgeführten Befehlen navigieren.

Die ausgabe des Befehls wird beim Drücken von Eingabe vorgelesen.
Mit F6 können Sie zwischen Ein- und Ausgabefenster wechseln.

durch Schließen des Fensters wird die Sitzung lediglich verborgen. Dies macht es möglich, zur Konsole zurückzukehren und alle bisherigen Eingaben und Variablen beizubehalten

### Namensraum {#PythonConsoleNamespace}
#### Automatische Importe {#toc36}

Der Einfachheit halber werden die folgenden Module und Variablen automatisch importiert:
sys, os, wx, log (aus logHandler), api, queueHandler, speech, braille

#### Schnappschuss-Variablen {#PythonConsoleSnapshotVariables}

Wann immer NVDA+Steuerung+Z gedrückt wird, werden einige Variablen gesetzt, die eine Momentaufnahme von NVDA darstellen.
Diese Variablen sind:

* focus: Das Objekt, welches momentan den Fokus besitzt.
* focusAnc: Die Vorfahren des aktuell fokussierten Objekts.
* fdl: Ebenen der Fokusunterschiede.
* fg: Das aktuelle Vordergrundfenster.
* nav: Das aktuelle Navigatorobjekt.
* mouse: Das Objekt, auf dem sich der Mauszeiger befindet.
* brlRegions: Die Braille-Regionen des aktiven Braille-Puffers.

## Die Remote-Python-Konsole {#toc38}

Für Situationen, in denen Fehler in NVDA über ein Netzwerk hinweg aus der Ferne korrigiert werden müssen, ist eine Remote-Python-Konsole verfügbar. 
Diese funktioniert ähnlich wie die weiter oben beschrieben [lokale Python-Konsole](#PythonConsole), der Zugriff erfolgt jedoch über TCP.

Bitte bedenken Sie, dass dies ein hohes Sicherheitsrisiko darstellt!
Sie sollten die Remote-Python-Konsole nur dann aktivieren, wenn Sie mit vertrauenswürdigen Netzwerken wie etwa VPNs verbunden sind.

### Verwendung {#toc39}

Um die Remote-Python-Konsole zu aktivieren, verwenden Sie die lokale Python-Konsole und importieren Sie remotePythonConsole. Rufen Sie anschließend remotePythonConsole.initialize() auf.
Jetzt können Verbindungen über den typ-Port 6832 aufgebaut werden.
Die Eingabeaufzeichnungsliste für zuvor eingegebene Befehle wird nicht unterstützt.
Der Namensbereich ist identisch mit dem  [Namensbereich der lokalen Python-Konsole](#PythonConsoleNamespace).

Es gibt jedoch einige weitere spezielle Funktionen:

* snap(): Erstellt einen Schnappschuss des aktuellen Zustands von NVDA und speichert diesen in den [Schnappschuss-Variablen](#PythonConsoleSnapshotVariables).
* rmSnap(): Entfernt alle Schnappschuss-Variablen.

Ende des Dokuments.

