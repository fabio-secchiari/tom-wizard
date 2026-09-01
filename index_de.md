::: titlepage
**TOM+ User Manual**

Version 2.0

![image](figures/tom_plus.png){width="85%" height="70%"}

Fabio Java

2026
:::

# Vorwort {#vorwort .unnumbered}

*Dies ist das offizielle ToM+-Benutzerhandbuch, das von mir (Fabio Java) auf Englisch verfasst wurde, ohne jegliche KI-Tools zu verwenden, weder für diese Anleitung noch für den Code, der ToM+ zum Laufen bringt. Andere Sprachen als Englisch wurden automatisch mit* [DeepL](https://www.deepl.com/en/translator) *übersetzt*.\
*In einer Ära der automatisierten Inhaltserstellung hebt sich dieses Handbuch ab, und Sie können sicher sein, dass alle beschriebenen Funktionen und die Benutzeroberfläche von Menschen erstellt wurden. Genau das macht dieses Projekt einzigartig im Vergleich zu allen Alternativen: Genau zu wissen, was der Code tut, ist der Schlüssel dazu, bewusst neue Funktionen zu entwickeln, Fehler zu beheben und bei Bedarf anderen ToM+-Besitzern Support zu bieten.*\
*ToM+ wird dank seiner großen Community, die aus dem* [deutschen Twizy-Forum](https://www.twizy-forum.de/twiz-o-meter) *entstanden ist, ständig weiterentwickelt. Wenn Sie ein ToM+-Gerät haben möchten, schreiben Sie mir eine E-Mail an* **info.twizometer@gmail.com**. *Wenn Sie eine neue Funktion vorschlagen, einen Fehler oder sogar einen Tippfehler in diesem Handbuch melden möchten, schreiben Sie mir bitte oder erstellen Sie einen Pull Request auf* [Codeberg](https://codeberg.org/fabio-java/ToM-Wizard).\
*Wenn Sie ein Standard-ToM oder ein BigToM besitzen, können Sie dieses Benutzerhandbuch ebenfalls verwenden, da die Funktionen im Wesentlichen gleich sind. Beim Standard-ToM fehlen lediglich die Dashboard-Seite und die 3D-Ladeseiten.*\
*Dieses Benutzerhandbuch wurde auf die ESP-Firmware-Version 2.4 aktualisiert.*

# Beschreibung und Funktionsübersicht

## Die wichtigsten ToM+-Funktionen

ToM+ verfügt über zahlreiche Funktionen und kann zusammen mit der Entwicklung der Firmware ständig aktualisiert werden. In den nächsten Abschnitten gebe ich Ihnen eine kurze Einführung in die Funktionen, damit Sie einen Eindruck von der Art des Produkts bekommen, das später im Handbuch ausführlicher erklärt wird.

### Ein neues Twizy-Dashboard

Da das Dashboard unseres Twizy nur einige Werte wie Geschwindigkeit und verbleibende Kilometer anzeigt, habe ich dieses coole Display entwickelt, das wesentlich mehr Daten anzeigen kann. Es liest diese direkt vom Twizy-CAN-Bus über den OBD-Anschluss im linken Handschuhfach aus. ToM „schnüffelt" lediglich die vom Twizy gesendeten Werte mit und zeigt sie anschließend auf dem LCD-Display an, wodurch viele weitere Funktionen möglich werden. ToM verfügt über einen kleinen, aber leistungsfähigen Speicher, der einige dieser Werte während der Fahrt speichern kann, um Ihnen eine Fahrtenhistorie bereitzustellen. Durch die Möglichkeit, bestimmte Werte zu speichern, können Ihre Konfigurationen und Anpassungen auch nach einem Firmware-Update auf ToM erhalten bleiben.

<figure data-latex-placement="H">
<img src="figures/dashboard.jpg" style="width:80.0%" />
<figcaption>Dashboard des ToM+</figcaption>
</figure>

Es versucht, den gleichen Stil wie das originale Twizy-Dashboard beizubehalten, jedoch mit einem moderneren und dreidimensionalen Erscheinungsbild. Wie beim Original werden Batterie, Gang, verbleibende Kilometer, Geschwindigkeit und Uhrzeit angezeigt. Zusätzlich habe ich den genauen **Batterieprozentsatz**, das Motordrehmoment, einige Statussymbole, Fahrinformationen und viele weitere Werte hinzugefügt, die Sie nach Ihren Wünschen konfigurieren können und die wir später im Detail betrachten werden.

Die Hauptseite ist anpassbar und Sie können auswählen, was darauf angezeigt werden soll. Dasselbe gilt für die anderen Seiten, durch die Sie mit der Taste blättern können, die am Wischerhebel montiert werden kann. Das allgemeine Erscheinungsbild der anderen Seiten ist im Bild dargestellt, mit einem Wert im Vordergrund und den anderen auf der linken Seite. Unten können Sie durch Antippen des Symbols die angezeigte Seite wechseln.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Motorseite des ToM+</figcaption>
</figure>

### WiFi-Konnektivität

Die im Black Box enthaltene ESP32-Platine kann sich mit einem WiFi- Netzwerkzugangspunkt verbinden. Sobald ToM+ verbunden ist, können Sie zahlreiche Dinge tun. Beispielsweise kann das Gerät verwendet werden, um Daten von Ihrem Twizy an Ihren persönlichen **MQTT**- Broker zu übertragen, wo Sie diese Werte verwenden können, um Ihr Fahrzeug in Ihr Heimautomatisierungs-IoT-System einzubinden.

Dies ist nicht die einzige Funktion im Zusammenhang mit der Wi-Fi-Fähigkeit von ToM+. Das Gerät kann auch als Access Point mit eigener SSID und eigenem Passwort fungieren und ein privates Netzwerk ohne Internetverbindung erstellen. Auf diese Weise können Sie sich sicher verbinden, **wobei Sie akzeptieren müssen, dass das Verbindungs- profil aktiv bleibt**, auch wenn keine Internetverbindung vorhanden ist (auf Android-Telefonen erscheint normalerweise 10 Sekunden nach der ersten Verbindung eine entsprechende Benachrichtigung), und anschließend zusätzliche Konfigurationen über einige vom ToM+ selbst gehostete Webseiten vornehmen. Geben Sie einfach die statische private IPv4-Adresse von ToM (***192.188.1.188***) in Ihren bevorzugten Browser ein und los geht's!

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="height:75.0%" />
<figcaption>Startseite des Webservers</figcaption>
</figure>

Wie Sie sehen können, ist der Webserver in dieser neuen Version von ToM wesentlich vollständiger und benutzerfreundlicher. Sie können einfach durch die Seiten navigieren und Ihr Gerät nach Ihren Wünschen konfigurieren. Der Webserver ist außerdem responsiv, sodass Sie ihn auch auf Ihrem Smartphone oder Tablet verwenden können.

### ToM-Telefonanwendung

Zusammen mit den Firmware-Updates für LCD und Black Box wird auch eine minimale Android-Anwendung aktuell gehalten, mit der Sie die Echtzeitdaten Ihres Twizy auf Ihrem Smartphone überwachen können.

Das Layout versucht, die ursprüngliche grafische Oberfläche von ToM nachzuahmen, und verwendet das **MQTT**- Protokoll, um Werte von ToM+ mit der Anwendung auszutauschen und zu übertragen. Daher müssen Sie die Konfiguration sowohl in der App als auch auf der MQTT-Seite von ToM+ vornehmen und dabei die IN- und OUT-Topics vertauschen. Die App wird als **APK**-Datei verteilt, einem Paket zur Installation von Android-Anwendungen, mit dem Sie diese App auch ohne Internetverbindung installieren können. Sie ist durch [Klicken hier](https://www.mediafire.com/file/du7px1bzq0zzdxu/TwizOMeter_v3.1.2.apk/file) verfügbar.

Möglicherweise müssen Sie in den Einstellungen Ihres Telefons die Option „Apps aus unbekannten Quellen installieren" aktivieren, um eine solche Dateierweiterung *(.apk)* zu öffnen. Beim ersten Start kann ein Pop-up erscheinen, das darauf hinweist, dass diese Anwendung für eine ältere Android-Version erstellt wurde, wenn Sie ein neueres Telefon besitzen: Tippen Sie einfach auf OK und ignorieren Sie die Meldung (die App funktioniert trotzdem einwandfrei). Hier sehen Sie eine Vorschau der Lade- und Einstellungsseite der App:

<figure data-latex-placement="H">
<img src="figures/tom_app_charging.png" style="width:80.0%" />
<figcaption>Ladeseite der ToM+-Android-App</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/tom_app_settings.png" style="width:65.0%" />
<figcaption>Einstellungsseite der ToM+-Android-App</figcaption>
</figure>

### Kurzer Überblick über den Verbrauch

ToM verwendet die Stromversorgung der 12-V-Batterie und bezieht diese direkt über den OBD-Anschluss. Der Verbrauch ist gering, wie die unten aufgeführten Messungen zeigen.

<figure data-latex-placement="H">
<img src="figures/consumption_off.png" style="width:65.0%" />
<figcaption>Verbrauch bei ausgeschaltetem Twizy</figcaption>
</figure>

Wenn das Mainboard aktiv und das Display eingeschaltet ist, beträgt der Verbrauch etwa 90 mA. Wenn zusätzlich WiFi eingeschaltet ist, liegt der Stromverbrauch ungefähr bei dem unten gezeigten Wert (möglicherweise etwas höher aufgrund der letzten Updates, die die 3D-Grafik eingeführt haben).

<figure data-latex-placement="H">
<img src="figures/consumption_on_wifi.png" style="width:65.0%" />
<figcaption>Verbrauch bei eingeschaltetem ToM+ mit WiFi</figcaption>
</figure>

Wenn der Twizy ausgeschaltet ist, wechselt die Black Box in den Schlafmodus und verbraucht 18 mA. Darüber hinaus ermöglicht die Touch-Funktion eine wesentlich einfachere Interaktion mit dem Gerät und seinem LCD-Display. Da eine resistive Touch-Technologie verwendet wird, können Sie Ihre Finger oder einen kleinen harten Kunststoffstift verwenden, um die Tasten zu drücken. Sie ist nicht so leistungsfähig wie kapazitive Touchscreen-Dashboards, aber wenn Sie sie einmal ausprobiert haben, möchten Sie nicht mehr darauf verzichten, vertrauen Sie mir!

## Mitgeliefertes ToM+-Kit

Beim Versand wird ToM+ normalerweise in einem braunen Karton verpackt, um die internen Platinen und Sensoren während des Transports vor Stößen zu schützen. In dieser neueren Version werden keine langen Kabel mehr benötigt, sondern nur noch ein kürzeres Kabel, das mit dem internen ToM+-Mainboard verbunden ist und in einem kleinen schwarzen Kunststoff- gehäuse untergebracht ist, das ich normalerweise „Black Box" nenne. Natürlich wird auch das resistive LCD-Touchdisplay mitgeliefert, auf dem Sie alle Funktionen anzeigen und konfigurieren können. Keine Schrauben oder Klebeband mehr nötig! Einfach das Display aufstecken -- es passt direkt auf das originale Dashboard.

<figure data-latex-placement="H">
<img src="figures/box.png" style="width:80.0%" />
<figcaption>Mitgeliefertes ToM+-Kit</figcaption>
</figure>

### Die Black Box

Die Black Box ist das Mainboard von ToM+ und enthält die meisten für den Betrieb des Systems benötigten Komponenten. Sie bietet:

- Einen externen Anschluss für das LCD-Display;

- Einen Erweiterungsanschluss mit Stromversorgungs- und GPIO-Pins;

- Einen integrierten OBD-Buchsenanschluss für den Twizy-CAN-Bus;

- Einen microUSB-Anschluss für Firmware-Updates;

- Einen Buchsenanschluss für die Taste am Wischerhebel.

- Einen EIN/AUS-Schalter für die ToM+-Stromversorgung

<figure data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:75.0%" />
<figcaption>Die Black Box</figcaption>
</figure>

### Der Erweiterungsanschluss

Wenn Sie Ihr ToM+ noch stärker anpassen möchten, können Sie dies ganz einfach über den hier gezeigten Anschluss tun. Er stellt eine zusätzliche 5-V-Stromversorgung bereit, die von VCC (zuvor rotes Kabel) und GND (zuvor schwarzes Kabel) kommt, sodass Sie eine externe LED, einen kleinen Summer oder was auch immer Sie bevorzugen mit Strom versorgen können. Die beiden anderen Kabel sind General Input Output Pins, PIN1 (zuvor gelb) und PIN2 (zuvor blau). Sie können entweder als Eingänge oder Ausgänge verwendet werden, je nachdem, was Sie auf der *„Expansion page"* des ToM-**Webservers** auswählen. In dieser neuesten Version des Geräts ist der Erweiterungsanschluss in die Black Box integriert (ohne farbige Kabel), die Pinbelegung bleibt jedoch gleich. Denken Sie daran, vor der Verwendung die Schutzabdeckung zu entfernen und eine Eingangsspannung von **maximal 3,3 V** zu verwenden. Für höhere Spannungen muss ein geeigneter Spannungsteiler verwendet werden.

<figure id="fig:expansion_pinout" data-latex-placement="H">
<img src="figures/expansion_bb.jpg" style="width:70.0%" />
<figcaption>Erweiterungsanschluss</figcaption>
</figure>

### Das LCD-Display und der Standfuß

Das resistive Touch-LCD-Display ist in einen 3D-gedruckten Standfuß integriert, der am originalen Dashboard befestigt wird. Auf Wunsch können Sie auch eine 3D-Halterung als eigenständige Lösung erhalten, um das Display wie beim Standard-ToM am Handschuhfach zu montieren. So erhalten Sie ein 2-in-1-Gerät, das je nach Wunsch sowohl aufgesteckt als auch eigenständig verwendet werden kann. Ein microSD-Steckplatz ist für Firmware-Updates zugänglich.

<figure data-latex-placement="H">
<img src="figures/display.png" style="width:80.0%" />
<figcaption>LCD-Display im Clip-on-Modus</figcaption>
</figure>

Das mit einer Schutzfolie versehene Display, wie in den Bildern zu sehen, kann in den 3D-Behälter eingesetzt werden, um einen verstellbaren Standfuß zu erhalten, den Sie überall aufstellen können.

<figure data-latex-placement="H">
<img src="figures/3d_stand_wdisplay.png" style="width:80.0%" />
<figcaption>LCD-Display als eigenständige Variante</figcaption>
</figure>

In der eigenständigen Version können Sie es mit der Abdeckung und den Schrauben befestigen, die Sie zusammen mit dem 3D-klappbaren Standfuß im Paket finden, wie in den folgenden Bildern gezeigt.

<figure id="fig:back_cover" data-latex-placement="H">
<img src="figures/back_cover.png" style="width:80.0%" />
<figcaption>Mitgelieferte LCD-Abdeckung</figcaption>
</figure>

Der 3D-Standfuß verfügt außerdem über Löcher an der Unterseite, wenn Sie ihn am Handschuhfach festschrauben möchten. Die anderen Löcher am Rahmen dienen dazu, die hintere Abdeckung festzuschrauben und das Display im Inneren an seinem Platz zu halten.

<figure id="fig:bottom_cover_screwholes" data-latex-placement="H">
<img src="figures/bottom_cover_screwholes.png" style="width:80.0%" />
<figcaption>Schraubbefestigung der LCD-Abdeckung</figcaption>
</figure>

### Zusätzliche nützliche Komponenten

Das Paket enthält einen Kabelbinder, um den 3D-gedruckten Standfuß für die Taste am rechten Wischerhebel zu befestigen (der ebenfalls mitgeliefert wird). Zusätzlich gibt es einen Bonus-Aufkleber, wenn Sie das Projekt unterstützen möchten, indem Sie ihn irgendwo auf Ihrem Twizy anbringen.

<figure data-latex-placement="H">
<img src="figures/cable_tie.jpg" style="width:80.0%" />
<figcaption>Kabelbinder</figcaption>
</figure>

<figure id="fig:wiper_stalk_button" data-latex-placement="H">
<img src="figures/wiper_stalk_button.jpg" style="width:80.0%" />
<figcaption>3D-gedruckte Taste für den Wischerhebel</figcaption>
</figure>

<figure data-latex-placement="H">
<img src="figures/sticker.png" style="width:80.0%" />
<figcaption>ToM-Aufkleber</figcaption>
</figure>

# Twiz O' Meter in Ihrem Fahrzeug installieren

Die Installation von ToM+ in Ihrem Twizy ist tatsächlich sehr einfach und erfordert keine besonderen Kenntnisse, denn wie ich normalerweise sage, handelt es sich um ein „Plug-and-Drive"-Gerät! Befolgen Sie einfach diese wenigen Schritte, um das Gerät schnell und korrekt zu installieren, oder wählen Sie selbst einen anderen Montageort.

## Position des LCD-Displays

Bei der Bestellung des Geräts können Sie den 3D-Standfuß zusätzlich zum Clip-on-Display auswählen. Sie können das Display also auf zwei verschiedene Arten installieren: im Clip-on-Modus oder mit dem 3D-Standfuß. Der Clip-on-Modus ist am häufigsten und ermöglicht es Ihnen, das Display am Dashboard des Fahrzeugs zu befestigen, während Sie das Display mit dem 3D-Standfuß auf einer ebenen Fläche im Fahrzeug platzieren können (ich empfehle normalerweise das rechte oder linke Handschuhfach).

### Clip-on-Modus

Wenn Sie diesen Modus wählen, ist die Installation wirklich einfach. Sie müssen das Display lediglich am Dashboard befestigen, an einer Position, die für Sie während der Fahrt gut sichtbar und bequem ist. Setzen Sie den oberen Teil des Displays auf das Dashboard und drücken Sie anschließend den unteren Teil nach unten, bis er einrastet.

<figure data-latex-placement="H">
<img src="figures/clip_on.jpg" style="width:80.0%" />
<figcaption>Installation im Clip-on-Modus</figcaption>
</figure>

Achten Sie darauf, dass das Kabel nicht im unteren Teil des Displays eingeklemmt wird, sondern sich frei durch die dafür vorgesehene Öffnung bewegen kann. Andernfalls könnte das Kabel beschädigt werden.

### 3D-Standfuß-Modus

Falls mitgeliefert, können Sie den 3D-Standfuß verwenden, um das Display auf einer ebenen Fläche im Fahrzeug zu platzieren. Sie können doppelseitiges Klebeband an der Unterseite anbringen, um ihn auf der Oberfläche zu befestigen. Alternativ können Sie die Schraublöcher an der Unterseite des Standfußes verwenden, um ihn mit zwei Schrauben zu befestigen.

Wie beim Clip-on-Modus sollten Sie darauf achten, dass das Kabel beim Anbringen der Abdeckung nicht im hinteren Teil des Displays eingeklemmt wird, sondern sich frei durch die dafür vorgesehene Öffnung bewegen kann. Andernfalls könnte das Kabel beschädigt werden. Siehe Abbildung [1.2](#fig:back_cover){reference-type="ref" reference="fig:back_cover"} und Abbildung [1.3](#fig:bottom_cover_screwholes){reference-type="ref" reference="fig:bottom_cover_screwholes"} auf Seite , um die genannten Teile zu sehen. So sieht der 3D-Standfuß ohne installiertes Display aus.

<figure data-latex-placement="H">
<img src="figures/3d_stand.jpg" style="width:80.0%" />
<figcaption>Leerer 3D-gedruckter Standfuß</figcaption>
</figure>

### Kabelanschluss

Anschließend können Sie die Schutzfolie vom Display entfernen und das Kabel anschließen, um es mit Strom zu versorgen. Das andere Ende des Kabels muss mit der Black Box verbunden werden, die im nächsten Schritt installiert wird. Der Stecker passt nur in einer Richtung. Achten Sie daher darauf, den Anschluss korrekt auszurichten, bevor Sie ihn einstecken.

<figure data-latex-placement="H">
<img src="figures/bb_connection.jpg" style="width:80.0%" />
<figcaption>Anschluss der Black Box</figcaption>
</figure>

## Position der Black Box

Nachdem Sie entschieden haben, wo das Display platziert werden soll, müssen Sie die Black Box anschließen.

Die Black Box muss mit dem OBD2-Anschluss des Fahrzeugs verbunden werden, der sich im linken Handschuhfach des Twizy befindet. Wenn Sie es noch nie geöffnet haben, finden Sie dort eine kleine Kunststoffabdeckung, die Sie entfernen müssen, um Zugang zum OBD2-Anschluss zu erhalten. Sobald Sie Zugang haben, stecken Sie die Black Box einfach ein und stellen Sie sicher, dass sie sicher verbunden ist. Der Stecker passt nur in eine Richtung. Achten Sie daher darauf, den Anschluss korrekt auszurichten, bevor Sie ihn einstecken.

<figure data-latex-placement="H">
<img src="figures/obd_connector.png" style="width:80.0%" />
<figcaption>Position des OBD2-Anschlusses im Twizy</figcaption>
</figure>

**Erst nachdem das Display angeschlossen wurde**, können Sie den Schalter an der Black Box einschalten. Damit ist die Installation abgeschlossen! Jetzt können Sie Ihren Twizy starten und die ToM+-Funktionen genießen.

# Erklärung der grundlegenden Benutzeroberfläche

## Bedeutung der Symbole {#sec:icon_list}

Die Benutzeroberfläche (UI) von ToM ist sehr intuitiv und einfach zu bedienen, und jede Angabe wird durch ein spezifisches Symbol dargestellt, das normalerweise darauf hinweist, wofür diese Daten nützlich sein können. Hier ist eine Liste aller Symbole, die Sie auf dem ToM finden könnten, und deren Bedeutung.

### Seitensymbole {#sec:page_icon_list}

Seitensymbole sind die Symbole, die Sie in der unteren Zeile des ToM+ Displays finden, und sie werden verwendet, um zwischen den verschiedenen Seiten zu wechseln. Seit dem letzten Update wurden sie mit einem metallischen 3D-Look überarbeitet.

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV2.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Motor.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryInfo2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Error.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/TripLog.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Gyroscope.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Street0Ok_v2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/3Dots.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Batteriegruppe {#sec:item_numbers}

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatterySoc.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatterySoh.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryKwh.jpg){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryA.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryA+red.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryKw.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Battery3°.jpg){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV2.jpg){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryV.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------------- -------------------------------------------------------------
  ![image](icons/BatteryDiff.png){height="8mm"}   

  ----------------------------------------------- -------------------------------------------------------------
:::

### Ladegruppe

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/CEta.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/Charge°.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/ChargedKwh.png){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/ChargeKwh.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

### Motorgruppe

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/MotoRPM2.jpg){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/MotorNm.jpg){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/Motor°2.jpg){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Sev°.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

### Erweiterungsport-Gruppe

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin1.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin2.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

### Gyroskopgruppe

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/InclDX.PNG){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/InclSX.PNG){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------------- -------------------------------------------------------------
  ![image](icons/UphillTwizy.png){height="8mm"}   

  ----------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------- -------------------------------------------------------------
  ![image](icons/DownhillTwizy.png){height="8mm"}   

  ------------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/GyroAcc.JPG){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Gtemp.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Timer.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Fahrtgruppe

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/tKm.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tKmh.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tKmR.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh100.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  -------------------------------------------- -------------------------------------------------------------
  ![image](icons/tkWh1min.png){height="8mm"}   

  -------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------ -------------------------------------------------------------
  ![image](icons/tTimer.png){height="8mm"}   

  ------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/tUphill.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/tDownhill.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

### Armaturenbrettgruppe

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/ODO.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/Kmh.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/KmhR.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------- -------------------------------------------------------------
  ![image](icons/KmRCalc.png){height="8mm"}   

  ------------------------------------------- -------------------------------------------------------------
:::

[]{#fig:calculated_kilometers_left label="fig:calculated_kilometers_left"}

## Armaturenbrett-Seite

Dieser Abschnitt befasst sich mit der Erklärung der Armaturenbrett-Seite, die die Hauptseite des ToM+ ist und wahrscheinlich diejenige, die Sie am meisten verwenden werden. Auf dem Bild unten habe ich die wichtigsten Teile nummeriert und werde sie in den folgenden Absätzen erklären.

<figure id="fig:dashboard_layout" data-latex-placement="H">
<img src="figures/dashboard_numbers.PNG" style="width:80.0%" />
<figcaption>Armaturenbrett-Seite mit nummerierten Teilen.</figcaption>
</figure>

**1**

: Aktueller Gang des Fahrzeugs, der normalerweise auch auf dem Original-Armaturenbrett angezeigt wird.

**2**

: Ein Wert, der aus Drehmoment, Stromverbrauch und Stromaufnahme ausgewählt wird und zum Füllen des in Punkt 6 beschriebenen Leistungsbalkens dient. Tippen Sie auf den Wert, um zwischen den drei Optionen zu wechseln.

**3**

: Fehlerstatus-Symbol, wird angezeigt, wenn ein Fehler vorliegt.

**4**

: Zeigt die aktive Fahrt an. Tippen Sie auf das Symbol, um die Fahrt-Seite zu öffnen.

**5**

: Symbole für MQTT und WiFi. Ausgegraut, wenn keine Verbindung besteht, und farbig bei Verbindung. Tippen Sie auf die Symbole, wenn Sie einen neuen WiFi-Scan oder eine MQTT-Neuverbindung durchführen möchten.

**6**

: Leistungsbalken, der den in Punkt 2 ausgewählten Wert anzeigt. Ausgehend von der Mittellinie füllt sich der Balken beim Beschleunigen von links nach rechts und beim regenerativen Bremsen von rechts nach links. Der Balken wird in beide Richtungen mit einem Farbverlauf gefüllt, und die **Maximal- und Minimalwerte sind anpassbar** auf der BigToM-Seite des Webservers.

**7**

: Zeigt die momentane Geschwindigkeit des Fahrzeugs an. Sie können auf der Webserver-Seite \"Erweiterte Info und Einstellungen\" zwischen km/h und mph wählen.

**8**

: Motorsymbol, tippen Sie darauf, um die Motorseite zu öffnen.

**9**

: Batterie-Symbol mit Farbverlauf, tippen Sie darauf, um die Batterie-Info-Seite zu öffnen.

**10**

: Zusätzlich angezeigte Werte, Sie können durch Antippen des Symbols zwischen ihnen wechseln.

**11**

: Zeigt Uhrzeit und Datum an, wechseln Sie durch Antippen zwischen ihnen.

**12**

: Anpassbares Geschwindigkeitswarnlimit (grün, gelb oder rot), siehe Abschnitt [4.4.14](#sec:web_btom_tom_sets){reference-type="ref" reference="sec:web_btom_tom_sets"} zur Aktivierung.

## Das Seitenlayout {#sec:main-layout}

Das Layout lässt sich in zwei Hauptteile unterteilen, die wir uns in den nächsten beiden Absätzen genauer ansehen werden. Der erste ist der Datenmonitor, der einige Funktionen bietet, um die im Vordergrund angezeigten Daten aus den in der Seitenleiste aufgelisteten auszuwählen. Der zweite ist die Status-Symbolleiste, die sich normalerweise am unteren Rand der Seite befindet. Die Batterie-, Motor-, Gyroskop- und Fahrt-Seiten teilen sich das gleiche Layout, wie auf dem Bild gezeigt.

<figure data-latex-placement="H">
<img src="figures/engine_page.jpg" style="width:80.0%" />
<figcaption>Beispiel für das gemeinsame Layout (die Motorseite).</figcaption>
</figure>

Auf der linken Seite des Bildschirms befindet sich, wie Sie auf dem Foto sehen können, eine Liste von vier Werten, die in einem minimalen Raster gruppiert sind. Jeder Wert ist mit seiner Maßeinheit und einem kleinen Symbol gekoppelt, das für jede Angabe eindeutig ist und alle in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} aufgelistet wurden. Über dem Wert befindet sich ein orangefarbener Fortschrittsbalken, der darstellt, wie groß (oder klein) der Wert im Vergleich zu seinem Maximal- (oder Minimal-) Wert ist.\
Der rechte Bereich des Bildschirms wird hauptsächlich von den Vordergrunddaten (oder einfach den ausgewählten Daten) eingenommen. Er verfügt über ein großes Twizy-Symbol, das von einem bogenförmigen Fortschrittsbalken umgeben ist, der dieselbe Funktion erfüllt wie der zuvor besprochene kleinere, mit dem einzigen Unterschied, dass er 32 statt nur 16 Stufen hat. An den Rändern des Fortschrittsbalkens befindet sich der Bereich oder der Multiplikator des in der Mitte der Seite angezeigten Wertes, welcher dem Symbol zugeordnet ist, das direkt darüber angezeigt wird.\
Unten befindet sich eine Liste von Symbolen, mit denen zwischen den verschiedenen Seiten des ToM+ gewechselt wird. Die Symbole sind für alle Seiten gleich und wurden in Abschnitt [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"} aufgelistet. In der oberen linken Ecke befindet sich ein kleines Symbol, das den aktuellen Gang des Fahrzeugs anzeigt. Wenn Sie darauf drücken, **kehren Sie zur Armaturenbrett-Seite zurück**, die wir gerade besprochen haben. In der oberen rechten Ecke befinden sich drei kleine Punkte, die bei Betätigung die Einstellungsseite öffnen. Zu guter Letzt befindet sich auf der langen weißen Linie am unteren Rand des Bildschirms die Statusleiste mit einigen Symbolen, die wir später besprechen werden.

### Ändern der Vordergrunddaten

Das Ändern der im Vordergrund angezeigten Daten ist sehr einfach und intuitiv. Sie können dies tun, indem Sie einfach auf das Symbol der Daten tippen, die Sie im Vordergrund anzeigen möchten, und die Werte werden getauscht. Auf diese Weise können Sie auch die Daten auf der linken Seite des Bildschirms neu anordnen, was sehr nützlich ist, wenn Sie bestimmte Daten in einer beliebigen Reihenfolge haben möchten.

<figure data-latex-placement="H">
<img src="figures/change_foreground.jpg" style="width:70.0%" />
<figcaption>Beispiel für das Ändern der Vordergrunddaten (auf der Motorseite).</figcaption>
</figure>

Als Beispiel hat der Benutzer im obigen Bild auf das Symbol der Motordrehzahl getippt, das derzeit auf der linken Seite des Bildschirms angezeigt wird. Die beiden Werte wurden getauscht und nun wird die Motordrehzahl im Vordergrund angezeigt, während der Batterie-SOC im linken Raster angezeigt wird.

### Ändern der aktiven Seite

Um die aktive Seite zu ändern, können Sie auf das Symbol der Seite tippen, zu der Sie wechseln möchten. Dieses befindet sich in der unteren Zeile des Bildschirms. Das Symbol wird orange und die neue Seite wird angezeigt. Im Bild ist die aktive Seite die Motorseite.

<figure data-latex-placement="H">
<img src="figures/changing_page.jpg" style="width:70.0%" />
<figcaption>Beispiel für das Ändern der aktiven Seite (auf der Motorseite).</figcaption>
</figure>

Jede dieser Aktionen kann über die Taste am rechten Scheibenwischerhebel ausgeführt werden, was beim Fahren sehr nützlich ist, da Sie Ihre Augen auf der Straße und Ihre Hände am Lenkrad behalten können. Die Taste kann verwendet werden, um durch die verschiedenen Seiten zu blättern, die Vordergrunddaten zu ändern und vieles mehr. Dies wird im Detail in Abschnitt [4.4.7.5](#sec:web_wiper_stalk){reference-type="ref" reference="sec:web_wiper_stalk"} beschrieben.

### Die Status-Symbolleiste {#sec:status_icon_bar}

Unterhalb der Tasten zum Seitenwechsel, die im vorherigen Absatz besprochen wurden, befindet sich eine lange weiße Linie, die Ihnen den Status der Netzwerkverbindung anzeigt und auch anzeigt, wann Alarme oder Fehler ausgelöst werden. Am Anfang der Linie befindet sich, wie Sie auf dem Bild sehen können, ein kleines Twizy-Symbol mit einer Nummer: Es ist eine Schaltfläche, die Sie zur Fahrt-Seite führt, die später in Abschnitt [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"} besprochen wird. Schauen wir uns nun die Status-Symbolleiste an.

<figure data-latex-placement="H">
<img src="figures/status_icon_bar.jpg" style="width:70.0%" />
<figcaption>Die Status-Symbolleiste.</figcaption>
</figure>

Beginnend auf der rechten Seite des Bildes sehen Sie ein magnetisches blaues Wellensymbol, das für den **Wi-Fi**-Verbindungsstatus steht. Wenn es farbig und fest leuchtet, wie oben gezeigt, bedeutet dies, dass ToM mit einem Wi-Fi verbunden ist, bei dem es sich sowohl um ein öffentliches Netzwerk als auch um eines aus Ihrer festgelegten Liste handeln kann. Wenn das Symbol ausgegraut ist, ist ToM mit keinen Netzwerken verbunden und sucht nach einer Abklingzeit von fünf Minuten erneut nach Wi-Fi-Netzwerken. Sie können jedoch durch Antippen des Symbols so schnell wie möglich einen neuen Scan erzwingen. Nicht zuletzt, wenn das Symbol blinkt, hat ToM einen Wi-Fi-Scan durchgeführt, ein oder mehrere Netzwerke gefunden und versucht, sich mit einem von ihnen zu verbinden.\
Das nächste Symbol ist eine violette Wolke mit dem Text **„MQTT"** darin und steht, wie Sie erraten können, für den **MQTT**-Verbindungsstatus. Die Position dieses Symbols ist festgelegt und kann nicht geändert werden, genau wie beim Wi-Fi-Symbol. Eine weitere Ähnlichkeit mit dem vorherigen Symbol besteht darin, dass es entweder fest leuchten oder mit demselben Farbcode wie zuvor ausgegraut sein kann.\
Dann haben wir das Fehlersymbol, das ein rotes Rechteck mit dem Text **„ERR"** darin ist. Es wird angezeigt, wenn ein Fehler vorliegt, oder ausgeblendet, wenn keine Fehler vorhanden sind.\
Schließlich haben wir Alarmsymbole, die durch farbige Sterne dargestellt werden. Verfügbare Sterne sind die auf dem Bild gezeigten. Sie können auf der Webserver-Seite \"Alarmauslöser\" auswählen, welchen Sie für jeden Alarm verwenden möchten. Dort können Sie auch wählen, ob Sie diese blinken lassen möchten oder nicht.

<figure id="fig:alarm_icons" data-latex-placement="H">
<img src="figures/alarm_icons.png" style="width:70.0%" />
<figcaption>Die Alarmsymbole.</figcaption>
</figure>

### Pop-ups

Auf diesen Seiten werden je nach den auf der Webserver-Seite „Alarmauslöser" festgelegten Konfigurationen Pop-ups angezeigt. Es gibt zwei Haupttypen von Pop-ups: der erste verschwindet erst, wenn Sie ihn bemerken und darauf drücken (dieser Typ blockiert das gesamte System und pausiert sowohl die Werte im linken Raster als auch den Vordergrundwert). Andererseits können Sie, wenn Sie beim Fahren nicht gestört werden möchten, den zweiten Pop-up-Typ verwenden, der speziell dafür entwickelt wurde, nach 10 Sekunden automatisch zu verschwinden.\
Hier sehen Sie ein Beispiel für die einfachste Art von Pop-up, bei dem das eingekreiste Warnsymbol kontinuierlich blinkt. Wie Sie sehen können, besteht es aus einem gelben Kasten mit einer gepunkteten Umrandung, der das Symbol des Werts und den Wert selbst enthält, der den zuvor auf der Webserver-Seite eingestellten Alarm ausgelöst hat (Motortemperatur = 35° C).

<figure data-latex-placement="H">
<img src="figures/pop-up.PNG" style="width:70.0%" />
<figcaption>Ein Beispiel für ein Pop-up.</figcaption>
</figure>

## Die Batterie-Info-Seite

Die Batterie-Info-Seite bietet Ihnen detailliertere Informationen zu jeder einzelnen Zelle der Batterie. Wie Sie vielleicht wissen, haben Standard-Twizy-Batterien 14 Zellen und einen gemeinsamen Temperatursensor für jedes Paar. Auf dieser Seite können Sie die Spannung und Temperatur jeder Zelle überwachen und haben auch einen Überblick über die Gesamtspannung der Batterie. Auf dem Bild ist zu sehen, wie dies normalerweise aussieht.

<figure data-latex-placement="H">
<img src="figures/binfo_page.jpg" style="width:80.0%" />
<figcaption>Die Batterie-Info-Seite.</figcaption>
</figure>

### Überprüfen von Spannung und Temperatur

Wie auf dem Bild oben auf der linken Seite der Seite gezeigt, befindet sich eine batterieförmige weiße Linie, die eine kleine Tabelle mit den Spannungen der ersten sieben Zellen enthält. Um die restlichen Zellenspannungen zu sehen, drücken Sie das orange und weiße Pfeilsymbol (das auf dem nächsten Foto eingekreist ist) und das Raster zeigt die nächsten Werte an.

Wenn Sie dieselbe Pfeiltaste erneut drücken, ändern sich die angezeigten Daten erneut und es werden die Zelltemperaturen in Celsius ausgedrückt. Der Vordergrundwert würde sich ebenfalls ändern und wie Sie an dem Symbol darüber erkennen können, wird die Gesamttemperatur der Batterie angezeigt, die in diesem Beispiel für jede Zelle gleich ist. Beziehen Sie sich auf das Bild unten, um die Änderung zu sehen.

<figure data-latex-placement="ht">
<figure>
<img src="figures/binfo_page2.jpg" />
<figcaption>Verbleibende Zellspannungen.</figcaption>
</figure>
<figure>
<img src="figures/binfo_page3.jpg" />
<figcaption>Zelltemperaturen.</figcaption>
</figure>
<figcaption>Zelltemperaturen.</figcaption>
</figure>

### Die komprimierte Batterie-Info-Seite {#sec:condensed_binfo}

Ein erneutes Drücken derselben Taste führt Sie zu einer speziellen Seite, die alle Daten, die wir im vorherigen Absatz besprochen haben, auf einmal enthält.

<figure data-latex-placement="H">
<img src="figures/binfo_page_condensed.png" style="width:80.0%" />
<figcaption>Die komprimierte Batterie-Info-Seite.</figcaption>
</figure>

Auf dem Foto oben sehen Sie, dass der Bildschirm in zwei Teile geteilt ist. Der erste ist die gleiche batterieförmige weiße Linie, aber etwas größer, um alle Spannungs- und Temperaturwerte aufzunehmen. Die Temperatur befindet sich zwischen den beiden Zellen, die diesen Temperatursensor gemeinsam nutzen. Auf der rechten Seite der Seite sehen Sie den Wert, der zuvor im Vordergrund angezeigt wurde, d. h. die Gesamtspannung der Batterie und die Gesamttemperatur der Batterie. Der SOC-Wert steht ebenfalls an erster Position, da er immer nützlich ist.\
Auf dieser Seite gab es nicht genug Platz für die Schaltflächen zum Seitenwechsel, da es wichtiger ist, die zuvor besprochenen Status-Symbole zu haben. Wenn Sie die Seite wechseln müssen, können Sie die Beenden-Schaltfläche in der unteren rechten Ecke drücken und gelangen dann auf eine Seite, die über die Steuerelemente zum Ändern der aktiven Seite verfügt.\
Ein wichtiger Hinweis des letzten Updates ist der Unterschied zwischen der Zelle mit der minimalen und der maximalen Spannung, die durch einen blauen bzw. roten Punkt dargestellt werden. Dieser Wert ist sehr wichtig, da er Ihnen sagen kann, ob die Batterie gesund ist oder nicht. Wenn der Unterschied zu hoch ist, bedeutet dies, dass die Batterie unausgeglichen ist und dies ein Zeichen für ein Problem sein könnte. ToM+ zeigt Ihnen diesen Wert auf der komprimierten Batterie-Info-Seite an, und Sie können auch im Webserver einen Alarmauslöser einstellen, um benachrichtigt zu werden, wenn der Unterschied zu hoch ist.\
Sie können in den Einstellungen festlegen, ob diese komprimierte Batterieseite als Standardseite angezeigt wird, wenn Sie auf die Schaltfläche Batterie-Info drücken, oder nicht. Der Vorgang wird in Abschnitt [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} gezeigt. Wenn Sie die Option wählen, alle vier in diesem Absatz behandelten Seiten anzuzeigen, können Sie auch die Pfeiltaste drücken, während Sie sich auf der komprimierten Seite befinden, um zurück zu den anderen Batterie-Info-Seiten zu blättern.

## Die Alarmprotokoll-Seite {#sec:alarm_log}

Auf dieser Seite können Sie alle Alarmauslöser sehen, falls Sie einen verpasst haben oder wenn Sie diese stummgeschaltet haben, um während der Fahrt nicht gestört zu werden. Schauen wir uns an, wie es aussieht.

<figure data-latex-placement="H">
<img src="figures/alarm_page.jpg" style="width:80.0%" />
<figcaption>Die 3D-Alarmprotokoll-Seite.</figcaption>
</figure>

Das Bild zeigt eine kleine Tabelle, die das Element, das den Alarm ausgelöst hat, gepaart mit seinem Symbol und seinem Wert enthält. Dann habe ich auch noch Datum und Uhrzeit hinzugefügt (verfügbar, wenn beim ersten Mal eine Verbindung zu einem Netzwerk hergestellt wurde), um zu wissen, wann dieser Datensatz der Liste hinzugefügt wurde.\
In den nächsten Bildern (mit dem alten Design) beziehen sich die meisten Datensätze auf den Batterie-SOC, insbesondere, wenn er unter 30 % fällt. In Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"} erfahren Sie, wie Sie Ihren eigenen Alarm auf dem Webserver einrichten.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old1.png" style="width:70.0%" />
<figcaption>Die 3D-Alarmprotokoll-Seite.</figcaption>
</figure>

### Überprüfen älterer Alarmauslöser

Wenn Sie ältere Alarmauslöser sehen müssen, die nicht in der Liste der ersten sieben aufgeführt sind, können Sie das gelbe Warnsymbol oben in der Tabelle drücken. Dadurch ändern sich die angezeigten Werte in die älteren. Sie können diese Aktion zweimal durchführen, da ToM bis zu 21 Alarmauslöser speichern kann und ältere vergisst.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old2.png" style="width:100.0%" />
<figcaption>Ändern der angezeigten Auslöser.</figcaption>
</figure>

Wie Sie auf diesen beiden Fotos der Alarmprotokoll-Seite sehen können, änderten sich die angezeigten Daten beim Drücken der eingekreisten gelben Warnschaltfläche auf einige der älteren, was Sie beim Vergleich der Daten feststellen können. Der Elementzähler links hat sich ebenfalls geändert (8--14).

### Löschen eines Alarmauslösers {#sec:delete_log_record}

Wenn Sie einen oder mehrere Datensätze nicht mehr benötigen, können Sie auswählen, ob einige davon gelöscht werden sollen. Wählen Sie einen oder mehrere Datensätze zum dauerhaften Entfernen aus, indem Sie auf das Datum oder die Uhrzeit drücken (ein kleines rotes Häkchen erscheint neben den ausgewählten Datensätzen). Drücken Sie dann auf das gelb eingekreiste Mülleimer-Symbol im zweiten Foto, um die ausgewählten Datensätze zu löschen. Diese Datensätze verschwinden und werden durch die nächsten Datensätze ersetzt, was zu einer Verschiebung der gesamten Liste führt, wie Sie auf dem zweiten Bild erkennen können.

<figure data-latex-placement="H">
<img src="figures/alarm_log_old3.jpg" style="width:100.0%" />
<figcaption>Löschen ausgewählter Alarmauslöser.</figcaption>
</figure>

Auf dieser Seite gibt es keine Status-Symbolleiste oder Schaltflächen zum Wechseln der Seite, da es sich eher um eine Einstellungsseite handelt und keine solchen Steuerelemente benötigt. Drücken Sie zum Beenden die Pfeiltaste in der unteren rechten Ecke und ToM bringt Sie zu der Seite zurück, auf der Sie sich vor dem Aufrufen der Alarmprotokoll-Seite befanden, und von dort aus können Sie die aktive Seite wieder ändern.

## Die Fahrt-Seite {#sec:trip_page}

Diese Seite kann die Daten über eine Fahrt speichern *(Fahrt bezeichnet die Zeitspanne vom Fahrbeginn bis zum Ausschalten Ihres Twizy)* und dann entscheiden, ob diese Werte beim erneuten Fahrbeginn gespeichert oder verworfen werden. Sie können gleichzeitig die Daten von bis zu fünf Fahrten speichern. Das Layout ist dasselbe wie auf der Hauptseite, sodass die Bedienelemente zum Ändern der Reihenfolge der Werte oder der Daten im Vordergrund bereits in Abschnitt [3.3](#sec:main-layout){reference-type="ref" reference="sec:main-layout"} besprochen wurden. Die nächsten Absätze befassen sich mit dem Zurücksetzen einer Fahrt und dem Ändern der aktuellen Fahrt.

<figure data-latex-placement="H">
<img src="figures/trip_page_full.jpg" style="width:80.0%" />
<figcaption>Die Fahrt-Seite.</figcaption>
</figure>

### Ändern der aktuellen Fahrt

Wenn Sie mit der Aufzeichnung der Daten auf einer bestimmten Fahrt zwischen 1 und 5 beginnen möchten, können Sie das im vorherigen Bild gelb eingekreiste Fahrtsymbol drücken. Wenn Sie es zum ersten Mal drücken, gelangen Sie zur Fahrt Nr. 1 und wiederholtes Drücken durchläuft alle verfügbaren Fahrten, sodass Sie diejenige auswählen können, die Sie starten oder fortsetzen möchten.\
Um zu sehen, in welcher Fahrt ToM derzeit aufzeichnet, beziehen Sie sich auf die orangefarbene Zahl im Fahrtsymbol. Sobald Sie die gewünschte Fahrt ausgewählt haben, können Sie bei Bedarf auch die aktive Seite wechseln, ohne die ausgewählte Fahrt zu verlieren, da ToM weiterhin Werte aufzeichnet, auch wenn die Fahrt-Seite nicht im Fokus steht.

### Fahrtaufzeichnung deaktivieren

In diesem Beispiel befinde ich mich derzeit auf der Motorseite und zeichne Daten auf der fünften Fahrt-Seite auf, wie durch die kleine orangefarbene Zahl neben dem Fahrtsymbol angegeben. Wenn Sie die Fahrtaufzeichnung pausieren möchten, können Sie dies auf dem ToM+ tun, indem Sie **die Fahrttaste drei Sekunden lang gedrückt halten**, während eine andere Seite aktiv ist (in diesem Beispiel die Batterieseite).\

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_page_on.jpg" />
<figcaption>Fahrtaufzeichnung aktiv auf Fahrt 5.</figcaption>
</figure>
<figure>
<img src="figures/trip_page_off.jpg" />
<figcaption>Fahrtaufzeichnung pausiert.</figcaption>
</figure>
<figcaption>Fahrtaufzeichnung pausiert.</figcaption>
</figure>

Sobald Sie losgelassen haben, ändert ToM+ das kleine Fahrtsymbol und zeigt das Kartensymbol anstelle der Fahrtnummer an, um Sie darüber zu informieren, dass keine Daten mehr aufgezeichnet werden (zweites Bild). Wenn Sie bereit sind, die Fahrt wieder aufzuzeichnen, drücken Sie auf die Fahrt-Seite, bis Sie die gewünschte Fahrt finden, indem Sie alle verfügbaren durchlaufen.

### Eine Fahrt zurücksetzen

Wenn Sie eine bestimmte Fahrt löschen möchten, können Sie sie auswählen und **die Fahrttaste drei Sekunden lang gedrückt halten**. Sobald Sie losgelassen haben, sollten Sie feststellen, dass alle Fahrtwerte auf der Seite zurückgesetzt wurden (normalerweise auf Null). Der Unterschied zwischen dieser Aktion und der vorherigen besteht darin, dass in diesem Fall die Fahrtdaten gelöscht werden, während im vorherigen Fall die Fahrtdaten nur angehalten werden. Außerdem müssen Sie sich hier auf der Fahrt-Seite befinden, während Sie sich im vorherigen Fall auf einer beliebigen anderen Seite befinden sollten.

## Die Fahrtenhistorie-Seite {#sec:trip_history}

Diese Seite speichert die Daten der letzten zwanzig Fahrten und das Layout entspricht dem der Alarmprotokoll-Seite. Die Werte werden nur aktualisiert und gespeichert, wenn die ausgewählte Fahrt die **Nummer 5** ist.

### So greifen Sie auf die Fahrtenhistorie-Seite zu

Diese Seite ist von der Hauptseite aus nicht zugänglich, aber Sie können sie erreichen, indem Sie **das Alarmprotokoll-Symbol in der unteren Zeile des Bildschirms lange drücken**, bis es sich ändert. Dies liegt daran, dass die Fahrtenhistorie-Seite keine Seite ist, die Sie oft verwenden werden. Daher wurde beschlossen, sie aus Platzgründen vor der Hauptseite zu verbergen, ebenso wie die Fehlerseite. Die Abfolge der Seiten, die durch **langes Drücken des Alarmprotokoll-Symbols** verfügbar sind, lautet also: Alarmprotokoll-Seite (Abschnitt [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ Fehlerseite (Abschnitt [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"}) $\rightarrow$ Fahrtenhistorie-Seite $\rightarrow$ zurück zur Alarmprotokoll-Seite, jeweils mit dem entsprechenden Symbol.\

<figure data-latex-placement="H">
<img src="figures/enter_trip_log_page.jpg" style="width:80.0%" />
<figcaption>Das Symbol für den Zugriff auf die Fahrtenhistorie-Seite.</figcaption>
</figure>

### Hauptsteuerelemente der Fahrtenhistorie-Seite

<figure data-latex-placement="H">
<img src="figures/trip_history_page.jpg" style="width:80.0%" />
<figcaption>Die Fahrtenhistorie-Seite.</figcaption>
</figure>

Auf diesem Bild sehen Sie die ersten sieben Fahrten, die in der Liste gespeichert sind, mit Datum und Uhrzeit sowie der zurückgelegten Strecke. Sie können die in jeder Zeile angezeigten Daten leicht ändern, indem Sie auf das Symbol der Daten drücken, wie unten gezeigt. Die Daten wechseln zwischen den meisten verfügbaren Fahrtdaten, sodass Sie auswählen können, welche angezeigt werden sollen. In den nächsten Bildern sehen Sie dieselbe Seite mit dem Stromverbrauch der Fahrt und der Durchschnittsgeschwindigkeit.

<figure data-latex-placement="ht">
<figure>
<img src="figures/trip_log_kwh.jpg" />
<figcaption>Fahrtstromverbrauch anzeigen.</figcaption>
</figure>
<figure>
<img src="figures/trip_log_kmh.jpg" />
<figcaption>Durchschnittsgeschwindigkeit der Fahrt anzeigen.</figcaption>
</figure>
<figcaption>Durchschnittsgeschwindigkeit der Fahrt anzeigen.</figcaption>
</figure>

Auf dem Webserver können Sie sie alle auf einmal sehen, dies wird in Abschnitt [4.4.5](#sec:web_trip_history){reference-type="ref" reference="sec:web_trip_history"} besprochen.

## Die Fehlerseite {#sec:error_page}

Diese Seite ähnelt der Alarmprotokoll-Seite und der Fahrtenhistorie-Seite, zeigt Ihnen jedoch die letzten aufgetretenen DTC-Fehler an. Die Steuerelemente zum Löschen von Datensätzen oder zum Anzeigen älterer wurden bereits in Abschnitt [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"} besprochen.

### So greifen Sie auf die Fehlerseite zu

Diese Seite ist nicht von der Hauptseite aus zugänglich, kann jedoch durch **langes Drücken des Alarmprotokoll-Symbols** in der unteren Zeile des Bildschirms erreicht werden, bis es sich ändert. Wie wir bereits besprochen haben, lautet die Abfolge der Seiten, die durch langes Drücken des Alarmprotokoll-Symbols verfügbar sind: Alarmprotokoll-Seite (Abschnitt [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"}) $\rightarrow$ Fehlerseite $\rightarrow$ Fahrtenhistorie-Seite (Abschnitt [3.7](#sec:trip_history){reference-type="ref" reference="sec:trip_history"}) $\rightarrow$ zurück zur Alarmprotokoll-Seite, jeweils mit dem entsprechenden Symbol.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/enter_error_page.jpg" />
<figcaption>Das Symbol für den Zugriff auf die Fehlerseite.</figcaption>
</figure>
<figure>
<img src="figures/error_page.jpg" />
<figcaption>Anzeigen der Fehlerseite.</figcaption>
</figure>
<figcaption>Anzeigen der Fehlerseite.</figcaption>
</figure>

### Hauptsteuerelemente der Fehlerseite

Wie Sie im zweiten Bild oben sehen können, ähnelt die Fehlerseite der Alarmprotokoll-Seite. Es wird eine Liste der letzten 14 aufgetretenen Fehler angezeigt, mit ihrem ODO, der DTC-Nummer, der DF-Nummer (falls verfügbar) und einem repräsentativen Symbol. Weitere Informationen wie SOC, Geschwindigkeit und eine kurze Beschreibung finden Sie auf der entsprechenden Seite des Webservers (Abschnitt [4.4.15](#sec:web_diagnostic){reference-type="ref" reference="sec:web_diagnostic"}).\
Durch Drücken auf das Symbol des Fehlers (im Bild gelb eingekreist) können Sie durch die Seiten der gespeicherten Fehler blättern, welche insgesamt 14 betragen. Die erste Seite zeigt die letzten 7 Fehler, während die zweite Seite die älteren zeigt. Um **Fehleraufzeichnungen zu löschen**, sowohl auf dieser Seite als auch im Auto, klicken Sie einfach auf das Mülleimer-Symbol.\
Wie auf anderen Seiten reichte der Platz nicht aus, um die Schaltflächen zum Seitenwechsel einzufügen. Daher können Sie die Beenden-Schaltfläche in der unteren rechten Ecke drücken, um zur vorherigen Seite zurückzukehren, und dann bei Bedarf die aktive Seite wechseln.

## Die Ladeseite {#sec:charging_page}

Diese Seite wird während der Fahrt nicht angezeigt und es gibt keine spezielle Schaltfläche, um sie aufzurufen. Das liegt hauptsächlich daran, dass dieser Ladebildschirm automatisch angezeigt wird, wenn sich der Twizy gerade im Ladezustand befindet.

Wie Sie auf dem Bild sehen können, ist das Layout dasselbe wie auf der Armaturenbrett-Seite. Der aktuelle SOC wird in der Mitte angezeigt und ersetzt den Geschwindigkeitswert.\
Es wird auch eine Animation gestartet, deren Geschwindigkeit je nach Ladeleistung variiert. Auf dem Foto unten gibt es auch einige ladespezifische Daten, die Sie in den Einstellungen ändern können, wie später erklärt wird. Auf dieser Seite haben Sie nicht die Symbol-Statusleiste, aber Sie haben immer noch die Netzwerkstatus-Symbole in der unteren rechten Ecke, da Sie die Ladewerte Ihres Autos auch überwachen können, wenn das Auto ausgeschaltet ist. Tatsächlich schaltet sich das ToM+ automatisch ein, wenn Sie Ihren Twizy an eine gültige Stromversorgung anschließen.

<figure data-latex-placement="H">
<img src="figures/charging_page.jpg" style="width:80.0%" />
<figcaption>Die Ladeseite.</figcaption>
</figure>

**1**

: Aktuell in der Batterie gespeicherte Leistung, ausgedrückt in $kWh$.

**2**

: Ein Wert, ausgewählt aus Drehmoment, Stromverbrauch und Stromaufnahme, der verwendet wird, um den blauen Teil des Leistungsbalkens zu füllen. Tippen Sie auf den Wert, um zwischen den drei Optionen zu wechseln.

**3**

: Aktuelle Ladeleistung, ausgedrückt in $kW$, wird verwendet, um die rechte Seite des Leistungsbalkens zu füllen.

**4**

: Zeigt die ETA an, d. h. die geschätzte Zeit bis zum Abschluss des Ladevorgangs.

**5**

: Der aktuelle SOC, d. h. der Ladezustand der Batterie, ausgedrückt in %.

**6**

: Zusätzlich angezeigte Werte, Sie können durch Antippen des Symbols zwischen ihnen wechseln.

**7**

: Symbole für MQTT und WiFi. Ausgegraut, wenn keine Verbindung besteht, und farbig bei Verbindung. Tippen Sie auf die Symbole, wenn Sie einen neuen WiFi-Scan oder eine MQTT-Neuverbindung durchführen möchten.

**8**

: Tastenkürzel zum Öffnen der Einstellungsseite für den Zugriff auf erweiterte Einstellungen.

## Die Einstellungsseite {#sec:settings_page}

Um ToM wesentlich besser anpassbar zu machen, gibt es hier die Einstellungsseite, auf die durch Drücken der drei Punkte in der oberen rechten Ecke auf einer der Hauptseiten zugegriffen werden kann. Jetzt können Sie das grundlegende Erscheinungsbild Ihres persönlichen ToM leicht bearbeiten.

<figure id="fig:settings_page" data-latex-placement="H">
<img src="figures/settings_page1.jpg" style="width:80.0%" />
<figcaption>Die erste Einstellungsseite.</figcaption>
</figure>

Die letzte Zeile gibt Ihnen Informationen über Ihren persönlichen ToM und zeigt an:

- Ihre ToM-**Seriennummer** im ersten Feld (im obigen Bild zensiert)

- Die Firmware-Version der Blackbox (ESP) (derzeit 2.4 im Bild)

- Die Firmware-Version des LCD-Touch-Displays (derzeit 2.4 im Bild)

Sie können auf die neueste Version der Firmware aktualisieren, wie in Abschnitt [5](#sec:update_procedure){reference-type="ref" reference="sec:update_procedure"} beschrieben.

### Erste Einstellungsseite

Wie Sie auf dem obigen Bild vielleicht bemerken, wird Ihnen die eingekreiste Schaltfläche in der oberen rechten Ecke sagen, auf welcher Einstellungsseite Sie sich gerade befinden. In diesem Fall ist es die erste, aber Sie können sie drücken, um zur zweiten zu wechseln. Die erste Seite befasst sich hauptsächlich mit dem Erscheinungsbild des ToM+, während die zweite Seite sich mit dem Verhalten des ToM+ und einigen anderen erweiterten Einstellungen befasst.

#### Anpassen der Seitenwerte

Wenn Sie die Reihenfolge der auf einer Seite angezeigten Daten ändern oder sogar Daten von verschiedenen Seiten kombinieren möchten, können Sie dies auf der Einstellungsseite tun, indem Sie diesen Schritten folgen.

<figure data-latex-placement="H">
<img src="figures/settings_page1_values.jpg" style="width:80.0%" />
<figcaption>Anpassen der Seitenwerte.</figcaption>
</figure>

Durch Drücken auf das erste Symbol durchlaufen Sie alle verfügbaren Seiten, deren Symbole zuvor in Abschnitt [3.1.1](#sec:page_icon_list){reference-type="ref" reference="sec:page_icon_list"} erklärt wurden, und Sie können die Werte für diese bestimmte Seite anpassen. Im obigen Bild hat der Benutzer die Gyroskop-Seite ausgewählt, sodass die auf der rechten Seite angezeigten Werte die aktuell für diese Seite festgelegten sind.\
Jedes der fünf Symbole unter der Überschrift **Displayed Data** (Angezeigte Daten) kann durch Antippen angepasst werden, wobei alle Daten durchlaufen werden, bis Sie die gewünschte gefunden haben (Symbolbedeutung in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} erklärt). Zum Beispiel können Sie auch wählen, einige Motordaten auf der Batterieseite anzuzeigen und die beiden zu kombinieren.\

<figure id="fig:icon_arrangement" data-latex-placement="H">
<img src="figures/settings_page1_matching.jpg" style="width:80.0%" />
<figcaption>Resultierende Layoutwerte.</figcaption>
</figure>

Nachdem Sie die angezeigten Werte angepasst haben, **denken Sie daran, sie zu speichern, indem Sie auf die Schaltfläche Beenden drücken**. Die neue Konfiguration wird wie im Bild gezeigt resultieren: Die erste Angabe wird im Vordergrund in der Mitte der Seite angezeigt, während alle anderen in der Tabelle auf der linken Seite in der auf der Einstellungsseite angegebenen Reihenfolge aufgelistet werden.

#### Auswählen der Startseite

Sie können wählen, welche Seite als erstes angezeigt wird, wenn Sie die Armaturenbrett-Seite verlassen. Drücken Sie dazu auf das Symbol, um durch alle verfügbaren Seiten zu blättern, bis Sie die gewünschte finden.

Im Bild unten hat der Benutzer die Batterieseite ausgewählt, sodass das ToM+ diese zuerst anzeigt, wenn er die Armaturenbrett-Seite verlässt.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_bright.jpg" style="width:80.0%" />
<figcaption>Anpassen von Startseite und Helligkeit.</figcaption>
</figure>

#### Anpassen der Displayhelligkeit

Wie Sie im obigen Bild sehen können, können Sie die Displayhelligkeit anpassen, indem Sie auf die Schaltflächen `-` oder `+` drücken. Die Helligkeit kann von 0 bis 100 % eingestellt werden und die Änderung wird sofort angewendet.\

#### Aktivieren/Deaktivieren der Ladeseite

Das ToM+ verfügt über eine spezifische Seite zur Anzeige speziellerer Ladedaten (Abschnitt [3.9](#sec:charging_page){reference-type="ref" reference="sec:charging_page"}). Sie können wählen, ob Sie sie aktiviert (*vertrauen Sie mir, es lohnt sich!*) oder deaktiviert lassen möchten.

Tippen oder schieben Sie den Schalter links, um zwischen ON und OFF zu wählen. Wenn der Schiebeschalter auf ON eingestellt ist, startet das ToM und lädt die Ladeseite, wenn Ihr Twizy lädt, ansonsten, im Zustand OFF, ist es während des Ladevorgangs ausgeschaltet. Um Ihre Änderungen zu speichern, drücken Sie die Beenden-Schaltfläche in der unteren rechten Ecke.\

<figure data-latex-placement="H">
<img src="figures/settings_page1_charge.jpg" style="width:80.0%" />
<figcaption>Anpassen der Ladeseite und Batterie-kWh.</figcaption>
</figure>

#### Einstellen Ihrer Batteriekapazität

Sie können Ihre Batteriekapazität in kWh einstellen, was nützlich ist, wenn Sie einen Twizy mit einer anderen Batterie als der Standardbatterie haben. Dies hilft dem ToM+, die verbleibende Reichweite genauer zu berechnen. Sie können den Wert in Schritten von 0,1 kWh anpassen, indem Sie auf die Schaltflächen `-` oder `+` drücken, und die Änderung wird sofort angewendet. Stellen Sie sicher, dass Sie **Ihre neue Konfiguration speichern**, indem Sie die Beenden-Schaltfläche in der unteren rechten Ecke drücken.

#### Kalibrierung des Gyroskopmoduls

Wenn Sie feststellen, dass die Neigungsdaten des Gyroskops möglicherweise falsch sind, versuchen Sie, die Schaltfläche „CALIBRATE" (KALIBRIEREN) zu drücken, die eine Gyroskopkalibrierung durchführt. Stellen Sie sicher, dass Sie sich mit Ihrem Twizy **auf einer ebenen Fläche** befinden, bevor Sie diesen Vorgang durchführen, da Ihre Neigungsdaten andernfalls noch schlechter wären. Der Vorgang ist hier unten abgebildet:

<figure data-latex-placement="H">
<img src="figures/settings_page1_calibrate.jpg" style="width:80.0%" />
<figcaption>Anpassen der Gyroskopkalibrierung.</figcaption>
</figure>

#### Ändern des Batterieseitenmodus

Sie können auswählen, ob nur die komprimierte Batterie-Info-Seite (Abschnitt [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"}) angezeigt werden soll, wenn Sie auf die Schaltfläche Batterie-Info drücken, oder nicht.

Die beiden verfügbaren Optionen sind *'Condensed'* (Komprimiert) und *'Multiple'* (Mehrfach) und Sie können zwischen ihnen wechseln, indem Sie auf den Text drücken. Die Änderung wird übernommen, sobald Sie die Beenden-Schaltfläche in der unteren rechten Ecke drücken. Der Modus **Multiple** zeigt alle vier Batterieseiten an, die wir in Abschnitt [3.4.2](#sec:condensed_binfo){reference-type="ref" reference="sec:condensed_binfo"} besprochen haben, während der Modus **Condensed** nur die komprimierte Seite anzeigt.\

### Zweite Einstellungsseite

Diese zweite Einstellungsseite befasst sich mit einigen erweiterten Einstellungen zum Ladevorgang. Um darauf zuzugreifen, drücken Sie die eingekreiste Schaltfläche in der oberen rechten Ecke der ersten Einstellungsseite und drücken Sie sie erneut, um zur ersten Einstellungsseite zu navigieren.\

<figure data-latex-placement="H">
<img src="figures/settings_page2.jpg" style="width:80.0%" />
<figcaption>Zweite Einstellungsseite.</figcaption>
</figure>

#### Ändern des Ladezustands

Sie können den maximalen Ladezustand Ihrer Twizy-Batterie wählen, was nützlich ist, wenn Sie die von der Batterie aufgenommene Leistung begrenzen möchten, um ihre Lebensdauer zu erhöhen oder für andere Zwecke. Die Stufe *'0'* bedeutet, dass der Begrenzer deaktiviert ist, während die Stufen *'1'* bis *'7'* bedeuten, dass die entsprechende Ladestufe bis zum verfügbaren Maximum verwendet wird.

Um die Stufe zu erhöhen oder zu verringern, drücken Sie auf die Schaltflächen `-` oder `+`. Die Änderung wird auf die aktuelle Ladung angewendet, falls bereits geladen wird, oder auf die nächste Ladung, falls nicht.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_lvl.jpg" style="width:60.0%" />
<figcaption>Ändern der Ladestufe.</figcaption>
</figure>

#### Manuelle Steuerung des Erweiterungs-PIN1

Einige Benutzer gaben an, dass es nützlich wäre, eine manuelle Steuerung des Erweiterungs-PIN1 zu haben, der normalerweise zur Steuerung eines Zusatzladegeräts verwendet wird. Bei Bedarf können Sie den Erweiterungs-PIN1 also manuell steuern, indem Sie die EIN/AUS-Taste drücken. Die Änderung wird übernommen, sobald Sie die Beenden-Schaltfläche in der unteren rechten Ecke drücken.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_stop.jpg" style="width:80.0%" />
<figcaption>Manuelle Steuerung des Erweiterungs-PIN1 und Stopp-Ladestufe.</figcaption>
</figure>

#### Stoppen der Ladung bei einem bestimmten SOC

Sie können wählen, den Ladevorgang bei einem bestimmten SOC zu stoppen, was nützlich ist, wenn Sie die Batterielebensdauer verlängern möchten. Sie können den Wert von 0 bis 100 % einstellen, indem Sie auf die Schaltflächen `-` oder `+` drücken. Die Änderung wird auf die aktuelle Ladung angewendet, falls bereits geladen wird, oder auf die nächste Ladung, falls nicht.\

#### Durchführung einer Ladung mit maximalen Parametern

Sie können wählen, eine Ladung ohne Leistungs- und SOC-Grenzen durchzuführen, was nützlich ist, wenn Sie ab und zu die Batteriezellen ausgleichen möchten. Sie können die Schaltfläche drücken, um die Ladung mit maximalen Parametern zu starten, die auf die aktuelle Ladung angewendet wird, falls bereits geladen wird, oder auf die nächste Ladung, falls nicht.\

<figure data-latex-placement="H">
<img src="figures/settings_page2_max.jpg" style="width:80.0%" />
<figcaption>Ladung mit maximalen Parametern und Ladevorgang abbrechen.</figcaption>
</figure>

#### Ladevorgang abbrechen

Sie können wählen, den Ladevorgang abzubrechen, was nützlich ist, wenn Sie den Ladevorgang sofort stoppen möchten. Sie können die Schaltfläche drücken, um den Ladevorgang abzubrechen, was sofort ausgeführt wird.\

### Das rechte Seitenmenü

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/SetupRed1.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/WifiBianco.PNG){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------------- -------------------------------------------------------------
  ![image](icons/MQTTBianco.PNG){height="8mm"}   

  ---------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/ExitIcon2.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

# Erweiterte ToM+-Konfigurationen

## Die WLAN-Einstellungsseite {#sec:wifi_settings}

Seit dem zweiten Firmware-Release kann sich Ihr ToM+ über ein integriertes WLAN-Modul mit dem Internet verbinden. Dies ermöglicht es Ihnen, Ihre Twizy-Echtzeitdaten in Kombination mit dem MQTT-Protokoll anzuzeigen, das in Abschnitt [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"} behandelt wird.\

<figure data-latex-placement="H">
<img src="figures/wifi_settings_3d.png" style="width:80.0%" />
<figcaption>Die WLAN-Einstellungsseite.</figcaption>
</figure>

Die Seite speichert bis zu vier Verbindungsprofile, um mit dem Internet verbunden zu sein, wenn Sie zu Hause, bei der Arbeit oder an einem öffentlichen Ort mit kostenlosem WLAN sind.\
Zusätzlich verfügt ToM+ über eine Weboberfläche, auf der Sie Daten in Echtzeit überwachen oder Ihre Einstellungen viel einfacher anpassen können. Schauen wir uns nun an, warum Sie dies tun sollten...

### Vorteile von ToM+ WLAN

Seit dem zweiten Firmware-Release kann sich Ihr ToM+ über ein integriertes WLAN-Modul mit dem Internet verbinden, was Ihnen den Zugriff auf viele weitere Funktionen als zuvor ermöglicht. Jetzt können Sie aus der Ferne auf Ihrem Smartphone auf Ihre Twizy-Daten zugreifen!\
Sie müssen den Ladezustand Ihres Twizy nicht mehr manuell überprüfen, da diese neue Funktion die Daten zum Ladezustand direkt auf Ihrem Smartphone veröffentlicht, und diese sind sowohl geschützt als auch privat. Es erfordert lediglich eine kurze MQTT-Konfiguration.\

- Kein mühsames, manuelles Überprüfen des Twizy-Ladezustands mehr!

- Zahlreiche Möglichkeiten, Ihren Twizy über MQTT in ein IoT-System einzubinden

- WLAN beeinträchtigt weder den Stromverbrauch noch die ToM-Leistung merklich

- Schalten Sie eine neue Webseite mit Twizy-Echtzeitdaten und benutzerfreundlichen ToM-Einstellungen frei

### Hinzufügen eines WLAN-Verbindungsprofils {#sec:add_wifi_profile}

Auf dieser neuen Einstellungsseite haben Sie eine kleine Tabelle mit vier Zeilen und zwei Spalten. Die erste Spalte enthält die **SSID** (d. h. den Namen) des Netzwerks, mit dem Sie sich verbinden möchten. Um genau zu sein, ist es der Name, den Sie auf Ihrem Telefon oder Laptop sehen. Er kann alphanumerisch sein und unterscheidet zwischen Groß- und Kleinschreibung (Großbuchstaben sind wichtig, achten Sie also auf die korrekte Schreibweise!). Die zweite Spalte unter der Überschrift **„KEY"** ist für das WLAN-Passwort vorgesehen.\
Wenn Sie auf eine Tabellenzelle tippen (entweder SSID oder Key), öffnet ToM+ eine Tastaturseite, auf der Sie Ihre Daten eingeben können. Das Drücken von OK bestätigt die eingegebene Zeichenfolge und führt Sie zurück zur WLAN-Einstellungsseite. Wir werden die Tastaturseite in Abschnitt [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"} besprechen.\
Bisher können Sie **vier verschiedene Verbindungsprofile** mit vier Paaren aus SSID und Passwort einrichten. Wenn Sie kein Profil einrichten, aber die WLAN-Schieberegler aktiviert sind, führt ToM+ dennoch alle zwei Minuten einen WLAN-Scan durch, um zu versuchen, öffentliche Verbindungen ohne Passwortschutz zu finden und sich dann zu verbinden. Drücken Sie die Taste mit dem **Pfeil unten rechts zum Speichern**.\
Das vierte WLAN-Verbindungsprofil ist besonders, da das Feld **„KEY 4"** sowohl als Standard-Passwortfeld für die letzte SSID als auch zum Ändern des Standard-Webserver-Passworts verwendet wird, wie in Abschnitt [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"} besprochen wird.

Darüber hinaus gibt es einige Speziacodes, die Sie in dieses Feld eingeben können, um geheime Konfigurationen durchzuführen. Diese Codes unterscheiden zwischen Groß- und Kleinschreibung und wirken sich nicht auf Ihr Feld **„KEY 4"** aus, wenn sie korrekt geschrieben sind, da ToM+ sie nur als Befehle verwendet. Sie können **GIVEMEDF!** eingeben (exakt so wie hier geschrieben, auch mit Unterstrichen und Ausrufezeichen), um die *DF-Fehlernummerierung und Fehlerbeschreibung* sowohl auf dem Display als auch in der Weboberfläche anzuzeigen.\
**ERINNERUNG!** Die Befehle werden von ToM+ nur ausgeführt, wenn sie über diese WLAN-Einstellungsseite eingegeben werden, nicht über die später besprochene Weboberfläche. Da die Herkunft der DF-Nummer nicht eindeutig geklärt ist, erfolgt die Aktivierung dieser Funktion auf eigene Verantwortung.

### WLAN-Verbindung prüfen {#sec:check_wifi_connection}

Die Überprüfung, ob Ihr ToM+ über WLAN mit dem Internet verbunden ist, ist sehr einfach. Auf allen Seiten befindet sich das WLAN-Symbol (behandelt in Abschnitt [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}), das seinen Status anzeigt.

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Tray_WiFiOff.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Tray_WiFi.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------------- -------------------------------------------------------------
  ![image](icons/Tray_WiFi.png){height="8mm"}   

  --------------------------------------------- -------------------------------------------------------------
:::

Wenn Sie spezifischere Informationen darüber erhalten möchten, ob Ihr ToM+ mit einem Netzwerk verbunden ist, können Sie zusätzliche Felder auf der WLAN-Einstellungsseite in der unteren rechten Ecke überprüfen, wie im folgenden Bild gezeigt.

<figure id="fig:wifi_bottom_line" data-latex-placement="H">
<img src="figures/wifi_bottom_line.png" style="width:70.0%" />
<figcaption>Die WLAN-Info im unteren Raster.</figcaption>
</figure>

Wie wir sehen können, wird eine IP-Adresse angezeigt, wenn ToM+ mit einem Netzwerk verbunden ist (hier ist es **10.24.126.204**). Dies ist die Adresse, die ToM+ verwendet, um sich mit dem Internet zu verbinden. Wenn dieses Feld eine Sequenz aus vier Zahlen (von 0 bis 255) enthält, die durch Punkte getrennt sind, ist WLAN verbunden; andernfalls bleibt es leer.

Tippen Sie darauf, um die MAC-Adresse von ToM+ anzuzeigen, und tippen Sie erneut, um zu sehen, mit welcher SSID (Netzwerkname) ToM+ verbunden ist. Weitere interessante Funktionen, bei denen die ToM+-IP-Adresse eine Rolle spielt, werden wir später in Abschnitt [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} sehen.

### WLAN-Funktionen aktivieren/deaktivieren {#sec:enable_disable_wifi}

In der Fußzeile der WLAN-Einstellungsseite befinden sich zwei Schieberegler. Um zwischen den Zuständen EIN und AUS zu wechseln, tippen oder schieben Sie sie einfach. Schauen wir uns an, was die beiden Schieberegler bewirken.\
Der erste dient dazu, **WLAN beim Laden** zu deaktivieren. Dies führt dazu, dass Ihr ToM+ vollständig offline ist und Sie Ihre Twizy-Daten erst wieder aus der Ferne überwachen können, wenn Sie es erneut aktivieren. In diesem Zustand ist das WLAN-Statussymbol immer ausgegraut, wie in Abschnitt [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"} gezeigt.\
Der zweite Schieberegler dient zum Aktivieren von **WLAN beim Fahren**. Dies ermöglicht es Ihrem ToM+, auch während der Fahrt mit Ihrem Twizy mit dem Internet verbunden zu bleiben. Dies ist nützlich, wenn Sie Echtzeitdaten über MQTT auf Ihr Smartphone übertragen möchten. Dadurch wird auch der Zugriff auf die Weboberfläche während der Fahrt ermöglicht und ToM+ sucht ebenfalls nach verfügbaren WLAN-Netzwerken.\
Wie bereits erwähnt, müssen Sie zum *Speichern Ihrer Änderungen* die Pfeiltaste unten rechts drücken. Wenn Sie dies nicht tun, gehen Ihre Änderungen beim Verlassen der Seite verloren.

## Die MQTT-Einstellungsseite {#sec:MQTT}

Wenn Sie bereits einen Blick auf den WLAN-Abschnitt [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"} geworfen haben, wissen Sie wahrscheinlich bereits, dass MQTT erforderlich ist, um aus der Ferne auf Ihre Daten zuzugreifen. Dieser Abschnitt zeigt Ihnen, wie Sie es korrekt einrichten und wie die ToM+-Schnittstelle mit diesem Protokoll umgeht.

<figure data-latex-placement="H">
<img src="figures/mqtt_settings_page.png" style="width:80.0%" />
<figcaption>Die MQTT-Einstellungsseite.</figcaption>
</figure>

Wenn ToM+ über WLAN mit dem Internet verbunden ist, kann MQTT aktiviert werden, und Sie können Ihre Twizy-Echtzeitdaten direkt auf Ihren Geräten anzeigen. Die Seite erlaubt nur eine MQTT-Serverkonfiguration, um **Datensicherheit und Privatsphäre** zu gewährleisten. Sie können diese Parameter sowohl auf dem ToM+ als auch auf seiner Webserver-Seite (Abschnitt [4.4.6](#sec:web_network_settings){reference-type="ref" reference="sec:web_network_settings"}) konfigurieren. Besprechen wir nun, was MQTT ist und einige seiner Hauptvorteile...

### Kurze MQTT-Erklärung {#sec:brief_mqtt}

MQTT ist eines der einfachsten Protokolle in der IT zur Übertragung kleiner Datennutzlasten mithilfe einer **Client/Server-Architektur**. Diese Methode erfordert einen oder mehrere Clients, die normalerweise Daten sammeln und diese dauerhaft speichern und/oder Berechnungen durchführen möchten.

Der Prozess benötigt also einen Server, der Daten von allen Clients verarbeitet und Aufgaben ausführt. Dieser Server wird als **MQTT-Broker** oder einfach Broker bezeichnet und ist in dieser Art von Architektur essenziell. Aber wie können Clients und Server untereinander kommunizieren?\
Der Kommunikationsprozess basiert auf einer Publish/Subscribe-Struktur (Veröffentlichen/Abonnieren). Einige Clients sammeln und veröffentlichen Daten und werden aus diesem Grund **Publisher** genannt, während andere darauf warten, dass diese Daten gesendet werden, und als **Subscriber** bezeichnet werden. Der Broker-Server steht in der Mitte und ist das Vermittlungsgerät, auf dem alle Daten von Publishern gespeichert und an Subscriber gesendet werden. Führen wir nun Topics ein...\
Ein **Topic** ist eine Abfolge von alphanumerischen Zeichen, die sich typischerweise auf ein bestimmtes Thema bezieht und dazu dient, alle Daten zu diesem spezifischen Thema zu speichern (wie ein Container). Topics sind nützlich, um eine Vielzahl von Daten zu organisieren, die von verschiedenen Publishern gesammelt wurden, um diese Informationen nicht zu verwirren. Wie nutzt ToM+ also MQTT?

### ToM+ und MQTT-Kommunikation

Nachdem wir nun wissen, was MQTT ist, wollen wir sehen, wie das MQTT- und ToM+-System tatsächlich funktioniert. ToM+ gilt als Publisher, da es aktualisierte Twizy-Daten sammelt und veröffentlicht. Die Smartphone-Anwendung hingegen ist der Subscriber, da sie darauf wartet, diese vom Twizy eben veröffentlichten Daten zu empfangen. Wer steht in der Mitte? Der Broker-Server.\
Sofern Sie keinen selbst gehosteten Broker-Server haben (wie ich) oder bereits einen kennen, den Sie nutzen können, erkläre ich in Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}, wie Sie Ihren kostenlosen externen Broker-Server einrichten.

Die Kombination von ToM+ mit dem MQTT-Protokoll kann sehr leistungsfähig sein, und wenn Sie Heimautomatisierung und IoT-Systeme mögen, eröffnen sich unendliche Möglichkeiten. Sie können beispielsweise Ihren eigenen Subscriber erstellen, der Aktionen auf Basis der von ToM+ veröffentlichten Daten ausführt.\

### Einrichten eines kostenlosen MQTT-Brokers {#sec:free_broker}

*Haftungsausschluss*: Nehmen Sie sich Zeit für diesen Vorgang, da er für nicht erfahrene Benutzer einige Minuten länger dauern kann, und stellen Sie sicher, dass Sie sich Ihre **Konfigurationsparameter notieren**.\
Wählen Sie zuallererst Ihren MQTT-Broker-Anbieter. Ich persönlich empfehle Maqiatto, da es kostenlos, intuitiv und einfach zu bedienen ist. Besuchen wir also die Tutorial-Seite der offiziellen Website: <https://www.maqiatto.com/examples>. Nun sollten wir eine Seite sehen, wie sie hier gezeigt wird:

<figure data-latex-placement="H">
<img src="figures/mqtt_step1.png" style="width:100.0%" />
<figcaption>Schritt 1: Drücken Sie die Taste „CREATE ACCOUNT“.</figcaption>
</figure>

Wie in der offiziellen Anleitung beschrieben, benötigen Sie ein Konto, um Ihren MQTT-Broker zu erstellen. Drücken Sie also die oben rechts eingekreiste Taste **„Create Account"** und erstellen Sie ein Konto. Sie werden zu dieser Seite weitergeleitet (<https://www.maqiatto.com/signup>), auf der Sie Ihre persönlichen Daten eingeben müssen.

<figure data-latex-placement="H">
<img src="figures/mqtt_step2.png" style="width:100.0%" />
<figcaption>Schritt 2: Füllen Sie Ihre persönlichen Daten aus.</figcaption>
</figure>

Nachdem Sie alle Formularfelder ausgefüllt haben, drücken Sie die grüne Taste **„Signup"** und warten Sie, bis diese Seite (<https://www.maqiatto.com/configure>) mit einer Erfolgsmeldung für die Registrierung erscheint, wie im Bild unten gezeigt:

<figure id="sec:free_broker_add_topics" data-latex-placement="H">
<img src="figures/mqtt_step3.png" style="width:100.0%" />
<figcaption>Schritt 3: IN/OUT-Topics hinzufügen.</figcaption>
</figure>

Auf dieser Seite können Sie Ihre verfügbaren Topics verwalten (siehe Abschnitt [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}) und neue erstellen. Erstellen wir also unser IN- und OUT-Topic zum Senden und Empfangen von ToM-Daten. Wie wir sehen können, gibt es ein festes Präfix (Ihre E-Mail-Adresse), da kostenlose Benutzer dieser Einschränkung unterliegen, aber das ist überhaupt kein Problem.\
In das leere Textfeld nach dem „/"-Symbol sollten wir den Namen eintragen, den wir unseren Topics geben möchten. Wählen Sie ihn sorgfältig aus und stellen Sie sicher, dass er klar und leicht zu merken ist. Ich werde das Eingabe-Topic beispielsweise **TOMin** und das Ausgabe-Topic **TOMout** nennen, aber Sie können den Namen wählen, den Sie bevorzugen.\
Geben Sie für das erste Topic **TOMin** ein und drücken Sie die blaue Taste **„+ Add Topic"**, wie ich es oben getan habe. Wenn der Vorgang erfolgreich abgeschlossen ist, wird eine grüne Pop-up-Meldung angezeigt mit dem Text **„Topic was added for this user"** und ein neuer Eintrag erscheint in der Liste der *„Available Topics"*, die zuvor leer war. Wiederholen Sie den Vorgang nun auch für das Topic **TOMout** und überprüfen Sie erneut, ob das Topic erfolgreich erstellt wurde. Vor diesem Vorgang war die Liste der *„Available Topics"* leer, aber jetzt können wir unsere beiden Topics in der Liste sehen und sie bei Bedarf löschen.

<figure data-latex-placement="H">
<img src="figures/mqtt_step4.png" style="width:80.0%" />
<figcaption>Schritt 4: Ändern Sie Ihr Broker-Passwort.</figcaption>
</figure>

*Dieser Schritt wird empfohlen, ist jedoch optional*. Zu diesem Zeitpunkt entspricht das Broker-Passwort dem Ihres Maqiatto-Kontos und ist überhaupt nicht sicher. Wenn Sie es jedoch nicht ändern möchten oder es Ihnen egal ist, können Sie diesen Schritt überspringen und zum nächsten übergehen.\
Nehmen wir uns also etwas Zeit, um den Broker sicher zu machen und vor unbefugtem Zugriff zu schützen. Der zweite Teil dieser Seite (<https://www.maqiatto.com/configure>) ermöglicht es Ihnen, Ihr Broker-Passwort zu ändern. Geben Sie einfach das neue Passwort in das Textfeld **„New MQTT Password"** ein und drücken Sie dann die blaue Taste **„Change Password"**.

Wenn alles klappt, erscheint eine grüne Pop-up-Meldung mit dem Text **„Broker user password was updated"**. Die Taste zum Ändern des Benutzernamens ist ausgegraut, da Sie Ihren Benutzernamen nur ändern können, wenn Sie Premium-Benutzer sind.

<figure data-latex-placement="H">
<img src="figures/mqtt_step5.png" style="width:70.0%" />
<figcaption>Schritt 5: Notieren Sie sich die Portnummer.</figcaption>
</figure>

Im letzten Abschnitt der Konfigurationsseite (<https://www.maqiatto.com/configure>) befinden sich die **„Port Management"**-Parameter. Notieren Sie sich den MQTT-TCP-Port, der gewöhnlich auf **1883** eingestellt ist (nur um sicherzugehen), da dies die Standard-Portnummer im Internet für das MQTT-Protokoll ist. Nun ist der MQTT-Broker bereit zur Verwendung und wir können zum nächsten Schritt übergehen: der Konfiguration von ToM+ mit den Broker-Parametern.

### ToM+ mit dem MQTT-Broker verbinden {#sec:mqtt_connection}

Nachdem nun klar ist, was MQTT ist (Abschnitt [4.2.1](#sec:brief_mqtt){reference-type="ref" reference="sec:brief_mqtt"}), und wir unseren persönlichen Broker eingerichtet haben (Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"}), wollen wir sehen, wo auf dem Display wir ToM+ mit unserem frisch erstellten Broker verbinden können.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect1.png" style="width:80.0%" />
<figcaption>MQTT-Broker-Verbindungsparameter.</figcaption>
</figure>

Wenn Sie auf das entsprechende Tabellenfeld tippen, öffnet ToM+ eine Tastaturseite, auf der Sie Ihre Daten eingeben können, wie in den WLAN-Einstellungen. Um Symbole oder Zahlen einzugeben, drücken Sie die Taste **„1/3"** auf der Tastatur, um den Zeichensatz zu wechseln. Durch Drücken von **OK** bestätigen Sie die eingegebene Zeichenfolge und kehren zur MQTT-Einstellungsseite zurück. Weitere Informationen zur Tastaturseite finden Sie in Abschnitt [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}. Wenn der Wert zu lang für das Feld ist, scrollt der Text automatisch.\
Als Erstes müssen Sie Ihre **Broker-Adresse** angeben. Im gezeigten Beispiel ist sie auf *„maqiatto.com"* eingestellt. Dies ist die Adresse des Broker-Servers, den wir gerade in Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} erstellt haben.

Anschließend muss die **Portnummer** angegeben werden, auf der der MQTT-Dienst läuft. Sofern Sie sie nicht manuell auf eine andere Nummer eingestellt haben, ist der MQTT-Port immer *1883*.

Als Nächstes folgt das Feld **User**, das den Benutzernamen darstellt, den ToM+ zur Authentifizierung bei der Verbindung mit dem Broker verwendet. Da das Paar aus Benutzername und Passwort einzigartig für Sie ist, verhindert dies, dass unerwünschte Benutzer Zugriff auf Ihren privaten Broker erhalten. In Ihrem Fall ist der Benutzer die E-Mail-Adresse Ihres Maqiatto-Kontos, geschrieben wie *youremail@example.com*.

Danach müssen wir das **Passwort des Brokers** angeben, das sich von dem Ihres Maqiatto-Kontos unterscheiden kann, wenn Sie es wie in Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} empfohlen geändert haben.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect2.png" style="width:80.0%" />
<figcaption>MQTT ToM+ Veröffentlichungsparameter.</figcaption>
</figure>

Konfigurieren wir nun unser **OUT-Topic**, in dem ToM+ die Twizy-Daten veröffentlichen wird. In Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} haben wir ein Out-Topic namens TOMout erstellt, aber der vollständige Name des Topics muss auch **Ihre E-Mail-Adresse als Präfix** enthalten, gefolgt von einem „/"-Symbol und dem Topic-Namen „TOMout". Im Beispiel ist es auf *„youremail@gmail.com/TOMout"* eingestellt.

Jetzt ist es Zeit für das **IN-Topic**, über das ToM+ MQTT-Befehle empfängt. Wie beim OUT-Topic haben wir ein In-Topic namens TOMin erstellt, aber der vollständige Name des Topics muss auch **Ihre E-Mail-Adresse als Präfix** enthalten, gefolgt von einem „/"-Symbol und dem Topic-Namen „TOMin". Im Beispiel ist es auf *„youremail@gmail.com/TOMin"* eingestellt.

Wenn ein MQTT-Publisher eine Nachricht an den Broker sendet, wird seine Verbindung durch Benutzername und Passwort authentifiziert, aber er veröffentlicht unter einem Alias, den Sie *willkürlich wählen können*. Es ist wichtig, keine Leerzeichen in der **Client ID** zu verwenden; es sind nur alphanumerische Zeichen und Symbole erlaubt. Denken Sie daran, dass es ratsam ist, diese einfach und klar zu halten, wie im Beispiel: *„TwizOMeter"*.

Der letzte Parameter ist die **Veröffentlichungsfrequenz** (Publish Frequency), die die Zeit zwischen den einzelnen ToM+-Veröffentlichungen darstellt. Sie wird in Millisekunden *(ms)* ausgedrückt und kann auf einen beliebigen Wert größer als 1000 ms (eine Sekunde) eingestellt werden. Der Standardwert beträgt *5000 ms* (fünf Sekunden) und stellt einen guten Kompromiss zwischen Datenaktualität und Netzwerkauslastung dar.\
Um Ihre **Änderungen zu speichern**, müssen Sie die Pfeiltaste unten rechts drücken. Wenn Sie dies nicht tun, gehen Ihre Änderungen beim Verlassen der Seite verloren. Nun ist ToM+ bereit, Daten über das MQTT-Protokoll zu senden und zu empfangen.\

### MQTT-Funktionen aktivieren/deaktivieren {#sec:enable_disable_mqtt}

Wenn Sie das Veröffentlichen von Daten mit dem MQTT-Protokoll vorübergehend oder dauerhaft deaktivieren möchten, drücken oder schieben Sie den linken Schieberegler mit der Aufschrift **„PUBLISH"** im Bild unten. Von da an wird ToM+ keine Twizy-Daten mehr über MQTT veröffentlichen, bis Sie es wieder aktivieren.

<figure data-latex-placement="H">
<img src="figures/mqtt_connect3.png" style="width:80.0%" />
<figcaption>Untere MQTT-Schieberegler.</figcaption>
</figure>

Der rechte Schieberegler unter **„SUBSCRIBE"** ermöglicht es ToM+, Befehle von externen Geräten zu empfangen, die auf dem angegebenen IN-Topic veröffentlicht werden. Dies ist nützlich, wenn Sie ein an den ToM+-Erweiterungsanschluss angeschlossenes Gerät über MQTT steuern möchten (z. B. eine smarte Steckdose zum Ferneinschalten des Ladevorgangs). Sie können diese Funktion jederzeit aktivieren oder deaktivieren, indem Sie die Taste drücken oder schieben.\

### ToM+ MQTT-Verbindung prüfen

Neben den beiden Schiebereglern befindet sich ein kleines **„STATUS"**-Feld, das anzeigt, ob die MQTT-Verbindung funktioniert oder nicht. Wenn ToM+ mit dem angegebenen MQTT-Broker verbunden ist, sehen Sie den Text *„CONNECTED"*. Wenn ein Problem mit der Broker-Verbindung vorliegt oder WLAN deaktiviert ist (wie in Abschnitt [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"} gesehen), funktioniert MQTT nicht ordnungsgemäß und es erscheint die Meldung *„DISCONNECTED"*, wie im Bild unten gezeigt.

<figure data-latex-placement="H">
<img src="figures/mqtt_status.png" style="width:80.0%" />
<figcaption>MQTT-Statusfeld.</figcaption>
</figure>

Übrigens können Sie den MQTT-Verbindungsstatus auch überprüfen, indem Sie auf die Status-Symbolleiste schauen (Abschnitt [3.3.3](#sec:status_icon_bar){reference-type="ref" reference="sec:status_icon_bar"}), in der das MQTT-Symbol lila ist, wenn die Verbindung hergestellt ist, andernfalls ist es ausgegraut.

Um Ihre **Änderungen zu speichern**, müssen Sie die Pfeiltaste unten rechts drücken. Wenn Sie dies nicht tun, gehen Ihre Änderungen beim Verlassen der Seite verloren.\

## Die Tastaturseite {#sec:keyboard_page}

Wenn Sie in der WLAN- oder MQTT-Einstellungsseite auf eine Tabellenzelle tippen, öffnet ToM+ eine Tastaturseite, auf der Sie Ihre Daten eingeben können. Die Tastaturseite ist sehr intuitiv und einfach zu bedienen. Sie können zwischen drei verschiedenen Zeichensätzen wechseln, indem Sie die Taste **„1/3"** in der unteren linken Ecke der Tastatur drücken.

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page1.jpg" />
<figcaption>Erster Zeichensatz: Buchstaben.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page1_caps.jpg" />
<figcaption>Erster Zeichensatz: Großbuchstaben.</figcaption>
</figure>
<figcaption>Erster Zeichensatz: Großbuchstaben.</figcaption>
</figure>

Im **ersten Zeichensatz** können Sie Buchstaben in Klein- oder Großschreibung eingeben, indem Sie die im ersten Bild gelb eingekreiste Shift-Taste drücken. Wenn Sie etwas eingeben, erscheint es im Textfeld oben auf der Tastatur. Wenn Sie ein Zeichen löschen möchten, drücken Sie einfach die Rücktaste (Backspace).

<figure data-latex-placement="ht">
<figure>
<img src="figures/keyboard_page2.jpg" />
<figcaption>Zweiter Zeichensatz: Symbole.</figcaption>
</figure>
<figure>
<img src="figures/keyboard_page3.jpg" />
<figcaption>Dritter Zeichensatz: Zahlen und mehr.</figcaption>
</figure>
<figcaption>Dritter Zeichensatz: Zahlen und mehr.</figcaption>
</figure>

Der **zweite Zeichensatz** ist für Symbole gedacht und der **dritte** für Zahlen und weitere Sonderzeichen. Um zum dritten Zeichensatz zu gelangen, drücken Sie einfach die Taste **„2/3"** in der unteren linken Ecke der Tastatur. Im dritten Zeichensatz können Sie durch Drücken der Taste **„3/3"** wieder zum ersten Zeichensatz zurückkehren. Auf diesen beiden Seiten hat die Shift-Taste keine Funktion, da sie nicht benötigt wird.\
Wenn Sie mit der Eingabe fertig sind, drücken Sie die Taste **OK**, um Ihre Eingabe zu bestätigen und zur vorherigen MQTT- oder WLAN-Einstellungsseite zurückzukehren, wo das bearbeitete Feld aktualisiert wird.

### Die reine Zahlentastatur

In einigen Feldern, wie z. B. der MQTT-Veröffentlichungsfrequenz, sind nur Zahlen erlaubt. In diesem Fall öffnet ToM+ eine reine Zahlentastaturseite, wie im Bild unten gezeigt.

<figure data-latex-placement="H">
<img src="figures/keyboard_num_only.jpg" style="width:80.0%" />
<figcaption>Reine Zahlentastatur.</figcaption>
</figure>

Wie Sie sehen können, ist das Layout dasselbe wie beim dritten Zeichensatz der vollständigen Tastatur, jedoch auf Zahlen und einige Sonderzeichen beschränkt. Sie werden auch bemerken, dass die Taste zum Wechseln des Zeichensatzes nicht verfügbar ist, da sie in diesem Fall nicht benötigt wird. Die Rücktaste steht weiterhin zum Löschen von Zeichen zur Verfügung, und die **OK-Taste** bestätigt Ihre Eingabe und führt zurück zur vorherigen Seite.

## Der Webserver {#sec:web_server}

Der Webserver ist eine neue Funktion, die mit dem zweiten Firmware-Release eingeführt wurde. Er ermöglicht Ihnen den Fernzugriff auf Ihre ToM+-Einstellungen und -Daten von jedem Gerät mit einem Webbrowser, wie z. B. Ihrem Smartphone, Tablet oder PC. Dies ist besonders nützlich für die Verwaltung von Standard- und **erweiterten Konfigurationen**, die auf dem ToM+-Display nicht verfügbar sind.

Zusätzlich können Sie den Webserver nutzen, um **WLAN und MQTT** viel einfacher einzurichten als nur über das ToM+-Display mit der Tastaturseite (Abschnitt [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}).\

<figure data-latex-placement="H">
<img src="figures/landing_page.png" style="width:46.0%" />
<figcaption>Startseite des Webservers.</figcaption>
</figure>

### Die Startseite

Auf der oben gezeigten Startseite sehen Sie zwölf Schaltflächen, die Ihnen Zugriff auf verschiedene Seiten des Webservers geben. Hier gebe ich einen kurzen Überblick über die auf jeder Seite verfügbaren Funktionen, bevor diese in den folgenden Absätzen vertieft werden. In diesem Abschnitt dienen die Symbole nur als visuelle Hilfe:\

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/BatteryInfo2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Street0Ok_v2.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ------------------------------------------------ -------------------------------------------------------------
  ![image](icons/Tray_WiFiOff.png){height="8mm"}   

  ------------------------------------------------ -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Pin1.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Alarm.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Swap.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/Swap.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ---------------------------------------- -------------------------------------------------------------
  ![image](icons/CEta.png){height="8mm"}   

  ---------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Timer.PNG){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  --------------------------------------- -------------------------------------------------------------
  ![image](icons/Kmh.png){height="8mm"}   

  --------------------------------------- -------------------------------------------------------------
:::

::: tcolorbox
  ----------------------------------------- -------------------------------------------------------------
  ![image](icons/Error.png){height="8mm"}   

  ----------------------------------------- -------------------------------------------------------------
:::

### Auf den Webserver zugreifen {#sec:web_server_access}

ToM+ ermöglicht es Ihnen, sich auf zwei Arten mit seiner Webserver-Seite zu verbinden, die beide in unterschiedlichen Situationen nützlich sind. Bevor wir beginnen, denken Sie daran, dass eine **IP-Adresse** im Grunde der numerische Name Ihres Geräts in einem Netzwerk ist (z. B. *192.168.1.100*).

***Für beide Methoden muss ToM+ mit einem Netzwerk verbunden sein.*** Stellen Sie also sicher, dass Ihr ToM+ entweder ein wie in Abschnitt [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"} erklärtes WLAN-Profil konfiguriert hat oder mit einem passwortfreien WLAN-Netzwerk verbunden ist. Um zu überprüfen, ob Ihr ToM+ verbunden ist, lesen Sie bitte Abschnitt [4.1.3](#sec:check_wifi_connection){reference-type="ref" reference="sec:check_wifi_connection"}.\
**Die erste und einfachste Einrichtung** besteht darin, den Hotspot Ihres Telefons ohne Passwort zu verwenden, sodass sich ToM+ verbindet, ohne ein WLAN-Profil konfigurieren zu müssen. Rufen Sie dann (immer noch auf Ihrem Telefon) Chrome oder Safari (oder einen beliebigen Webbrowser) auf und geben Sie die IP-Adresse von ToM+ ein (gezeigt in Abbildung [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"}).\
**Die zweite Methode** funktioniert nur, wenn Sie sich in unmittelbarer Nähe des Twizy innerhalb der WLAN-Reichweite befinden. Sie können Ihr Telefon oder Ihren Laptop verwenden, um einen WLAN-Scan durchzuführen, und dann je nach Modell nach dem Netzwerk *„ToM+ AP"*, *„Twiz o'Meter AP"* oder *„BigToM AP"* suchen. Als Nächstes sollten Sie sich mit dem **korrekten Passwort** mit diesem Netzwerk verbinden. Es ist anfänglich auf das Wort „pass", gefolgt von der Seriennummer Ihres Geräts, eingestellt (z. B. *pass129777*). Die Seriennummer finden Sie auf der Einstellungsseite, wie in Abbildung [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"} erklärt. Sie können es dann auf Wunsch ändern, aber es gibt kein Passwort-Wiederherstellungssystem (siehe Abschnitt [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}). Sobald Sie mit dem ToM+ Access Point verbunden sind, geben Sie in einem beliebigen Browser seine statische IP-Adresse ein, die **192.188.1.188** lautet.

### Webserver-Passwort ändern {#sec:web_change_password}

Um das Passwort für den Webserver zu ändern, rufen Sie auf dem Display die WLAN-Einstellungsseite auf (Abschnitt [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) und tippen Sie auf das Feld **„KEY 4"**. Dadurch wird die Tastaturseite geöffnet (Abschnitt [4.3](#sec:keyboard_page){reference-type="ref" reference="sec:keyboard_page"}), auf der Sie Ihr neues Passwort eingeben können. Dieses Passwort wird dann sowohl als Access-Point-Passwort als auch für das vierte WLAN-Verbindungsprofil verwendet.

### Datenmonitor-Seite {#sec:web_data_monitor}

Wie in der Einleitung erwähnt, listet diese Seite alle verfügbaren ToM+-Daten auf, geordnet in sieben verschiedenen Tabellen, von denen jede nur die in ihrer Kopfzeile angegebenen Daten enthält. Die Datenverteilung entspricht der in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} verwendeten und kann nicht geändert werden.

Diese Werte werden **alle 10 Sekunden aktualisiert** und sind mit ihrer Maßeinheit gekoppelt. Machen Sie sich keine Sorgen um Ihre Privatsphäre, da Ihre Daten verpackt in einer speziellen Paketstruktur übertragen werden, die schwer abzuhören oder zu knacken ist. Darüber hinaus nutzt der Webserver keine externen Dienste oder MQTT für die Überwachung, sodass Ihre Daten privat und sicher bleiben. Die Seite wird vollständig direkt von der Blackbox generiert und unterliegt keiner weiteren Verarbeitung.

<figure data-latex-placement="H">
<img src="figures/monitor_page1.png" style="width:100.0%" />
<figcaption>Datenmonitor-Seite — obere Tabellen.</figcaption>
</figure>

Im zweiten Teil der Seite befinden sich die letzten drei Tabellen, die Dashboard-Daten und Daten des Erweiterungsanschlusses enthalten; die letzte enthält alle Spannungen und Temperaturen der Batterie-Infos. Drücken Sie die vom roten Pfeil angezeigte grüne Taste **„HOME"**, um zur Startseite zurückzukehren.

<figure data-latex-placement="H">
<img src="figures/monitor_page2.png" style="width:100.0%" />
<figcaption>Datenmonitor-Seite — untere Tabellen.</figcaption>
</figure>

### Fahrtenverlauf-Seite {#sec:web_trip_history}

Diese enthält die Werte der zuvor in Abschnitt [3.6](#sec:trip_page){reference-type="ref" reference="sec:trip_page"} besprochenen Fahrtenseite. Sie kann bis zu 5 verschiedene Datensätze speichern, und selbst wenn die auf dem Display angezeigten Daten begrenzt sind, werden sie auf der Webserver-Seite alle angezeigt. Die erste Tabelle zeigt Fahrten, jeweils organisiert in fünf Zeilen, und die Kopfzeilen jedes Datensatzes sind in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} aufgeführt.

<figure data-latex-placement="H">
<img src="figures/trip_page1.png" style="width:100.0%" />
<figcaption>Fahrtenverlauf-Seite — Fahrtendaten.</figcaption>
</figure>

Die zweite Tabelle zeigt die letzten zwanzig Fahrten (ab der aktuellsten) mit denselben Kopfzeilen wie die erste Tabelle. Sie können zur Startseite zurückkehren, indem Sie die grüne Taste **„HOME"** direkt unter der zweiten Tabelle drücken.

<figure data-latex-placement="H">
<img src="figures/trip_page2.png" style="width:100.0%" />
<figcaption>Fahrtenverlauf-Seite — Fahrtenhistorie.</figcaption>
</figure>

### Netzwerkeinstellungsseite {#sec:web_network_settings}

Auf dieser Seite können Sie WLAN-Profile und den MQTT-Broker konfigurieren, ohne sich mit der Tastatur des ToM+-Displays abmühen zu müssen. Die Seite ist in zwei Haupttabellen unterteilt, eine für WLAN (Abschnitt [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}) und die andere für MQTT-Einstellungen (Abschnitt [4.2](#sec:MQTT){reference-type="ref" reference="sec:MQTT"}).\
Wie Sie im Bild sehen können, enthält die erste alle vier Profile, die zuvor auf dem ToM+ eingestellt wurden, oder, falls nicht, deren Standardwerte. Das Gleiche gilt für Passwörter, die erst sichtbar sind, wenn Sie die Schaltfläche „O" neben dem Passwort drücken, das Sie sehen möchten. Erneutes Drücken blendet das Passwort wieder aus. Hier können Sie auch das WLAN-Passwort für den Access Point ändern (Abschnitt [4.4.3](#sec:web_change_password){reference-type="ref" reference="sec:web_change_password"}).

<figure data-latex-placement="H">
<img src="figures/wifi_page1.png" style="width:100.0%" />
<figcaption>Netzwerkeinstellungsseite — WLAN-Tabelle.</figcaption>
</figure>

Die beiden Kontrollkästchen erfüllen dieselben Funktionen wie die beiden Schieberegler auf der WLAN-Einstellungsseite des ToM+. Wofür diese verwendet werden, erfahren Sie in Abschnitt [4.1.4](#sec:enable_disable_wifi){reference-type="ref" reference="sec:enable_disable_wifi"}. Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren.

<figure data-latex-placement="H">
<img src="figures/wifi_page3.png" style="width:100.0%" />
<figcaption>Netzwerkeinstellungsseite — WLAN-Statustabelle.</figcaption>
</figure>

Wenn Ihr ToM+ mit einem Netzwerk verbunden ist, erscheint unterhalb der eben besprochenen Tabelle eine kleine Tabelle, deren Zeilen drei Hauptinformationen enthalten: die SSID, die IP-Adresse des ToM+ und die MAC-Adresse. Diese Daten finden Sie auch auf dem ToM+-Display auf der WLAN-Einstellungsseite, wie zuvor in Abbildung [4.1](#fig:wifi_bottom_line){reference-type="ref" reference="fig:wifi_bottom_line"} gezeigt.\
Die zweite Haupttabelle enthält hingegen die Einstellungen des MQTT-Brokers, wie sie zuvor auf dem ToM+-Display konfiguriert wurden, oder, falls nicht, Standardwerte (*z. B. „broker.address"*). Sie können diese bequem manuell auf dieser Webserver-Seite ändern, was viel komfortabler ist als die Verwendung der Tastatur des ToM+-Displays. Schauen Sie sich im Bild unten an, wie diese Tabelle nach der Konfiguration aussehen kann.

<figure data-latex-placement="H">
<img src="figures/wifi_page2.png" style="width:100.0%" />
<figcaption>Netzwerkeinstellungsseite — MQTT-Tabelle.</figcaption>
</figure>

Die beiden Kontrollkästchen erfüllen dieselben Funktionen wie die beiden Schieberegler auf der MQTT-Einstellungsseite von ToM+. Wofür sie verwendet werden, erfahren Sie in Abschnitt [4.2.5](#sec:enable_disable_mqtt){reference-type="ref" reference="sec:enable_disable_mqtt"}. Wenn Ihr ToM+ mit dem MQTT-Broker verbunden ist, enthält die Tabellenkopfzeile den Text **„(CONNECTED!)"**.\
Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren. Am Ende dieser Seite befindet sich, im Bild durch einen roten Pfeil gekennzeichnet, die grüne Schaltfläche **„HOME"**, um zur Startseite zurückzukehren.

### Erweiterungseinstellungsseite {#sec:web_expansion_settings}

Diese Seite enthält die Konfiguration für PIN1 und PIN2 des Erweiterungsanschlusses sowie die Konfiguration für die rechte Scheibenwischerhebels-Taste. Sie kann sehr nützlich sein, wenn Sie Dinge anpassen und Ihrem ToM+ eine persönliche Note verleihen möchten. Die Pin-Belegung des Erweiterungsanschlusses ist in Abbildung [1.1](#fig:expansion_pinout){reference-type="ref" reference="fig:expansion_pinout"} dargestellt. Da es sich um allgemeine Ein-/Ausgabe-Pins handelt, können Sie den Modus für jeden einzelnen Pin je nach Bedarf wählen.\
Wenn Sie den Modus **„INPUT"** wählen, lauscht diese Leitung auf das im nächsten Feld angegebene Signal. Dies kann beim Einrichten eines sehr spezifischen Alarms sehr nützlich sein, aber wir werden dies später besprechen. Wenn Sie hingegen den Modus **„OUTPUT"** wählen, überträgt ToM+ das im nächsten Feld angegebene Signal, das HIGH (5V) oder LOW (0V) sein kann, wenn ein Alarm ausgelöst wird. Wie bereits erwähnt, wird dies in Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"} vertieft.\
Seit den neuesten Firmware-Releases wurden den Erweiterungs-PINs neue Modi neben INPUT und OUTPUT hinzugefügt. Schauen wir uns diese genauer an:\

- **IR CONTROLLER**: Dieser Modus ermöglicht die Steuerung von ToM+ über eine Infrarot-Fernbedienung.

- **KEY+ CONTROLLER**: Dieser Modus ermöglicht die Steuerung Ihres ToM+ über eine Infrarot-Drehfernbedienung. Für diese beiden ersten Modi erscheint eine zusätzliche Konfigurationstabelle.

- **SERIAL TX**: Ermöglicht die Konfiguration einer seriellen TX-Leitung (noch nicht implementiert).

- **SERIAL RX**: Ermöglicht die Konfiguration einer seriellen RX-Leitung (noch nicht implementiert).

- **CTRL BUTTON**: Dieser Modus ermöglicht es Ihnen, die rechte Scheibenwischerhebels-Taste als Steuertaste für Ihre ToM+-Gesten zu verwenden.

#### Standard-OUTPUT-Modus

Sowohl im **„OUTPUT"**- als auch im **„INPUT"**-Modus müssen Sie zuerst zwischen *„Active High"* und *„Active Low"* wählen. Wenn ein Alarm auslöst, wird ein LOW/HIGH-Signal an den PIN gesendet, der als Alarmausgang ausgewählt wurde (entweder PIN1 oder PIN2).

Wenn Sie *„Active High"* wählen, ist das gesendete Signal HIGH (5V) und wird normalerweise auf LOW (0V) gehalten.

Wenn Sie *„Active Low"* wählen, ist das gesendete Signal LOW (0V) und wird normalerweise auf HIGH (5V) gehalten.

<figure data-latex-placement="H">
<img src="figures/expansion_page1.png" style="width:100.0%" />
<figcaption>Erweiterungseinstellungsseite — PIN1-Tabelle.</figcaption>
</figure>

Wie Sie im Bild unten sehen können, können Sie bei Auswahl des Modus **„OUTPUT"** auch den *„Output Type"* wählen. Dies ist nützlich, wenn Sie ein sehr spezifisches Ausgabegerät haben, das eine zusätzliche Verwaltung erfordert, die nicht auf das Standard-HIGH/LOW-Signal beschränkt ist. Um dies zu erreichen, können Sie aus einer Liste bereits verwalteter Ausgabegeräte wählen, die im Bild oben hervorgehoben sind.\
Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren. Wenn Sie eine Idee für ein neues Ausgabegerät haben, das für die Community nützlich sein könnte, können Sie mich gerne kontaktieren.\

- *„Normal"*: Dies ist der Standard-OUTPUT-Modus, beschränkt auf HIGH/LOW-Signale.

- *„Charger auxilliary fan"*: Damit können Sie einen Zusatzlüfter steuern. Sie müssen einen Alarm für die Ladegerättemperatur mit einem Schwellenwert einrichten. Wenn dieser beim Laden ausgelöst wird, beginnt der Lüfter mit der Kühlung des Ladegeräts und stoppt erst, wenn die Temperatur unter den ausgewählten Schwellenwert mit einer festen Hysterese fällt (falls erforderlich auch nach dem Ende des Ladevorgangs).

- *„Reku break light"*: Damit können Sie eine Relaisplatine anschließen, die das Bremslicht steuert, um es im Rekuperationsmodus einzuschalten. Dies ist besonders nützlich, wenn Ihr Twizy getunt ist, um die Rekuperationsleistung zu erhöhen.

- *„Auxilliary charger"*: Damit können Sie ein Zusatzladegerät mit einem Alarm für SOC oder Batteriespannung steuern. Es ermöglicht den Anschluss einer Relaisplatine, die bei Bedarf ein Zusatzladegerät aktiviert oder deaktiviert. Es schaltet sich nur im Lademodus mit einer kleinen festen Verzögerung ein.

- *„Motor fan"*: Damit können Sie einen Motorlüfter mit einem Alarm für die Motortemperatur steuern. Es funktioniert genauso wie der Ladegerätlüfter mit dem Unterschied, dass dies nur während der Fahrt funktioniert.

#### Standard-INPUT-Modus

Wie Sie im Bild unten sehen können, erscheinen bei Auswahl des Modus **„INPUT"** keine zusätzlichen Tabellen. Dieser Modus stützt sich stark auf die Alarmkonfiguration und Auslöser; lesen Sie daher bitte Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}. Wir haben in der zweiten Tabelle den Modus **„INPUT"** gewählt, der genauso funktioniert, aber für PIN2 des Erweiterungsanschlusses vorgesehen ist.

Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren.

<figure data-latex-placement="H">
<img src="figures/expansion_page3.png" style="width:100.0%" />
<figcaption>Erweiterungseinstellungsseite — PIN2-Tabelle.</figcaption>
</figure>

#### IR CONTROLLER-Modus

Zunächst benötigen Sie einen IR-Empfänger (entweder einen Sensor oder ein Modul wie das im ersten Bild), der an einen der PINs der Erweiterungsplatine angeschlossen wird. Dieser Modus ist für die Verwendung mit einer allgemeinen IR-Fernbedienung vorgesehen, aber ich persönlich empfehle die im zweiten Bild unten gezeigte, die speziell für die Anbringung am Lenkrad entwickelt wurde.

<figure data-latex-placement="ht">
<figure>
<img src="figures/ir_receiver.jpg" />
<figcaption>IR-Empfängermodul.</figcaption>
</figure>
<figure>
<img src="figures/ir_controller_photo.jpg" />
<figcaption>IR-Fernbedienung für das Lenkrad.</figcaption>
</figure>
<figcaption>IR-Fernbedienung für das Lenkrad.</figcaption>
</figure>

Wenn Sie den Modus **„IR CONTROLLER"** für die Tabelle von PIN1 oder PIN2 wählen, denken Sie daran, die Schaltfläche **„SAVE"** zu drücken, um Ihre Änderungen zu speichern. Sobald Sie gespeichert haben, wird die Seite neu geladen und unten erscheint eine zusätzliche Tabelle, die Sie im folgenden Bild sehen können.

<figure data-latex-placement="H">
<img src="figures/ir_settings.png" style="width:80.0%" />
<figcaption>Erweiterungseinstellungsseite — IR-Einstellungstabelle.</figcaption>
</figure>

Diese Tabelle hilft Ihnen, jede Taste der IR-Fernbedienung mit dem entsprechenden IR-Code zu koppeln. Im oberen Teil der Tabelle befindet sich ein kleiner Textbereich, den Sie als **IR-Code-Empfangsmonitor** verwenden können, um IR-Codes Ihrer Fernbedienung nach dem Anschließen des IR-Empfängers in Echtzeit zu testen.\
Damit können Sie die anderen Felder entsprechend ausfüllen. Das letzte ist besonders wichtig und ist im Grunde der Code, den die Fernbedienung sendet, wenn Sie eine Taste gedrückt halten. Vergessen Sie danach nicht, die Schaltfläche **„SAVE"** zu drücken, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren. Schließlich befindet sich daneben eine nützliche Schaltfläche **„Default"**, um Ihre Änderungen bei Bedarf einfach zurückzusetzen.

#### KEY+ CONTROLLER-Modus

Dieser Modus ist dem eben besprochenen sehr ähnlich, ist jedoch für die Verwendung mit einem anderen Controller-Typ vorgesehen (dem im Bild unten). Es handelt sich um einen drahtlosen Bluetooth-Drehcontroller für Autoradios, der je nachdem, wie schnell/langsam Sie den äußeren Ring drehen, verschiedene Aktionen ausführt. Und natürlich hat er auch noch einige Tasten im inneren Teil.\

<figure data-latex-placement="H">
<img src="figures/keyp_controller.jpg" style="width:40.0%" />
<figcaption>Drahtloser Bluetooth-Drehcontroller.</figcaption>
</figure>

Wenn Sie den Modus **„KEY+ CONTROLLER"** für die Tabelle von PIN1 oder PIN2 wählen, denken Sie daran, die Schaltfläche **„SAVE"** zu drücken, um Ihre Änderungen zu speichern. Sobald Sie gespeichert haben, wird die Seite neu geladen und unten erscheint eine zusätzliche Tabelle, die Sie im Bild unten sehen können.

<figure data-latex-placement="H">
<img src="figures/keyp_settings.png" style="width:80.0%" />
<figcaption>Erweiterungseinstellungsseite — KEY+-Einstellungstabelle.</figcaption>
</figure>

Dies funktioniert genauso wie die IR-Einstellungstabelle. Der Hauptunterschied besteht darin, was ToM+ vom Erweiterungsanschluss liest, was kein IR-Code mehr ist, sondern eine Spannung.

Im Bild oben sind die Standardwerte dargestellt, die von *0* bis *3,3V* reichen und ohne Dezimalpunkt geschrieben werden. Beispiel: *018* bedeutet *0,18V* und *157* bedeutet *1,57V* usw. ToM+ hat eine Toleranz von *0,05V* auf die Eingabewerte, um Spannungsschwankungen zu vermeiden.\
Vergessen Sie danach nicht, die Schaltfläche **„SAVE"** zu drücken, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren. Schließlich befindet sich daneben eine nützliche Schaltfläche **„Default"**, um Ihre Änderungen bei Bedarf einfach zurückzusetzen.

#### CTRL BUTTON-Modus {#sec:web_wiper_stalk}

Diese letzte Tabelle enthält die Konfiguration, die erforderlich ist, damit die mitgelieferte rechte **Scheibenwischerhebels-Taste** (Abbildung [1.4](#fig:wiper_stalk_button){reference-type="ref" reference="fig:wiper_stalk_button"}) funktioniert. Sie können diese Taste verwenden, um durch die gesamte ToM+-Benutzeroberfläche zu navigieren, ohne den Touchscreen zu benutzen, und zwar mit diesen drei Haupt-**Aktionen**: *„Browse items"*, *„Change page"*, *„Select-deselect"*. Um dies zu erreichen, gibt es drei Arten von **Tastendrücken**: *„Short"*, *„Medium"*, *„Long"*.\

<figure data-latex-placement="H">
<img src="figures/expansion_page2.png" style="width:100.0%" />
<figcaption>Erweiterungseinstellungsseite — Tabelle für Scheibenwischerhebels-Taste.</figcaption>
</figure>

Im ersten Teil dieser Tabelle können Sie diese Aktionen mit den von Ihnen bevorzugten Gesten neu anordnen.\

- *„Browse items"*: Bewegt eine kleine weiße Markierung neben die aktuell ausgewählten Daten.

- *„Change page"*: Ermöglicht das Durchblättern der in der Rotation vorhandenen Seiten.

- *„Select-deselect"*: Simuliert das Tippen auf die ausgewählten Daten (z. B. Wechsel von Hintergrund zu Vordergrund).\

Im zweiten Teil der Tabelle können Sie die **Seiten auswählen, die Sie überspringen möchten**, wenn Sie mit der Geste *„Change page"* durch die verfügbaren Seiten blättern. Wenn ich beispielsweise die Batterie-Info-Seite beim Blättern mit der Taste nicht überwachen möchte, deaktiviere ich sie einfach, und sie wird aus der Rotation entfernt.\
Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um Ihre Änderungen zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren. Am Ende dieser Seite befindet sich, im Bild durch einen roten Pfeil gekennzeichnet, die grüne Schaltfläche **„HOME"**, um zur Startseite zurückzukehren.

### Alarmauslöser-Seite {#sec:web_alarm_triggers}

Wenn auf ToM+ etwas passiert und Sie darüber benachrichtigt werden möchten, können Sie auf dieser Seite auswählen, wie und wann Sie benachrichtigt werden möchten. Sie können bis zu **zehn Alarme** gleichzeitig laufen lassen, und ToM+ überprüft ständig den Status jeder Bedingung. Im Bild ist die erste Tabelle dargestellt, in der Sie derzeit aktive Alarme sehen können.

<figure data-latex-placement="H">
<img src="figures/alarm_page1.png" style="width:100.0%" />
<figcaption>Alarmseite — Liste bestehender Alarme.</figcaption>
</figure>

Die Kopfzeilen der Tabellen sind praktisch die Elemente der Bedingung, auf die ToM+ lauscht.\

- **ITEM**: Dies sind die zu prüfenden Daten, ausgewählt aus der Liste in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"}.

- **CONDITION**: Dies ist das Operatorzeichen, das beim Vergleichen der Werte verwendet wird.

- **VALUE**: Dies ist ein vorzeichenbehafteter Ganzzahlwert, der als zweiter Begriff des Vergleichs verwendet wird.

- **ACTION**: Dies ist die Aktion, die ausgeführt wird, wenn der Alarm auslöst. Siehe die nächste Tabelle.

- **SEND-MQTT**: Dies ist ein binäres Feld; wenn es angekreuzt ist, wird eine Nachricht auf dem MQTT-Topic veröffentlicht.

- **COMMAND**: Dies ist eine optionale Zeichenfolge, die als zusätzlicher Befehl gesendet werden kann.

 \
Der erste Alarmauslöser prüft den Batterieverbrauch und aktiviert PIN2 der Erweiterungsplatine, wenn er größer als 35A ist. In diesem spezifischen Beispiel wird er verwendet, um das hintere Bremslicht einzuschalten, wenn die Rekuperation ausreicht, um den Twizy zu verlangsamen.\
Der zweite Alarmauslöser prüft den Batterie-SOC und zeigt auf dem Display ein einfaches Pop-up an, das benachrichtigt, dass der Batteriepegel niedriger als 30% ist. Durch Aktivieren des Feldes *„Change page"* habe ich eine weitere Option hinzugefügt, die ToM+ anweist, eine MQTT-Nachricht zu senden, wenn dieser Alarm auslöst.\
Der dritte Alarmauslöser prüft den Batterie-SOC und führt nach Abschluss des Ladevorgangs (z. B. gleich 97%) dasselbe wie zuvor aus, führt jedoch einen zusätzlichen Befehl aus. Der Befehl *cmd/charge/Power 0* deaktiviert einen Tasmota WLAN-Schalter, der den Twizy-Stecker mit der Wandsteckdose verbindet.

Die Funktion der Spalte **„COMMAND"** ist also sehr nützlich und ermöglicht es Ihnen, Ihr ToM+ in Ihr IoT-Haus einzubinden. Siehe Anhang [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} für detaillierte Konfigurationen.\
Wenn Sie einen bestimmten Alarm entfernen möchten, müssen Sie nur die Schaltfläche **„Remove"** in der letzten Spalte drücken.\

<figure data-latex-placement="H">
<img src="figures/alarm_page2.png" style="width:100.0%" />
<figcaption>Alarmseite — Tabelle zum Hinzufügen neuer Alarme.</figcaption>
</figure>

In der zweiten Tabelle können Sie der eben besprochenen Liste einen neuen Alarm hinzufügen. Zunächst müssen Sie das **ITEM** aus allen in Abschnitt [3.1](#sec:icon_list){reference-type="ref" reference="sec:icon_list"} aufgeführten verfügbaren Daten auswählen. In diesem Auswahlfeld sind die Elemente wie in der eben zitierten Liste organisiert. Wählen Sie dann die **CONDITION**, d. h. den Operator des Vergleichs, zwischen *„lower"*, *„greater"* oder *„equal"*. Als Nächstes ist der Referenz-**VALUE** an der Reihe, eine vorzeichenbehaftete Ganzzahl, der rechte Begriff des Vergleichs.\
Nehmen wir uns etwas Zeit, um alle möglichen **ACTION**s zu erklären.\

- *pop-up*: Ein gelbes Pop-up, das den Elementwert mitteilt, erscheint in der Mitte des Bildschirms. Um es auszublenden, drücken Sie es einmal. Ein Pop-up-Beispiel sehen Sie im ersten Bild unten.

- *pop-up 10 sec*: Ein gelbes Pop-up, das den Elementwert mitteilt, bleibt zehn Sekunden lang auf dem Bildschirm.

- *silent*: Es finden keine sichtbaren Aktionen statt: Wird häufig verwendet, um nur MQTT-Nachrichten zu senden.

- *icon x fix*: Symbol x (*wobei x 2, 3, 4 oder 5 sein kann*) leuchtet auf. Siehe Abbildung [4.4](#fig:alarm_icons2){reference-type="ref" reference="fig:alarm_icons2"} für Alarmsymbole.

- *icon x blink*: Symbol x (*wobei x 2, 3, 4 oder 5 sein kann*) beginnt zu blinken.

- *pin1 active*: PIN1 der Erweiterungsplatine wird aktiviert (LOW oder HIGH je nach Pegel, der in den Erweiterungseinstellungen in Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"} gewählt wurde).

- *pin2 active*: PIN2 der Erweiterungsplatine wird aktiviert. In diesem Beispiel wurde PIN2 als INPUT-Modus eingestellt, ist also ausgegraut, da er keine OUTPUT-Aktion darstellen kann.

 \

<figure id="fig:alarm_icons2" data-latex-placement="ht">
<figure>
<img src="figures/pop-up.PNG" />
<figcaption>Pop-up: Batterietemp &gt; 89°C.</figcaption>
</figure>
<figure id="fig:alarm_icons2">
<img src="figures/alarm_icons.png" />
<figcaption>Alarmsymbole (2, 3, 4 und 5).</figcaption>
</figure>
<figcaption>Alarmsymbole (2, 3, 4 und 5).</figcaption>
</figure>

Das nächste Feld ist das binäre **SEND MQTT**-Flag: Wenn aktiviert, veröffentlicht ToM+ eine MQTT-Nachricht auf dem konfigurierten MQTT-Out-Topic (z. B. TOMout, siehe Abschnitt [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}), wenn der Alarm als zusätzliche Benachrichtigung auslöst. Zu guter Letzt gibt es das Textfeld **AUX CMD**, das einen zusätzlichen Befehl enthält, der über MQTT an andere IoT-Geräte gesendet werden kann. Siehe Anhang [7](#apx:tasmota){reference-type="ref" reference="apx:tasmota"} für detaillierte Konfigurationen eines Tasmota-Schalters als Beispiel.\
Schließlich können Sie Ihren Alarm hinzufügen, indem Sie die Schaltfläche **„Add to list"** drücken. Die Seite wird automatisch neu geladen und der Alarmauslöser wird an die Liste in der ersten Tabelle angehängt.

Drücken Sie am Ende der Seite die grüne Taste **„HOME"**, um zur Startseite zurückzukehren.

### Alarmsystem-Protokollseite {#sec:web_alarms_log}

Diese Seite speichert die letzten 21 Alarmauslösungen und erfüllt dieselbe Funktion wie die Protokollseite von ToM, wie in Abschnitt [3.5](#sec:alarm_log){reference-type="ref" reference="sec:alarm_log"} gezeigt. Sie können unerwünschte Datensätze auch anzeigen und entfernen, indem Sie die Schaltfläche **„Remove"** neben dem Datensatz drücken, den Sie dauerhaft löschen möchten (auch auf dem ToM+-Display).\

<figure data-latex-placement="H">
<img src="figures/alarm_log1.png" style="width:60.0%" />
<figcaption>Tabelle der Alarmlogbuch-Seite.</figcaption>
</figure>

Offensichtlich enthält die Tabelle das **ITEM** und den **VALUE**, die den Alarm ausgelöst haben. Es gibt jedoch zusätzliche Felder mit Datum und Uhrzeit, wann die Auslösung stattfand. Drücken Sie dann wie gewohnt am Ende der Seite die grüne Schaltfläche **„HOME"**, um zur Startseite zurückzukehren.

### OTA-Update & Einstellungsseite {#sec:web_ota_update}

Auf dieser Seite können Sie die **Firmware spontan über die Weboberfläche aktualisieren**, ohne sich wie in älteren Versionen mit dem Flash-Tool herumschlagen zu müssen. Diese neue Funktion spart Zeit und ist viel benutzerfreundlicher. Stellen Sie daher sicher, dass Sie immer die neueste Version der Firmware installiert haben, um Zugriff auf die neuesten Funktionen und Verbesserungen zu haben!

#### OTA-Update

Die erste Tabelle gibt Ihnen einige Informationen über die Blackbox-Firmware: Besprechen wir diese Werte. Die **ESP fw** ist wahrscheinlich das wichtigste Element im Raster, da sie Ihnen die Version mitteilt, die derzeit auf dem ESP-Motherboard installiert und geladen ist.

Ein weiteres nützliches Feld ist die **S/N**, die für Seriennummer steht, die Sie auch auf dem ToM+ finden, wie in Abbildung [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"} gesehen. Die nächste Zeile ist etwas technischer und steht in direktem Zusammenhang mit dem OTA-Update-Mechanismus (Over-The-Air). **Current ptn** und **Next ptn** beziehen sich auf die Partitionsadressen, an denen die Firmware derzeit gespeichert ist und wo sie während des laufenden Updates gespeichert wird.\
Manchmal werden Firmware-Patches, wie Fehlerbehebungen oder kleinere Dinge, veröffentlicht, ohne die Versionsnummer zu ändern (z. B. 2.4). In diesen Fällen kann es nützlich sein zu wissen, welche spezifische Binärdatei installiert ist; daher enthalten die nächsten beiden Felder deren vollständigen Namen. Wie Sie sehen können, gibt es zwei Haupt-Firmware-Partitionen, **Ota0** und **Ota1**, sodass Sie zwei verschiedene Versionen installiert haben und bei Bedarf zwischen ihnen wechseln können. Hier lautet der vollständige Name für beide *ESP32_Fw24_70_4error12*.

Das letzte Feld ist der vollständige Name der Firmware der **Special partition**, bei der es sich um einen zusätzlichen Speicher handelt, der zum Halten von Software Dritter verwendet wird (z. B. die Tuning-Software Twizy-cfg). Weitere Informationen zum Tuning Ihres Twizy mit Twizy-cfg auf ToM+ finden Sie in Anhang [6](#apx:tuning){reference-type="ref" reference="apx:tuning"}.

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Update- und Info-Tabelle.</figcaption>
</figure>

Der zweite Teil dieser Tabelle ermöglicht es Ihnen, die Firmware zu aktualisieren oder Software von Drittanbietern zu laden. Laden Sie zunächst die Binärdatei (mit der Endung .bin) herunter, die Sie auf dem ToM+ installieren möchten. Drücken Sie dann die Schaltfläche **„Browse..."** und navigieren Sie durch Ihre Geräteordner, bis Sie die gewünschte Datei finden.

Wenn es sich um ein *Standard-ToM+-Update* handelt, drücken Sie die Schaltfläche **„UPDATE"**. Um den Update-Status zu überprüfen, erscheint am unteren Rand der Tabelle ein orangener Fortschrittsbalken mit Prozentangabe. Wenn er 100% erreicht, startet ToM+ schließlich neu, um die Änderungen zu übernehmen.

Wenn es sich um *Software von Drittanbietern* handelt, stellen Sie sicher, dass Sie die Option *„Update to special partition"* aktivieren und erst danach die Schaltfläche **„UPDATE"** drücken. Sobald das Update abgeschlossen ist, startet ToM+ neu und lädt die Firmware der Spezialpartition.\
In der Tabelle **„BOOT OPTIONS"** können Sie hingegen, sobald Sie die gewünschten Firmwares geladen haben, bei Bedarf zwischen ihnen wechseln. Nehmen wir an, ich nutze die ToM+ 2.4 Firmware und möchte etwas Tuning mit der Drittanbieter-Software Twizy-cfg durchführen; ich habe bereits beide in die korrekten Partitionen geladen. Um dies zu erreichen, drücken Sie die Schaltfläche *„Reboot from special partition"* und warten Sie, bis ToM+ neu startet; folgen Sie dann Anhang [6](#apx:tuning){reference-type="ref" reference="apx:tuning"} für weitere Informationen.\
Die Schaltflächen *„Reboot from Ota0 partition"* und *„Reboot from Ota1 partition"* werden verwendet, um zwischen den ToM+-Firmware-Versionen zu wechseln. Nehmen wir an, ich nutze die ToM+ 2.4 Firmware, möchte aber aus irgendeinem Grund zur Version 2.3 zurückkehren, die ich zuvor hatte. Drücken Sie dazu die entsprechende Schaltfläche, um entweder von Ota1 oder Ota0 neu zu starten. ToM+ startet sofort neu und die Verbindung zur Weboberfläche wird getrennt.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Tabelle für Boot-Optionen.</figcaption>
</figure>

In der nächsten Tabelle haben wir die Tabelle **„LCD FIRMWARE UPDATE"**, die es ermöglicht, OTA-Updates auch für das LCD-Display durchzuführen. Das bedeutet kein Hantieren mehr mit der MicroSD-Karte und dem kleinen Loch am Display.\
**WARNUNG:** Wie in der Tabelle beschrieben, dürfen Sie diese Webseite während des Updates **NICHT** schließen: Es wird empfohlen, Ihren Bildschirmschoner zu deaktivieren, um ein Fehlschlagen des Updates zu vermeiden. Der Vorgang kann je nach Firmware-Version einige Minuten dauern, bis zu 10 Minuten.\
Dies ist ähnlich wie das Blackbox-OTA-Update. Laden Sie also zuerst die Datei (mit der Endung .tft) herunter, die Sie auf dem ToM+ installieren möchten. Drücken Sie dann die Schaltfläche **„Browse..."** und navigieren Sie durch Ihre Geräteordner, bis Sie die gewünschte Datei finden.

Wenn Sie das *Hauptdisplay aktualisieren*, drücken Sie die Schaltfläche **„UPDATE LCD"**. Um den Update-Status zu überprüfen, zeigt der blaue Fortschrittsbalken unter dem Haftungsausschluss-Feld die auf das LCD kopierten Blöcke an. Wenn er fertig ist, startet das Display neu (nicht die Blackbox).

Wenn Sie das *Zusatzdisplay (Twin Display) aktualisieren*, stellen Sie sicher, dass Sie die Option *„Update AUX LCD"* aktivieren und erst danach die Schaltfläche **„UPDATE LCD"** drücken. Sobald das Update abgeschlossen ist, startet das LCD-Display neu und lädt die gewünschte Firmware.

<figure data-latex-placement="H">
<img src="figures/ota_lcd.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Tabelle für LCD-Firmware-Update.</figcaption>
</figure>

#### Einstellungen und HW-Upgrade

Im nächsten Abschnitt der Webseite können wir Einstellungen verwalten, was WLAN- und MQTT-Konfigurationen, Symbolanordnungen der ToM+-Seiten und mehr umfasst. Es ist daher immer ratsam, **vor dem Update ein Backup** zu erstellen, um die erneute Eingabe von Passwörtern zu vermeiden, falls ein Update fehlschlägt. Drücken Sie dazu die Schaltfläche **„BACKUP"**, und eine Datei namens *prefs.ToM* wird auf Ihr Gerät heruntergeladen. Manchmal öffnet sich ein Pop-up, um Sie zu warnen, dass diese Datei eine ungewöhnliche Dateiendung hat; klicken Sie auf die Schaltfläche *Behalten* und laden Sie sie trotzdem herunter.\
Der umgekehrte Vorgang ist ebenso einfach. Drücken Sie die Schaltfläche **„Browse..."** und navigieren Sie durch Ihre Geräteordner, bis Sie die Einstellungsdatei *prefs.ToM* finden. Um die Änderungen zu übernehmen, drücken Sie die Schaltfläche **„RESTORE"**; Sie werden zur Bestätigung auf die Startseite weitergeleitet.

<figure data-latex-placement="H">
<img src="figures/prefs_page.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Tabelle zur Einstellungssicherung.</figcaption>
</figure>

Diese nächste Tabelle ist sehr spezifisch für Benutzer älterer ToM-Versionen, die nun das Passwort erhalten haben, um ihr Gerät auf ToM+ aufzurüsten, ohne die Blackbox auszutauschen. Wenn dies bei Ihnen der Fall ist, geben Sie bitte das Passwort in das Textfeld ein und drücken Sie die Schaltfläche **„UPGRADE"**. Von nun an ist Ihr ToM endlich auf ToM+ aufgerüstet, viel Spaß!

<figure data-latex-placement="H">
<img src="figures/hw_upgrade.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Tabelle zum Hardware-Upgrade.</figcaption>
</figure>

Drücken Sie am Ende der Tabelle die grüne Taste **„HOME"**, um zur Startseite zurückzukehren.

### Erweiterte Info- & Einstellungsseite {#sec:web_advanced_info}

Diese Seite ist für verschiedene erweiterte Einstellungen gedacht, die aus Platzgründen nicht auf den Einstellungsseiten des ToM+-Displays (besprochen in Abschnitt [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}) verfügbar sind.\
Das erste Flag, **„Disable Auto-dimming"**, kann aktiviert werden, wenn Sie nicht möchten, dass das LCD-Display des ToM+ die Helligkeit beim Einschalten des Fernlichts/Abblendlichts anpasst. Andernfalls können Sie die **„Dimming brightness (%)"** in Prozent (bis zu 100%) einstellen und den Faktor der Helligkeitsreduzierung bei Aktivierung der Scheinwerfer selbst festlegen.

<figure data-latex-placement="H">
<img src="figures/adv_sett_page1.png" style="width:100.0%" />
<figcaption>Erweiterte Info-Seite — Tabelle für erweiterte Einstellungen.</figcaption>
</figure>

Als Nächstes haben wir den Unterabschnitt **Warnmeldungen beim Ausschalten**, in dem Sie die Erinnerungen (*Scheinwerfer* und *Handbremse*) und Infos (*Systemfehler* und *Ladebegrenzungen*) auswählen können, die beim Ausschalt-Pop-up des ToM+ angezeigt werden. Es sieht aus wie im Bild unten gezeigt und lässt Sie beispielsweise wissen, wenn Sie vergessen haben, die Handbremse anzuziehen. Die letzten beiden Kontrollkästchen sind für zukünftige Verwendungen reserviert und noch nicht implementiert.

<figure data-latex-placement="H">
<img src="figures/pop-up_finale.png" style="width:50.0%" />
<figcaption>Warnmeldung beim Ausschalten.</figcaption>
</figure>

Dann gibt es die **„Secondary font colour"** mit einer Farbauswahl, mit der die sekundäre Schriftfarbe auf dem ToM+-Display geändert werden kann.

Ein weiteres verfügbares Flag ist **„Invert current value sign"**. Wenn aktiviert, zeigt es bei den Stromverbrauchswerten im Grunde eine vorzeichenbehaftete Ganzzahl anstelle von Absolutwerten an.\
Die kleine Untergruppe darunter ist der **Cheatzy**-Kompatibilität mit ToM+ gewidmet. Sie können Ihren **„Cheating factor"** multipliziert mit 10 einstellen: Beispielsweise wird 2,0 zu 20. Sie können auch auswählen, ob der Cheatzy beim Laden oder beim regenerativen Bremsen aktiviert ist, indem Sie das Flag **„Cheat also Charge/Reku"** verwenden. Diese Einstellungen machen nur Sinn, wenn der Cheatzy angeschlossen und eingeschaltet ist; andernfalls können sie Ihre Stromwerte fehlerhaft verändern.\
Dann gibt es ein weiteres Flag: **„Increase thermal protection threshold"**, mit dem der Überhitzungsschutz-Schwellenwert für ToM+ in wärmeren Jahreszeiten um 15°C erhöht werden kann.

Die nächsten beiden Werte sind zusätzliche Konfigurationen für die von ToM+ berechneten **Rest-KM**, basierend auf einer Abtastung des aktuellen Verbrauchs. Hier können Sie im Feld **„Remaining KM sampling time (min)"** einstellen, wie oft die Abtastung erfolgt (Standard: einmal pro Minute) und wie stark die letzte Stichprobe die Gesamtberechnung beeinflusst (Standard: 10%) im Feld **„Remaining KM sample weight (%)"**.\
Schließlich haben wir das Flag **„Miles to Kilometers"**, das hilft, wenn Ihr BigToM aus einem meilenbasierten Dashboard erstellt wurde, Sie aber km/h als Maßeinheit wünschen. Wenn aktiviert, führt ToM+ diese Konvertierung für Sie durch.

Bitte denken Sie daran, Ihre **Änderungen zu speichern**, indem Sie die Schaltfläche **„SAVE"** am Ende dieser Tabelle drücken. Wenn Sie dies nicht tun, gehen Ihre Änderungen beim Verlassen der Seite verloren.

<figure data-latex-placement="H">
<img src="figures/adv_info.png" style="width:90.0%" />
<figcaption>Erweiterte Info-Seite — Tabelle für erweiterte Informationen.</figcaption>
</figure>

Die Tabelle oben enthält Daten zu Ihrer Batterie, wie gespeicherte Kapazität, **SOH**, **Batterie-Kilometerstand**, insgesamt verbrauchte kWh und zu Ladevorgängen, wie die Anzahl der *gesamten*, *vollständigen* und *teilweisen* Ladevorgänge sowie die **maximal akzeptierte Ladeleistung**.\

<figure data-latex-placement="H">
<img src="figures/item_scroll.png" style="width:100.0%" />
<figcaption>Erweiterte Info-Seite — Element-Scroll-Tabelle.</figcaption>
</figure>

Diese letzte Tabelle ist eine sehr spezielle Funktion, die vor einigen Updates eingeführt wurde und es Ihnen ermöglicht, dynamisch wechselnde Elemente auf Seiten Ihrer Wahl zu haben. Sie kann auf die Seiten *Batterie*, *Motor*, *Gyroskop*, *Fahrt* und *Ladevorgang* angewendet werden, und Sie können über das Feld **„Page"** auswählen, welche davon genutzt werden soll.

Anschließend können Sie auswählen, an welcher Position die Datenelemente Ihrer Wahl gescrollt werden sollen. Verwenden Sie dazu das Feld **„Position"** und wählen Sie aus der Liste die von Ihnen bevorzugte Position unter Bezugnahme auf Abbildung [3.4](#fig:icon_arrangement){reference-type="ref" reference="fig:icon_arrangement"} für das Layout-Arrangement.\
Das Feld **„Freq"** ist die Scrollfrequenz, im Grunde wie lange jedes Datum an dieser Position bleibt, bevor es zum nächsten wechselt. Wie Sie vielleicht bemerken, ist in Klammern angegeben, dass das Feld mit *5 Sekunden* multipliziert wird. Das bedeutet, dass die Eingabe des Werts *1* zu einer Frequenz von *5 Sekunden* führt, der Wert *2* zu einer von *10 Sekunden* und so weiter.

Der wichtigste Teil ist die Auswahl der zu scrollenden Elemente, und Sie können bis zu zehn Datenwerte auswählen. Tragen Sie in den Textbereichen **„Scrolling items"** die Liste der gewünschten Elementnummern ein (z. B. 59 oder 48), eine pro Zeile, bezogen auf die Nummern in Klammern in der Liste von Abschnitt [3.1.2](#sec:item_numbers){reference-type="ref" reference="sec:item_numbers"}.\
Denken Sie immer daran, Ihre Änderungen zu speichern, indem Sie die Schaltfläche **„SAVE"** am Ende dieser Tabelle drücken. Wenn Sie dies nicht tun, gehen Ihre Änderungen beim Verlassen der Seite verloren.

Wenn Sie die Scroll-Funktion für eine bestimmte Seite und Position **deaktivieren** möchten, wählen Sie diese Felder aus und geben Sie dann *0* in das Textfeld **„Freq"** ein. Drücken Sie direkt danach **„SAVE"**, und das Scrollen wird deaktiviert, wobei zu den Standardwerten zurückgekehrt wird.

Drücken Sie die grüne Taste **„HOME"** am Ende der Tabelle, um zur Startseite zurückzukehren.

### Ladeeinstellungen & Log {#sec:web_charging_prefs}

Diese Seite ist in zwei Haupttabellen unterteilt: Die erste dient zur Steuerung des Ladevorgangs, während die zweite eine Liste der letzten 15 Ladevorgänge mit einigen zusätzlichen Daten enthält.

#### Ladeeinstellungen

Beginnend mit den nützlichsten haben wir das Feld **„Charging status"**, das Informationen über den aktuellen Status des Fahrzeugs enthält, einschließlich *220V Netz* und *Ladevorgang* mit ihren EIN- und AUS-Flags.

Direkt darunter befindet sich das Feld **„Charge power limit"**, in dem Sie wählen können, wie viel Leistung Ihr Twizy beim Laden nutzen kann, von $0,4 kW$ bis zu $2,3 kW$ mit 7 Stufen zur Auswahl (wählen Sie *0, um das Leistungslimit zu deaktivieren*).

In der oberen rechten Ecke befindet sich die Schaltfläche **„ABORT CHARGING"**, die den Ladevorgang sofort und geordnet stoppt, genau wie die auf dem ToM+-Display auf der Einstellungsseite, die wir in Abschnitt [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"} besprochen haben.

<figure data-latex-placement="H">
<img src="figures/charging_process.png" style="width:100.0%" />
<figcaption>Ladeeinstellungs-Seite — Tabelle zur Steuerung des Ladevorgangs.</figcaption>
</figure>

Gleich danach befindet sich das Feld **„Stop charge at SOC %"**, das den Lade-Prozentsatz angibt, bei dem ToM+ automatisch das Signal zum Abbrechen des Ladevorgangs sendet. Nur zu Ihrer Information: Das Begrenzen der maximalen Ladereihe (95% oder weniger) verlangsamt den Zerfall des Batterie-SOH.

Weiter zum nächsten Feld haben wir das Feld **„Full charge after"**, das sich eng auf das letzte bezieht, das wir besprochen haben. Im Grunde stoppt dies den Ladevorgang bei dem ausgewählten SOC einmal alle *X* Ladevorgänge nicht (*zum Beispiel 10* wie im Bild). Denken Sie daran, dass eine 100%-Ladung hin und wieder hilfreich ist, um die Spannungen der Batteriezellen neu zu balancieren.

Ein weiteres verwandtes Feld ist das Flag **„Max charge once (next/current)"**, das wie eine Schaltfläche funktioniert und ToM+ anweist, eine vollständige Ladung ohne den gewählten SOC-Stopp durchzuführen. Dies überschreibt das vorherige Feld und wird **nach dem Drücken von „SAVE"** auf den aktuellen Ladevorgang angewendet, wenn dieser bereits läuft, oder auf den nächsten, falls nicht.\
Jetzt gibt es ein Sicherheitsfeld, die **„Charger max temperature"**, in dem Sie einen Schwellenwert (Ganzzahlwert in °C) einstellen können; wird dieser mit einer vom Benutzer definierten Marge-Hysterese überschritten, reduziert ToM+ langsam die zuvor gesehene Leistungsgrenze. Es reduziert diese weiter (bei Bedarf um zwei Stufen), bis die Temperatur wieder normal ist, woraufhin auch die Leistungsgrenze zurückgesetzt wird.

Die genannte Marge ist im entsprechenden Feld **„Temp margin"** anpassbar, in das Sie einen Ganzzahlwert (in °C) eingeben können, der zur maximalen Ladegerättemperatur addiert wird, um den Schwellenwert zu lockern, bevor die Ladeleistung reduziert wird.

Ein weiteres verwandtes Feld ist die **„Abort temperature"**, die den letzten Sicherheitsschwellenwert für die Ladegerättemperatur enthält; wird dieser überschritten, bricht ToM+ den Ladevorgang sofort ab.\
Als Nächstes haben wir drei MQTT-Steuerfelder, die durch ihre fortlaufende Nummer unterschieden werden. Durch Aktivieren eines dieser Flags können Sie den Parameter auf der linken Seite aus der Ferne über das MQTT-Protokoll konfigurieren. Um dies zu erreichen, müssen Sie nach dem Aktivieren des entsprechenden Feldes und dem **Drücken von „SAVE"** lediglich eine MQTT-Nachricht auf dem in Klammern angegebenen Topic (z. B. *001* oder *002*) auf Ihrem Broker veröffentlichen (konfiguriert in Abschnitt [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}).

Wenn Sie die **MQTT control (001)** aktivieren, können Sie den Ladevorgang starten und stoppen, indem Sie entweder *0* oder *1* auf dem MQTT-Topic *001* veröffentlichen. Das Gleiche gilt für **MQTT control (002)** durch Veröffentlichung eines Werts zwischen *0* und *7* auf *002* sowie **MQTT control (003)** auf *003* mit einem Wert zwischen *0* und *100*.\
Zu guter Letzt haben wir das Feld **„Aux Cmd"**, das für Zusatzbefehl steht und sich genauso verhält wie das, das wir bereits auf der Alarmauslöser-Seite in Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"} besprochen haben. Es wird gesendet, wenn der Ladevorgang abgeschlossen ist oder wenn der Ladevorgang beim angegebenen SOC stoppt.\
Nach jeder Änderung drücken Sie die Schaltfläche **„SAVE"**, um *Ihre Änderungen zu speichern*; andernfalls gehen sie beim Verlassen der Seite verloren.

#### Ladehistorie

Die Ladehistorie-Tabelle enthält die letzten fünfzehn Ladevorgänge zusammen mit einigen nützlichen Werten zu deren Bereicherung. Wie Sie sehen können, gibt es Datum und Uhrzeit sowie den **ODO Kilometers**-Wert beim Start des Ladevorgangs. Daneben sehen wir, wie viel Zeit der Ladevorgang in Anspruch genommen hat, die **Average Power** (durchschnittliche Leistung) sowie die **charged kWh** (geladene kWh). Schließlich haben wir *init SOC* und *end SOC*, welche die Start- und Endprozentsätze darstellen.\
Die letzte Spalte enthält einige zusätzliche **Notes** (Hinweise) zum Ladestatus, z. B. wie er gestoppt wurde (entweder Stopp-SOC erreicht oder manuell abgebrochen) oder ob er noch läuft.

Wenn Sie möchten, können Sie auch einige Datensätze manuell löschen, indem Sie die Schaltfläche *X* am Ende des gewünschten Datensatzes drücken. Es ist möglich, alle auf einmal zu löschen, indem Sie die Schaltfläche **„CLEAR HISTORY"** im unteren Teil der Tabelle drücken.

<figure data-latex-placement="H">
<img src="figures/charging_history.png" style="width:95.0%" />
<figcaption>Ladeeinstellungs-Seite — Ladehistorie-Tabelle.</figcaption>
</figure>

Drücken Sie die grüne Taste **„HOME"** unter der letzten Tabelle, um zur Startseite zurückzukehren.

### Uhrzeit- & Datumsseite {#sec:web_time_date}

Mit Ihrem ToM+ können Sie das aktuelle Datum und die Uhrzeit überprüfen, aber wie stellt man sie ein? Diese Seite wurde genau für diesen Zweck erstellt und enthält eine einzelne Tabelle, die im folgenden Bild gezeigt wird.

<figure data-latex-placement="H">
<img src="figures/time_page.png" style="width:100.0%" />
<figcaption>Aktuelle Uhrzeit- &amp; Datumstabelle.</figcaption>
</figure>

Die ersten fünf Felder sind selbsterklärend und intuitiv; passen Sie Datum und Uhrzeit einfach an Ihre Zeitzone an. Das Kontrollkästchen **„DST"**, das für Daylight Saving Time (Sommerzeit) steht, ermöglicht das Aktivieren oder Deaktivieren des 1-Stunden-Versatzes je nach aktueller Jahreszeit.

Wenn Sie Ihre Änderungen bestätigen und auf ToM+ anwenden möchten, drücken Sie einfach die Schaltfläche **„SET"**, und sie werden aktualisiert.\
Als Nächstes haben wir ein sehr nützliches Feld, das Flag **„Synchronize clock with WiFi"**, das nützlich ist, wenn Sie bereits eine WLAN-Verbindung wie in Abschnitt [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"} besprochen konfiguriert haben. Schalten Sie dies einfach ein und überlassen Sie ToM+ die Arbeit.

Direkt darunter befindet sich ein technischerer Wert bezüglich des Datums/der Uhrzeit, der ToM+ Ihre aktuelle Zeitzone (**TZ**) mithilfe einer Zeichenfolge namens **„POSIX"** mitteilt. Dies beinhaltet auch, wann der 1-Stunden-Sommerzeitversatz angewendet wird. In den meisten mitteleuropäischen Ländern lautet die Zeichenfolge wie folgt: *CET-1CEST,M3.5.0/2,M10.5.0/3*; suchen Sie im Zweifelsfall online nach der POSIX-TZ-Zeichenfolge Ihres Landes.\
Denken Sie wie immer daran, Ihre Änderungen durch Drücken der Schaltfläche **„SAVE"** am Ende der Tabelle zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren.

Drücken Sie die grüne Taste **„HOME"** unter der Tabelle, um zur Startseite zurückzukehren.

### BigToM / ToM+ Einstellungsseite {#sec:web_btom_tom_sets}

Auf dieser Seite können Sie einige Parameter Ihres BigToM oder ToM+ anpassen, da diese Seite hauptsächlich Konfigurationen für die **Dashboard-Seite** enthält, die nur auf diesen beiden Geräten verfügbar ist.

<figure data-latex-placement="H">
<img src="figures/btom_page.png" style="width:100.0%" />
<figcaption>BigToM \ToM+ Einstellungstabelle.</figcaption>
</figure>

Beim Ersetzen Ihres Dashboards durch ein BigToM-Dashboard müssen Sie möglicherweise einige Kilometer zum ODO des neuen Dashboards hinzufügen oder davon abziehen, um Ihren ursprünglichen Stand zu erhalten. Das liegt daran, dass sie auf dem Dashboard-Motherboard gespeichert sind. Der erste Parameter ist daher das Feld **„ODO kms offset"**, das zur Korrektur dieser Kilometerdifferenz verwendet wird.

Wie Sie vielleicht wissen, werden Dashboard-Geschwindigkeitsanzeigen aus Sicherheitsgründen absichtlich um $3 km/h$ erhöht. Wenn Sie Ihre reale Geschwindigkeit sehen möchten, aktivieren Sie einfach das Flag **„Real speed (not ODO)"** in der zweiten Zeile der Tabelle.\
Schauen wir uns nun das Flag **„Lock touch while driving"** an. Wenn aktiviert, wird der Touchscreen während der Fahrt (d. h. Geschwindigkeit $>0$) aus Sicherheitsgründen deaktiviert.

Als Nächstes haben wir das Flag **Skip welcome animation**, das aktiviert werden kann, wenn Sie es leid sind, die Begrüßungsanimation beim Wechsel vom Dashboard zu einer anderen Seite zu sehen.\
Dann gibt es einen Bereich, der dem Leistungsbalken gewidmet ist, der in Abbildung [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"} oben im Dashboard-Layout gezeigt wird. Hier können Sie über das Auswahlfeld **„Power bar item"** wählen, welcher Wert angezeigt und zum Füllen des Leistungsbalkens verwendet werden soll. Es stehen drei verfügbare Daten zur Auswahl: *Engine Torque* (Motordrehmoment), *Battery Ampere* (Batteriestrom) oder *Battery kW* (Batterieleistung).

Die beiden Felder **„Up/Down section scale %"** darunter werden verwendet, um den Bereich des Leistungsbalkens anzupassen, und repräsentieren den Prozentsatz des Maximal-/Minimalwerts des ausgewählten Datenelements. Im Beispielbild habe ich für den maximalen Bereich *30%* eingetragen.\
Im nächsten Abschnitt können wir eine weitere nützliche Funktion aktivieren, die ebenfalls in Abbildung [3.1](#fig:dashboard_layout){reference-type="ref" reference="fig:dashboard_layout"} direkt unter der Geschwindigkeitsanzeige gezeigt wird. Dies wird durch Aktivieren des Flags **„Enable alert speed bar"** erreicht, das über drei anpassbare Schwellenwerte verfügt, die jeweils einer Farbe von *Grün* über *Gelb* bis *Rot* entsprechen.

Die folgenden drei Felder, **„Speed alert low/medium/high limit"**, sind mit der jeweiligen Schwellenwertgeschwindigkeit in $km/h$ auszufüllen, um die Geschwindigkeitsleiste mit der entsprechenden Farbe aufleuchten zu lassen. Im Beispiel wird die Leiste beim Überschreiten von $50 km/h$ gelb und beim Überschreiten von $70 km/h$ rot. Wie Sie vielleicht bemerken, wollte ich nicht, dass die grüne Leiste angezeigt wird, daher habe ich den Schwellenwert *low* auf denselben Wert wie den Schwellenwert *medium* gesetzt.\
Vorletztes haben wir das standardmäßig aktivierte Flag **„3D layout for charging page"**, das 3D-Details anstelle der Standard-ToM-Ladeseite anzeigt.

Und schließlich gibt es die zuletzt hinzugefügte Funktion namens **Twin ToM**, die für die ursprünglichen ToM-Besitzer entwickelt wurde, bevor ToM+ herauskam. Damit können Sie das kleinere Display zusammen mit der neuen Ansteckversion verwenden, um zwei Seiten gleichzeitig zu überwachen. Damit dies funktioniert, müssen Sie das Flag in der letzten Zeile aktivieren: **„Enable auxiliary display"**.

Anschließend können Sie über das Auswahlfeld **„Start page"** eine bestimmte Seite auswählen, die beim Einschalten auf dem Zusatzdisplay angezeigt werden soll, oder einfach *Last shown* (Zuletzt angezeigt) wählen.\
Denken Sie wie immer daran, Ihre Änderungen durch Drücken der Schaltfläche **„SAVE"** am Ende der Tabelle zu speichern; andernfalls gehen sie beim Verlassen der Seite verloren.

Drücken Sie die grüne Taste **„HOME"** unter der Tabelle, um zur Startseite zurückzukehren.

### Diagnose-Seite {#sec:web_diagnostic}

Diese Seite besteht aus nur einer Tabelle und ermöglicht es Ihnen, weitere Informationen zu den letzten 10 Fehlern anzuzeigen, die in Ihrem Twizy aufgetreten sind, ähnlich wie auf der in Abschnitt [3.8](#sec:error_page){reference-type="ref" reference="sec:error_page"} besprochenen ToM+-Displayseite.

Die angezeigten Werte sind die **„DTC Number"** und, falls verfügbar, die **„DF Number"**, bei denen es sich um eindeutige Identifikatoren für Twizy-Fehler handelt, sodass Sie online danach suchen können. Als Nächstes haben wir den Fehler-**„Status"**, wie z. B. *SAVED*, wenn er bereits aufgetreten ist, oder *PRESENT*, wenn er gerade erst aufgetreten ist.

Informationen zur *Aktivierung von DF-Nummern* finden Sie in Abschnitt [4.1.2](#sec:add_wifi_profile){reference-type="ref" reference="sec:add_wifi_profile"}.

<figure data-latex-placement="H">
<img src="figures/error_page.png" style="width:100.0%" />
<figcaption>Diagnose-Seite — Fehlerlisten-Tabelle.</figcaption>
</figure>

Zusammen mit diesen Werten sind die nächsten vier Werte die Referenzen für **„ODO"**, **„SOC"**, **„speed"** (Geschwindigkeit) und **„12V Battery voltage"** (12V-Batteriespannung) zum Zeitpunkt des Auftretens des entsprechenden Fehlers.

Für jeden Fehlerdatensatz gibt es, falls verfügbar, ein Feld für die Fehler-**„Description"** (Beschreibung).\
Wenn Sie Twizy-Fehler löschen möchten, selbst fatale, können Sie die unten stehende Schaltfläche **„DELETE ERRORS"** drücken, die alle Fehler auf einmal löscht.

Drücken Sie die grüne Taste **„HOME"** unter der Tabelle, um zur Startseite zurückzukehren.

# Wie du deine ToM+-Firmware aktualisierst {#sec:update_procedure}

## Voraussetzungen vor dem Update

ToM+ entwickelt sich ständig weiter, da ich fast täglich Vorschläge erhalte, um bestimmte Funktionen zu verbessern oder sogar neue, coole Features hinzuzufügen. Ich versuche, alle Ratschläge der Besitzer zu berücksichtigen, und diese Tipps und Ideen führen zu Firmware-Updates. Wenn du beim Fahren Fehler oder ungewöhnliches Verhalten bemerkst, melde diese bitte an mich, damit sie in Firmware-Patches behoben werden können. Wie ich eingangs erwähnt habe, wird ToM+ kontinuierlich verbessert -- bleib also auf dem Laufenden...

### Warum sollte ich aktualisieren?

Nun, ein neues Update bedeutet neue Funktionen und Fehlerbehebungen. Warum solltest du also die alte Firmware-Version behalten, wenn du ganz einfach die neueste stabile Version installieren kannst? Es gibt also keinen Grund, dein ToM+ veraltet zu lassen, da das Software-Upgrade **für immer kostenlos** ist und dir beim Ausprobieren neuer Funktionen viel Freude und Spaß bringt. Letztendlich rate ich dir persönlich dazu, dein ToM+ auf dem neuesten Stand und sicherer zu halten.\
Alle älteren Firmware-Versionen sind weiterhin im Twizy-Forum im ToM-Bereich (<https://www.twizy-forum.de/twiz-o-meter>) unter den Themen *„\[Twiz o'meter\] Update auf Firmware x.x"* verfügbar. Tatsächlich erlaubt ToM+ bei Bedarf auch Downgrades.

### Was brauche ich für das Update?

In den folgenden Abschnitten wird eine alternative Methode zum Aktualisieren beschrieben, die im Vergleich zur bereits in Abschnitt [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"} besprochenen OTA-Methode deutlich zeitaufwendiger ist. Ich persönlich **empfehle die OTA-Methode**, da sie sicherer und einfacher durchzuführen ist, wenn man sich nicht besonders gut mit IT und Embedded Systems auskennt.\
Wenn du dennoch davon überzeugt bist, die ToM+-Firmware mit der zweiten Methode zu aktualisieren, benötigst du ein paar Dinge, um das Update erfolgreich abzuschließen. Allererst benötigst du einen Computer; sowohl Desktop-PCs als auch Laptops sind für diese Aufgabe bestens geeignet.

Später werden wir sehen, wie du ToM+ mit dem Computer verbindest, um die neuen Update-Dateien darauf zu übertragen. Das zweite, was du besorgen musst, ist ein Micro-USB-Kabel -- dasselbe, das gewöhnlich für aufladbare Geräte und ältere Smartphones verwendet wird. Zudem benötigst du eine microSD-Karte mit einer Speicherkapazität zwischen 8 und 32 GB. Beispiele sind auf den Fotos unten zu sehen. Und natürlich benötigst du dein ToM+!

<figure data-latex-placement="H">
<img src="figures/cables_sd_update.png" style="width:80.0%" />
<figcaption>Micro-USB-Kabel und Beispiel einer microSD-Karte.</figcaption>
</figure>

### Wie sehen die Update-Dateien aus? {#sec:update_files}

Bevor du die Firmware aktualisierst, musst du natürlich die ZIP-Datei der gewünschten Version aus dem Twizy-Forum (wieder unter <https://www.twizy-forum.de/twiz-o-meter>) herunterladen. Wahrscheinlich musst du dich im Forum registrieren, um Firmware-Dateien und Bilder zu sehen und herunterzuladen. Es ist eine wirklich tolle und aktive Community, daher empfehle ich ohnehin, Mitglied zu werden. Nach dem Entpacken der Dateien in den Ordner solltest du Folgendes erhalten:

<figure data-latex-placement="H">
<img src="figures/firmware_release_folder.png" style="width:100.0%" />
<figcaption>Dateiliste des Firmware-Release-Ordners.</figcaption>
</figure>

Zuerst bemerken wir eine Textdatei namens *changeLog23.txt*, mit der die hinzugefügten Funktionen und behobenen Fehler der neuesten Firmware-Version nachverfolgt werden. Lies sie durch, wenn du neugierig bist, was es Neues gibt, oder wenn du zusätzliche Hilfe beim Update-Vorgang benötigst.\
Als Nächstes gibt es zwei Ordner, die das **LCD-Display-Firmware**-Update im *.tft*-Format enthalten. **Wähle die Version**, die für dein Gerät gemacht ist: den ersten Ordner, wenn du ein ToM+ oder ein BigToM hast (was ein größeres Display bedeutet), oder den anderen, wenn du ein traditionelles ToM hast oder das Twin ToM (kleinerer Bildschirm) aktualisieren möchtest. Dies ist ein entscheidender Schritt, da neue Icons und Grafiken sonst nicht zu deiner Displaygröße passen.\
Die letzte Datei ist die Binärdatei *ESP32Fw23.bin* für das **Blackbox-Update**. Stelle sicher, dass du alle diese Dateien hast, da du sie in den nächsten Schritten benötigst.

### Was sollte ich vor dem Update wissen?

Bereiten wir nun unser ToM+ auf das Update vor, indem wir den **Schalter an der Blackbox auf OFF stellen**. Stelle sicher, dass er ausgeschaltet ist (*d. h. Symbol 0 auf dem Schalter*), da du andernfalls schwerwiegende Probleme am ToM+ verursachen wirst.

Wenn dein Twizy also noch mit eingestecktem Schlüssel eingeschaltet ist, schalte ihn einfach komplett aus und ziehe den Zündschlüssel ab. Nach diesen einfachen Schritten bist du bereit für den Update-Vorgang. Denke jedoch daran, den in der Anleitung beschriebenen Schritten strikt zu folgen. Gehe nicht nach Gefühl vor, da du sonst riskierst, dein Gerät dauerhaft zu unbrauchbar zu machen.\
Der Aktualisierungsvorgang ist recht einfach, und du musst sowohl die LCD-Firmware als auch die der Blackbox in genau dieser Reihenfolge aktualisieren. Wie das geht, sehen wir im nächsten Abschnitt.

## Aktualisieren der LCD-Firmware

Das LCD-Display ist eines der wesentlichen Bauteile von ToM+, wie in den ersten beiden Kapiteln besprochen wurde, und muss aus diesem Grund ebenfalls aktualisiert werden. Neue Firmware bedeutet neue Icons und andere Layouts. Um die neuen Daten aufzuspielen, ist es unerlässlich, eine kleine **microSD-Karte** zu verwenden. Der SD-Kartensteckplatz des ToM+ befindet sich unter dem Display. Daher musst du es möglicherweise vorübergehend aus dem Handschuhfach nehmen, um besser daran arbeiten zu können, oder es einfach nach hinten kippen, um die Öffnung zu sehen.

### Vorbereiten der microSD-Karte

Leider funktionieren nicht alle microSD-Karten mit dem Display, insbesondere neuere, die für Kameras entwickelt wurden. Bisher habe ich jedoch Class 10 HC-Karten von 8 bis 32 GB getestet, und diese scheinen gut zu funktionieren. Du kannst es aber gerne mit deiner eigenen Speicherkarte versuchen und prüfen, ob sie funktioniert.\
Nachdem wir eine microSD-Karte ausgewählt haben, die eine Speicherkapazität **zwischen 8 und 32 GB** besitzen muss, müssen wir die LCD-Firmware darauf kopieren. Bevor wir die Datei darauf kopieren, müssen wir sicherstellen, dass sich keine anderen Dateien darauf befinden, da das Upgrade sonst nicht funktioniert.

Verschiebe daher alle Dateien auf deinen Computer und formatiere die microSD-Karte im **FAT32-Format**, wie ich es im Screenshot hier getan habe. Klicke dazu mit der rechten Maustaste auf das Kartensymbol in deinem Datei-Explorer und wähle die Option **„Formatieren..."** aus dem Kontextmenü.

<figure data-latex-placement="H">
<img src="figures/forma_sd_steps.png" style="width:70.0%" />
<figcaption>Schritte zum Formatieren der microSD-Karte in FAT32.</figcaption>
</figure>

Wie im Bild gezeigt, wähle das Dateisystem **FAT32**, aktiviere die Option **„Schnellformatierung"** und drücke die Schaltfläche **„Starten"**, um den Vorgang zu beginnen. Warte, bis der Vorgang abgeschlossen ist, und kopiere dann die *.tft*-Datei aus dem ZIP-Ordner des Firmware-Releases, das du installieren möchtest, auf die Karte.

### Einsetzen der microSD-Karte

Jetzt sind wir bereit, die microSD-Karte in den Steckplatz des LCD-Displays einzusetzen. Es kann hilfreich sein, eine Spitzzange zu verwenden, um die microSD-Karte vorsichtig einzuführen. Dies stellt sicher, dass du den internen SD-Kartensteckplatz genau triffst.\
**WICHTIG!** Die microSD-Karte passt nur in einer Richtung in den Steckplatz: Die Kontaktseite muss zur Bildschirmoberfläche zeigen, wie im Bild dargestellt. Wenn sie nicht passt, wende keine Gewalt an! Versuche, sie umzudrehen.

Nachdem die microSD-Karte in den internen Steckplatz eingeführt wurde, drücke sie langsam in das Gehäuse, bis du ein „Klick"-Geräusch hörst. Das bedeutet, dass du die Zange sicher entfernen kannst, ohne dass die Karte im Gehäuse verloren geht.

<figure data-latex-placement="H">
<img src="figures/sd_insert.jpg" style="width:60.0%" />
<figcaption>microSD-Karte in die Öffnung des Displays einsetzen.</figcaption>
</figure>

### Der Ablauf des Updates

Sobald die microSD-Karte eingesetzt ist, können wir mit dem Update-Ablauf fortfahren. Gehen wir nun zurück zum Twizy und schließen das Display wieder an die Blackbox an. Schalte dann das Display über den Schalter an der Blackbox ein (*d. h. Symbol 1 auf dem Schalter*) und schalte erst danach deinen Twizy mit dem Zündschlüssel ein.

Warte, bis das LCD-Display den Aktualisierungsvorgang startet und der Fortschritt in Prozent angezeigt wird, wie in der Abbildung unten dargestellt (sowohl für das ToM+- als auch für das ToM-Display). Der Kopiervorgang von der microSD-Karte dauert in der Regel etwa eineinhalb Minuten.

<figure data-latex-placement="ht">
<figure>
<img src="figures/update_screen_lcd.jpg" />
<figcaption>ToM+-Display-Update.</figcaption>
</figure>
<figure>
<img src="figures/copy_sd_card.png" />
<figcaption>ToM-Display-Update.</figcaption>
</figure>
<figcaption>ToM-Display-Update.</figcaption>
</figure>

Sobald die Aktualisierung der LCD-Firmware erfolgreich abgeschlossen ist, siehst du diesen Bildschirm mit der Meldung **„Update Succeeded!"**. Nach dem Update das Gerät **NICHT** mit eingesteckter microSD-Karte einschalten! Jetzt können wir das Auto ausschalten und ToM+ über den Schalter an der Blackbox wieder auf OFF schalten.

Entferne dann die microSD-Karte, während das gesamte System ausgeschaltet ist, womit das LCD-Update abgeschlossen ist. **WICHTIG!** Wenn du die Karte entfernst, während ToM+ eingeschaltet ist, wirst du das Gerät dauerhaft unbrauchbar machen! Fahren wir danach, ohne den Zustand des Gesamtsystems zu verändern, mit dem Blackbox-Update fort, wie im nächsten Abschnitt beschrieben.

## Aktualisieren der Blackbox-Firmware (Windows)

Die Blackbox ist die zweite wesentliche Komponente von ToM+ und bildet das Gehirn des gesamten Systems. Wenn wir nur das Display aktualisieren, weiß die Blackbox nicht, wofür die neuen Icons gedacht sind, was zu Kommunikationsfehlern führt.

Daher ist es entscheidend, die neue Firmware auch auf der Hauptplatine von ToM+ zu installieren. Dazu benötigen wir die microSD-Karte nicht mehr, sondern verwenden das zuvor vorbereitete Micro-USB-Kabel und den Computer. Wir werden die Firmware direkt auf das ESP32-Board flashen, um die neue Software zu installieren.

### Vorbereiten des Computers

Bevor wir das Kabel an den Computer anschließen, müssen wir einige Programme installieren, damit alles ordnungsgemäß funktioniert. Das **ESP32-Board** benötigt Treiber, um vom Betriebssystem erkannt zu werden. Wir laden diese direkt von der offiziellen Website herunter.

Auf der Download-Seite der [Silicon Labs-Website](https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads) müssen wir unsere Betriebssystemversion auswählen, wie im Screenshot unten zu sehen ist.

<figure data-latex-placement="H">
<img src="figures/driver_download.png" style="width:100.0%" />
<figcaption>Treiber-Downloadseite bei Silicon Labs.</figcaption>
</figure>

Da dieser Abschnitt der Anleitung speziell für Windows-Betriebssysteme gilt, laden wir das Paket *„CP210x Windows Drivers"* herunter, indem wir auf den im Bild oben gelb markierten Link klicken.

Die heruntergeladene Datei ist ein ZIP-Ordner, der gewöhnlich *„CP210xWindowsDrivers.zip"* heißt und in dem sich einige Ordner und Dateien befinden. Im Screenshot unten sind alle üblicherweise im ZIP-Ordner enthaltenen Dateien aufgelistet.

<figure data-latex-placement="H">
<img src="figures/driver_folder.png" style="width:70.0%" />
<figcaption>Inhalt des Treiber-ZIP-Ordners.</figcaption>
</figure>

Entpacke alle Dateien in einen temporären Ordner auf deinem Desktop. Nun ist es wichtig, die richtige *„.exe"*-Datei für die Installation der Treiber auszuführen. Wenn dein Betriebssystem 64-Bit ist (bei den meisten Computern), führst du die Datei *CP210xVCPInstallerx64.exe* aus, andernfalls ist die zweite *„.exe"*-Datei die passende, wie im Bild gezeigt.

Stelle sicher, dass du die ausführbare Datei mit Administratorrechten startest, indem du mit der rechten Maustaste darauf klickst und die Option **„Als Administrator ausführen"** wählst. Falls du dazu aufgefordert wirst, erlaube dem Programm, Administratoraktionen auf deinem Computer auszuführen, da der Treiber-Installationsprozess sonst nicht startet.

<figure data-latex-placement="ht">
<figure>
<img src="figures/wizard_step1.png" />
<figcaption>Erster Schritt: „Weiter“ drücken.</figcaption>
</figure>
<figure>
<img src="figures/wizard_step2.png" />
<figcaption>Zweiter Schritt: „Akzeptieren“ und „Weiter“.</figcaption>
</figure>
<figcaption>Zweiter Schritt: „Akzeptieren“ und „Weiter“.</figcaption>
</figure>

Sobald das Installationsprogramm startet, siehst du ein Fenster wie das auf der linken Seite. Dies ist ein Assistent zur Installation der Treiber, die erforderlich sind, damit dein Computer die Blackbox erkennt. Drücke nun die Schaltfläche **„Weiter"**, wie hier gezeigt, um den Vorgang zu starten.\
Das nächste Fenster, das du voraussichtlich sehen wirst, ist das auf der rechten Seite. Hier musst du die Lizenz akzeptieren, indem du die erste Option **„Lizenz akzeptieren"** auswählst. Anschließend kannst du auf die Schaltfläche **„Weiter"** drücken und das Kopieren der Treiber in den richtigen Systemordner starten: Warte, bis der Kopiervorgang abgeschlossen ist.

Wenn das Kopieren beendet ist, ist die Installation der CP210X-Treiber abgeschlossen und du kannst die Blackbox sicher an deinen Computer anschließen. Drücke nun die Schaltfläche **„Fertigstellen"**, um das Fenster zu schließen.\
Stelle vor allen weiteren Schritten sicher, dass der Schalter an der ToM+-Blackbox auf OFF steht (*d. h. Symbol 0 auf dem Schalter*). Der Twizy muss ebenfalls ausgeschaltet sein, denn wenn du versuchst, das Kabel an deinen PC anzuschließen, während ToM+ noch vom Fahrzeug mit Strom versorgt wird, vermischst du die Stromversorgungen (5V und 12V), was ToM+ definitiv beschädigen würde.

<figure id="fig:black_box_labels" data-latex-placement="H">
<img src="figures/black_box.jpg" style="width:60.0%" />
<figcaption>Die Komponenten der Blackbox.</figcaption>
</figure>

Die Blackbox verfügt auf der Rückseite über einen kleinen Micro-USB-Anschluss, wie im Bild oben zu sehen ist. Schließe also die Micro-USB-Seite des Kabels an die Blackbox an. Verbinde danach die USB-Seite des Kabels mit einem freien USB-Anschluss deines Computers.

**WICHTIG!** Beide Seiten des Kabels passen nur in einer Richtung in die entsprechenden Buchsen. Wende daher keine Gewalt an, da du sonst den Anschluss des ToM+ oder deines Computers beschädigen könntest. Versuche, den Stecker umzudrehen, und prüfe, ob es so passt.\
Nun sollte der Computer das ESP32-Board der Blackbox erkennen, sofern du die Treiber ordnungsgemäß installiert hast. Um dies zu überprüfen, suche auf deinem PC nach der App **„Geräte-Manager"** und starte sie.

Nun sollte sich ein Fenster öffnen, das wie in der Abbildung unten aussieht. Suche die Zeile **„Anschlüsse (COM & LPT)"** mit dem Steckersymbol und doppelklicke darauf, um die Liste aller seriellen Geräte zu öffnen. Suche, wie im Screenshot gezeigt, nach *„Silicon Labs CP210x to UART Bridge (COMx)"* und notiere dir die COM-Nummer (im Beispiel **COM8**). Diese Nummer wird im nächsten Schritt benötigt, damit der PC weiß, wohin die neue Firmware-Version hochgeladen werden soll. Setzen wir diesen Vorgang fort...

<figure data-latex-placement="H">
<img src="figures/device_manager.png" style="width:80.0%" />
<figcaption>Geräte-Manager UART serielle Schnittstelle (COM8).</figcaption>
</figure>

Besuche die [offizielle ESP32-Website](https://www.espressif.com/en/support/download/other-tools), um ein Tool herunterzuladen, das wir zum Flashen der Firmware auf unsere Blackbox-Platine benötigen. Suche nach **„Flash Download Tools"** und drücke die Schaltfläche wie im Bild gezeigt. Suche dann auf der Seite nach den *„Flash Download Tools"* mit dem Speichern-Symbol und klicke darauf.

Dadurch wird ein ZIP-Ordner namens *„flashdownloadtoolx.x.x.zip"* heruntergeladen, wobei die „x"-Symbole durch die Versionsbezeichnung ersetzt werden (in diesem Beispiel **V3.9.11**). Beim Öffnen des heruntergeladenen ZIP-Ordners wirst du feststellen, dass sich darin ein weiterer Ordner befindet. Entpacke diesen auf deinen Desktop oder an einen beliebigen Ort und öffne ihn. Die darin enthaltenen Dateien entsprechen in der Regel den im Screenshot unten aufgelisteten.

<figure data-latex-placement="H">
<img src="figures/esptool_folder.png" style="width:70.0%" />
<figcaption>Inhalt des Flash-Tools-ZIP-Ordners.</figcaption>
</figure>

Wähle die Datei *„flashdownloadtool.11.exe"* (oder die entsprechende heruntergeladene Version) aus und führe sie mit Administratorrechten aus, indem du mit der rechten Maustaste auf die Datei klickst und die Option **„Als Administrator ausführen"** wählst. Falls du dazu aufgefordert wirst, erlaube der ausführbaren Datei die Durchführung von Aktionen auf deinem Computer.\
Sobald das Programm gestartet ist, sollte sich ein Terminal-Fenster öffnen, das nach einigen Sekunden die Benutzeroberfläche startet. Sie sollte so aussehen wie im ersten Beispiel hier gezeigt. Du musst den **„ChipType"** auf *„ESP32"* ändern, wie im zweiten Schritt unten dargestellt. Lass den Rest unverändert und drücke die Schaltfläche **„OK"**.

<figure data-latex-placement="H">
<img src="figures/launching_flashtool.png" style="width:85.0%" />
<figcaption>ESP32-Hauptplatine im Auswahldialog auswählen.</figcaption>
</figure>

### Der Ablauf des Updates

Sobald du die Schaltfläche **„OK"** drückst, öffnet sich ein Fenster mit dem Titel *„ESP32 DOWNLOAD TOOL"*. Entpacke nun die Binärdatei (mit der Endung *.bin*), die dem ToM+-Firmware-Release-ZIP beiliegt, wie in Abschnitt [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"} beschrieben.

Drücke dann die im ersten Bild gezeigte Schaltfläche **„..."** und wähle den Pfad der *„.bin"*-Datei aus. Sobald du das getan hast, klicke auf die Schaltfläche **„Öffnen"**, woraufhin in der ersten Zeile ein grüner Eintrag mit dem gerade bestätigten Pfad erscheint.

Fahre fort, indem du das **Kontrollkästchen neben der ersten Zeile aktivierst**, um die Firmware auszuwählen, die du hochladen möchtest. Gib dann in das im zweiten Bild gezeigte Textfeld diese Zeichenfolge ein: **0$\times$`<!-- -->`{=html}10000** (mit vier Nullen). Dies stellt die Speicherstartadresse dar, an der die Firmware-Dateien abgelegt werden.

Nun folgt der letzte Konfigurationsschritt: Wähle die COM-Nummer über das Auswahlfeld in der unteren rechten Ecke. Stelle sicher, dass du den richtigen COM-Port auswählst, den wir uns zuvor im **Geräte-Manager** notiert haben.

<figure data-latex-placement="H">
<img src="figures/flashtool_page.png" style="width:100.0%" />
<figcaption>Konfigurationsschritte im ESP32 Download Tool.</figcaption>
</figure>

Starte nun das Update, indem du auf die Schaltfläche **„START"** drückst, wie im ersten Bild gezeigt. Am unteren Rand des Fensters erscheint ein grüner Fortschrittsbalken; der gesamte Vorgang dauert in der Regel ein paar Minuten.

Sobald der Upload abgeschlossen ist, siehst du die Meldung **„FINISH"** im grünen Feld in der linken unteren Ecke, wie im Bild gezeigt. Als zusätzliche Bestätigung ist der Fortschrittsbalken voll -- das Update ist nun abgeschlossen.

<figure data-latex-placement="H">
<img src="figures/flashtool_page2.png" style="width:100.0%" />
<figcaption>ESP32 Download Tool schließt das Update ab.</figcaption>
</figure>

Schließe nun dieses Fenster. Anschließend kannst du das Kabel sicher von deinem PC und vom ToM+ trennen. Erst nach diesen Schritten kannst du die normale Stromversorgung des ToM+ wiederherstellen, indem du den Schalter in den Zustand 1 bringst und deinen Twizy mit dem Zündschlüssel einschaltest.

Um deine vorherigen Konfigurationen wiederherzustellen, rufe die ToM+-Einstellungsseite auf, indem du auf die drei Punkte in der oberen rechten Ecke drückst, und drücke dann die Beenden-Taste, ohne etwas zu ändern. Auf diese Weise wird die im Blackbox-Speicher gespeicherte Datenstruktur aktualisiert und deine Einstellungen sind wieder vorhanden.\
**Herzlichen Glückwunsch!** Du hast den gesamten Update-Vorgang abgeschlossen. Genieße nun die neue Firmware und denke daran, mir Fehler oder Probleme per privater Nachricht zu melden, eventuell mit einem beigefügten Bild.

## Aktualisieren der Blackbox (Unix)

Die Blackbox ist die zweite wesentliche Komponente von ToM+ und bildet das Gehirn des gesamten Systems. Wenn wir nur das Display aktualisieren, weiß die Blackbox nicht, wofür die neuen Icons gedacht sind, was zu Kommunikationsfehlern führt.

Daher ist es entscheidend, die neue Firmware auch auf der Hauptplatine von ToM+ zu installieren. Dazu benötigen wir die microSD-Karte nicht mehr, sondern verwenden das zuvor vorbereitete Micro-USB-Kabel und den Computer. Wir werden die Firmware direkt auf das ESP32-Board flashen, um die neue Software zu installieren.

Stelle vor allen weiteren Schritten den Schalter der ToM+-Blackbox auf OFF (*d. h. Symbol 0 darauf*) und schalte auch deinen Twizy aus. Dies ist ein wichtiger Schritt, der strikt befolgt werden muss, um Schäden am Gerät zu vermeiden.

### Vorbereiten des Computers

Lade den im Firmware-Release-Beitrag angehängten ToM+-Firmware-Update-Ordner herunter. Entpacke nun die im ToM+-Firmware-Release-ZIP enthaltene Binärdatei (Endung *.bin*), wie in Abschnitt [5.1.3](#sec:update_files){reference-type="ref" reference="sec:update_files"} beschrieben. Die Datei heißt in der Regel *„FwXXESP32.bin"*, wobei das Symbol *„XX"* durch die Versionsnummer ersetzt wird, zum Beispiel *„23"*.\
**Haftungsausschluss:** *Dieser Blackbox-Vorgang wurde unter Ubuntu 20.04 getestet (hoffe, er funktioniert auch mit anderen Unix-Distributionen). Schließe die Blackbox erst an, wenn du ausdrücklich dazu aufgefordert wirst*.\
Nun müssen wir das Paket esptool installieren, um die neue Firmware auf die Blackbox zu flashen. Führe dies entweder über die grafische Benutzeroberfläche der Paketverwaltung deiner Unix-Distribution aus oder mit dem entsprechenden Befehl im Terminal. Zum Beispiel *„sudo apt-get esptool"*, wie im Bild gezeigt. Gib bei Aufforderung das Passwort des Sudo-Benutzers ein, drücke EINGABE und warte.

<figure data-latex-placement="H">
<img src="figures/apt_get_esptool.png" style="width:100.0%" />
<figcaption>Installation des esptool-Pakets unter Ubuntu.</figcaption>
</figure>

Als Nächstes musst du Python installieren, falls du es noch nicht installiert hast, da das esptool in der Sprache Python geschrieben ist. Gib daher den Befehl *„sudo apt-get python"* ein, wie im Bild gezeigt. Gib bei Aufforderung erneut das Passwort des Sudo-Benutzers ein, drücke EINGABE und warte.

<figure data-latex-placement="H">
<img src="figures/apt_get_python.png" style="width:100.0%" />
<figcaption>Installation des Python-Pakets unter Ubuntu.</figcaption>
</figure>

Sobald beide Pakete installiert sind, gib *„sudo tail -f /var/log/messages"* im Terminal ein, wie im Bild gezeigt, um die Logdatei in Echtzeit zu überwachen. Diese zeigt an, welchem COM-Port die Blackbox vom Betriebssystem zugewiesen wird. Gib bei Aufforderung das Passwort des Sudo-Benutzers ein und drücke EINGABE. **Jetzt können wir die Blackbox anschließen**.

<figure data-latex-placement="H">
<img src="figures/tail_com.png" style="width:100.0%" />
<figcaption>Echtzeit-Überwachung der COM-Verbindungen.</figcaption>
</figure>

Die Blackbox verfügt auf der Rückseite über einen kleinen Micro-USB-Anschluss, wie in Abbildung [5.1](#fig:black_box_labels){reference-type="ref" reference="fig:black_box_labels"} zu sehen ist. Schließe also die Micro-USB-Seite des Kabels an die Blackbox an. Verbinde danach die USB-Seite des Kabels mit einem freien USB-Anschluss deines Computers.

**WICHTIG!** Beide Seiten des Kabels passen nur in einer Richtung in die entsprechenden Buchsen. Wende daher keine Gewalt an, da du sonst den Anschluss des ToM+ oder deines Computers beschädigen könntest. Versuche, den Stecker umzudrehen, und prüfe, ob es so passt.\
Sobald du die Blackbox an den Computer anschließt, solltest du eine Ausgabe erhalten, die der hier im Codeblock gezeigten ähnelt.

``` {.bash language="bash"}
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.232228] usb 1-3: new full-speed USB
device number 3 using xhci_hcd
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423441] usb 1-3: New USB device found,
idVendor=10c4, idProduct=ea60, bcdDevice= 1.00
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423453] usb 1-3: New USB device
strings: Mfr=1, Product=2, SerialNumber=3
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423457] usb 1-3: Product: CP2102 USB
to UART Bridge Controller
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423461] usb 1-3: Manufacturer: Silicon
Labs
85
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.423464] usb 1-3: SerialNumber: 0001
Oct 15 11:05:14 Kubuntu2004 mtp-probe: checking bus 1, device 3:
"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-3"
Oct 15 11:05:14 Kubuntu2004 mtp-probe: bus: 1, device: 3 was not an MTP device
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.457397] usbcore: registered new
interface driver usbserial_generic
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.457415] usbserial: USB Serial support
registered for generic
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460166] usbcore: registered new
interface driver cp210x
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460185] usbserial: USB Serial support
registered for cp210x
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.460236] cp210x 1-3:1.0: cp210x
converter detected
Oct 15 11:05:14 Kubuntu2004 kernel: [ 172.464538] usb 1-3: cp210x converter now
attached to ttyUSB0
Oct 15 11:05:14 Kubuntu2004 mtp-probe: checking bus 1, device 3:
"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-3"
Oct 15 11:05:14 Kubuntu2004 mtp-probe: bus: 1, device: 3 was not an MTP device
```

Die Zeile, die uns interessiert, ist diese: *„cp210x converter now attached to ttyUSB0"*, wobei das Wort **„ttyUSB0"** die serielle Schnittstelle ist, an der die Blackbox angeschlossen ist. Notiere dir daher diesen Port (der von meinem abweichen kann), da wir ihn beim Hochladen der neuen Firmware benötigen.

### Der Ablauf des Updates

Navigiere mit deinem Dateimanager in den Ordner, in dem die Firmware-*.bin*-Datei gespeichert ist, und öffne dort ein Terminal, indem du mit der rechten Maustaste auf den Ordner klickst und die Option **„Terminal öffnen"** aus dem Kontextmenü wählst. Alternativ kannst du auch manuell mit dem Befehl „cd" durch deine Ordner navigieren, bis du den richtigen Ordner gefunden hast.

Sobald du dich im richtigen Verzeichnis befindest, führe diesen langen und etwas trockenen Befehl aus. Ersetze dabei *„ttyUSBx"* durch den Namen der seriellen Schnittstelle, den wir im vorherigen Schritt notiert haben (z. B. *„ttyUSB0"*), und *„ESP32FwXX.bin"* durch den Namen der *„.bin"*-Datei, die die auf ToM+ zu ladende Firmware-Version enthält (z. B. *„ESP32Fw23.bin"*).

        python /usr/share/esptool/esptool.py --chip auto --port /dev/ttyUSBx --baud
    921600 --before default_reset --after hard_reset write_flash -z --flash_mode dio
    --flash_freq 40m --flash_size 4MB 0x10000 ESP32_FwXX.bin

Du solltest eine Ausgabe ähnlich der folgenden erhalten:

``` {.bash language="bash"}
Serial port /dev/ttyUSB0
Connecting........_____.....____
Detecting chip type... ESP32
Chip is ESP32D0WDQ5 (revision 3)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme
None
Crystal is 40MHz
MAC: xx:xx:xx:xx:xx:xx
Changing baud rate to 921600
Changed.
Enabling default SPI flash mode...
Configuring flash size...
Erasing flash...
Compressed 716176 bytes to 461048...
Took 2.90s to erase flash block
Wrote 716176 bytes (461048 compressed) at 0x00010000 in 9.1 seconds (effective
630.3 kbit/s)...
Hash of data verified.
Leaving...
Hard resetting via RTS pin...
```

Schließe nun dieses Fenster und alle anderen. Anschließend kannst du das Kabel sicher von deinem PC und vom ToM+ trennen. Erst nach diesen Schritten kannst du die normale Stromversorgung des ToM+ wiederherstellen, indem du den Schalter in den Zustand 1 bringst und deinen Twizy mit dem Zündschlüssel einschaltest.

Um deine vorherigen Konfigurationen wiederherzustellen, rufe die ToM+-Einstellungsseite auf, indem du auf die drei Punkte in der oberen rechten Ecke drückst, und drücke dann die Beenden-Taste, ohne etwas zu ändern. Auf diese Weise wird die im Blackbox-Speicher gespeicherte Datenstruktur aktualisiert und deine Einstellungen sind wieder vorhanden.\
**Herzlichen Glückwunsch!** Du hast den gesamten Update-Vorgang abgeschlossen. Genieße nun die neue Firmware und denke daran, mir Fehler oder Probleme per privater Nachricht zu melden, eventuell mit einem beigefügten Bild.

# Tuning auf Ihrem ToM+ (Twizy-cfg) {#apx:tuning}

## Was ist Twizy-cfg?

[Twizy-Cfg](http://github.com/dexterbg/Twizy-Cfg) ist eine **Open-Source**, leichtgewichtige Konfigurations-Shell, die für den im Renault Twizy verbauten SEVCON Gen4-Motorcontroller entwickelt wurde. Sie wurde von [dexterbg](https://github.com/dexterbg) entwickelt. Das Tool wurde für den Betrieb auf Arduino-Mikrocontrollern mit einem MCP2515-SPI-CAN-Bus-Modul entwickelt und bietet Hardware-Hackern, Technikern und EV-Enthusiasten eine direkte Kommandozeilenschnittstelle zur Interaktion mit dem Antriebssystem des Fahrzeugs über den standardmäßigen **OBD-II-Diagnoseanschluss**.\
Im Kern fungiert Twizy-cfg als Brücke zwischen *High-Level*-Makrobefehlen und *Low-Level* CANopen-SDO-Registeroperationen. Dadurch ermöglicht es eine präzise Abstimmung und Überwachung des Antriebsstrangs und bietet unter anderem folgende Möglichkeiten:\

- Anpassung des Fahrprofils: Einstellung wichtiger Leistungsparameter wie maximale Leistung, Drehmomentbegrenzungen, Höchstgeschwindigkeit und Beschleunigungsrampen.

- Energiemanagement: Feinabstimmung der Energierückgewinnung beim Ausrollen und Bremsen, um Reichweite und Bremswirkung auszubalancieren.

- Profilverwaltung: Speichern, Laden und Wiederherstellen benutzerdefinierter Leistungsprofile direkt im bzw. aus dem EEPROM des Arduino.

- Diagnose & Low-Level-Zugriff: Ausführen von rohen CANopen-Befehlen und grundlegenden OBD-II-Diagnoseanfragen zur Untersuchung von Controller-Zuständen und Firmware-Versionen.

 \
Dieser Anhang beschreibt, wie ToM+ eine spezielle Partition mit der oben genannten Software verwalten kann, die für den Betrieb auf dem ESP32-Board (ToM+-Chip) angepasst wurde.

## Voraussetzungen

**HINWEIS!** Ziel dieses Anhangs ist die Installation und Ausführung einer alternativen Firmware, die nicht von mir programmiert wurde und die Hardware für einen anderen Zweck verwendet als den, für den sie entwickelt wurde. Wenn Sie dieser Anleitung folgen, verfügen Sie über eine **Dual-Boot-Blackbox**, in der die ToM+-Firmware und die Twizy-cfg-Firmware gemeinsam vorhanden sind und je nach Bedarf gestartet werden können.\
Dafür benötigen Sie eine Blackbox mit einer Firmware-Version **1.45** oder höher. Dies ist eine wichtige Voraussetzung, da dieser Vorgang die OTA-Update-Funktion benötigt, die mit der genannten Version eingeführt wurde. Siehe Abschnitt [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}, um Ihre ESP-Firmware-Version zu überprüfen, und Abschnitt [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}, um Ihre Firmware bei Bedarf per OTA zu aktualisieren.\
Anschließend benötigen Sie die kompilierte Version von ESP32-kompatiblem Twizy-cfg, die Sie über [diesen Link](https://www.mediafire.com/file/n5waunl2w19cpl6/TwizyCfg_ok.ino.bin.zip/file) herunterladen können. Entpacken Sie den Inhalt und behalten Sie die *".bin"*-Datei, die wir später benötigen.

## Der Update-Vorgang

Verbinden Sie sich nun mit dem Webserver, indem Sie eine der in Abschnitt [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} beschriebenen Methoden verwenden, und navigieren Sie anschließend zur Seite **„OTA Update and Prefs"** (Abschnitt [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}). Verwenden Sie dort die zuvor extrahierte *".bin"*-Datei für das Update und aktivieren Sie die Option **„Update to special partition"** (andernfalls ersetzen Sie die originale ToM+-Firmware).\

<figure data-latex-placement="H">
<img src="figures/ota_page3.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Update- und Informationstabelle.</figcaption>
</figure>

Wenn der Fortschrittsbalken 100% erreicht, wird das ToM+-LCD-Display schwarz. Dies ist das erfolgreiche Zeichen dafür, dass ToM+ neu startet und die *Twizy-cfg*-Software lädt. Verbinden Sie sich nun auf Ihrem Gerät mit dem Access Point **„Twizy-cfg"**, um auf dessen Webserver zuzugreifen. Falls Sie dazu aufgefordert werden, bestätigen Sie, dass die Verbindung aktiv bleiben soll, auch wenn kein Internetzugang verfügbar ist.

Das **Passwort** ist das Standard-ToM+-Passwort, also das Wort „pass" gefolgt von der Seriennummer Ihres Geräts (z. B. *pass129777*). Die Seriennummer finden Sie auf der Einstellungsseite, wie in Abbildung [3.3](#fig:settings_page){reference-type="ref" reference="fig:settings_page"} erklärt.\
Öffnen Sie nun einen Webbrowser und geben Sie **192.168.4.1/webserial** ein, um zum Webserver-Interface zu gelangen, über das Sie Tuning-Befehle senden können. Das Command-Terminal sieht ähnlich aus wie das hier gezeigte Bild. Wie bereits erwähnt, ist Tuning keine offizielle ToM+-Funktion und *Twizy-cfg* wurde nicht von mir entwickelt. Informationen zu Tuning-Befehlen und Konfigurationen finden Sie daher im [Twizy-cfg-Forumsthema](https://www.twizy-forum.de/projekte-twizy/83451-twizy-cfg-sevcon-shell-fuer-arduino?start=0) oder im [Github-Repository](https://github.com/dexterbg/Twizy-Cfg).\

<figure data-latex-placement="H">
<img src="figures/TuningMonitor.PNG" style="width:70.0%" />
<figcaption>Tuning-Monitor zur Ausführung von Tuning-Befehlen.</figcaption>
</figure>

Solange Sie Twizy-cfg verwenden, wird die ToM+-Firmware nicht geladen und das Display bleibt daher ausgeschaltet. Wenn Sie zur offiziellen ToM+-Firmware zurückkehren möchten, müssen Sie lediglich den selbsterklärenden Befehl **reboot** im Tuning-Monitor eingeben.\
Damit startet ToM+ neu und wechselt zur anderen Partition, sodass es wieder sein normales Verhalten zeigt. Die Tuning-Konfiguration bleibt dabei in Ihrem Twizy erhalten. Wenn Sie die Twizy-cfg-Shell erneut benötigen, öffnen Sie einfach die Seite **„OTA Update and Prefs"** auf dem ToM+-Webserver und wählen Sie die Option *„REBOOT FROM SPECIAL PARTITION"* aus der in der folgenden Abbildung gezeigten Tabelle. Die *".bin"*-Datei muss nicht erneut hochgeladen werden.

<figure data-latex-placement="H">
<img src="figures/ota_boot.png" style="width:100.0%" />
<figcaption>OTA-Update-Seite — Tabelle mit Boot-Optionen.</figcaption>
</figure>

# Steuerung eines Tasmota-WLAN-Schalters {#apx:tasmota}

## Was sind WLAN-Schalter/-Steckdosen?

In diesem Anhang erkläre ich, wie Sie Ihr ToM+ so konfigurieren können, dass es mit einem WLAN-AC-Schalter / einer WLAN-AC-Steckdose oder jedem anderen Gerät mit **Tasmota-Firmware** interagiert.

Im Grunde handelt es sich dabei um *Relaismodule*, die über eine drahtlose Verbindung aus der Ferne gesteuert werden können. Solche Geräte sind auf vielen E-Commerce-Websites (wie Amazon) für wenige Dutzend Euro erhältlich.\
Sie sind in vielen verschiedenen Bauformen erhältlich, häufig jedoch in den beiden in der Abbildung gezeigten Varianten. Die zweite Variante ist kompakter und benutzerfreundlicher, während die erste eine Kabelverbindung benötigt, um mit Ihren elektrischen Geräten verbunden zu werden.

<figure data-latex-placement="ht">
<figure>
<img src="figures/Sonoff.PNG" />
<figcaption>Sonoff WLAN-Smart-Switch.</figcaption>
</figure>
<figure>
<img src="figures/TasmotaPlug.PNG" />
<figcaption>Tasmota-WLAN-Smart-Plug.</figcaption>
</figure>
<figcaption>Tasmota-WLAN-Smart-Plug.</figcaption>
</figure>

*Aber warum ist das nützlich?* Es gibt viele Gründe, warum Sie ToM+ mit solchen Geräten verbinden möchten. Nehmen wir an, Sie möchten das Laden der Traktionsbatterie stoppen, wenn das Ladegerät überhitzt, und den Ladevorgang wieder starten, wenn die Temperatur sinkt; oder Sie möchten **den Ladevorgang stoppen**, sobald ein gewünschter SOC erreicht wurde.

Oder, wie ich es in diesem Anhang zu experimentellen Zwecken gemacht habe, eine Lampe in meinem Zimmer einschalten, wenn der Twizy (in der Garage geparkt) den Ladevorgang fast abgeschlossen hat. Kurz gesagt gibt es zahlreiche nützliche Ideen, bei denen ein WLAN-Schalter/eine WLAN-Steckdose zusammen mit ToM+ eingesetzt werden kann, um interessante Projekte zu realisieren.

## Voraussetzungen

Dafür benötigen Sie eine Blackbox mit einer Firmware-Version **1.4** oder höher. Dies ist eine wichtige Voraussetzung, da dieser Vorgang Funktionen benötigt, die mit der genannten Version eingeführt wurden. Siehe Abschnitt [3.10](#sec:settings_page){reference-type="ref" reference="sec:settings_page"}, um Ihre ESP-Firmware-Version zu überprüfen, und Abschnitt [4.4.10](#sec:web_ota_update){reference-type="ref" reference="sec:web_ota_update"}, um Ihre Firmware bei Bedarf per OTA zu aktualisieren.

Zusätzlich müssen **WLAN und MQTT konfiguriert** sein, damit das gesamte System funktioniert. Falls dies noch nicht geschehen ist, lesen Sie bitte Abschnitt [4.1](#sec:wifi_settings){reference-type="ref" reference="sec:wifi_settings"}, um WLAN einzurichten, und Abschnitt [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"} für die MQTT-Konfiguration. Beide müssen aktiviert und verbunden sein, damit diese Funktion verwendet werden kann.\
Außerdem benötigen Sie selbstverständlich einen WLAN-Schalter oder eine WLAN-Steckdose, je nach Bedarf. Das Gerät muss mit einer **Tasmota-Firmware** (*Version 7* oder höher) laufen.

Beachten Sie, dass Geräte wie *„Sonoff"* ab Werk mit einer proprietären Firmware ausgeliefert werden, die das MQTT-Protokoll nicht nativ unterstützt.\
Um solche Geräte wie in diesem Anhang verwenden zu können, müssen Sie sie auf die Tasmota-Firmware aktualisieren. Im Internet finden sich zahlreiche Anleitungen zur Installation der Tasmota-Firmware. Suchen Sie nach einer Anleitung, die zu Ihrem Gerät passt, und folgen Sie dieser. Wenn Sie sich nicht mit dem Firmware-Update beschäftigen möchten, empfehle ich persönlich, ein Gerät zu kaufen, auf dem Tasmota bereits installiert ist.

## Tasmota-MQTT-Konfiguration

Navigieren Sie zur **Tasmota WebUI**. Dort wird eine Startseite ähnlich der unten gezeigten angezeigt. Bei Unsicherheiten können Sie jederzeit die [offizielle Dokumentation](https://tasmota.github.io/docs/) konsultieren.

<figure data-latex-placement="H">
<img src="figures/Mqtt1.PNG" style="width:45.0%" />
<figcaption>Tasmota WebUI — Startseite.</figcaption>
</figure>

Drücken Sie zunächst die Schaltfläche **„Configuration"**, die Sie zur auf dem ersten Bild unten gezeigten Seite führt. Konfigurieren Sie anschließend die *WLAN-Verbindung*, indem Sie Ihre Zugangsdaten (SSID und Passwort) auf der Tasmota-Seite **„Configure WiFi"** eingeben. Folgen Sie danach den Anweisungen zur Konfiguration der *MQTT-Einstellungen*, indem Sie die WebUI-Seite **„Configure MQTT"** aufrufen.\

<figure data-latex-placement="ht">
<figure>
<img src="figures/Mqtt2.PNG" />
<figcaption>Konfigurationsseite.</figcaption>
</figure>
<figure>
<img src="figures/Mqtt4.PNG" />
<figcaption>MQTT-Konfigurationsseite.</figcaption>
</figure>
<figcaption>MQTT-Konfigurationsseite.</figcaption>
</figure>

Geben Sie nun Broker-Adresse, Benutzer-ID, Passwort und Portnummer ein. Diese müssen mit den auf ToM+ eingestellten Werten übereinstimmen! Die Erklärung der einzelnen Felder finden Sie in Abschnitt [4.2.4](#sec:mqtt_connection){reference-type="ref" reference="sec:mqtt_connection"}.\
Die schwierigsten Parameter sind **„Topic"** und **„Full Topic"**. Diese dürfen nicht mit den MQTT-Topics von ToM+ identisch sein, da sie spezifisch für das von Ihnen verwendete Gerät sind. Wenn Sie dieselben *TOMin*- und *TOMout*-Topics verwenden, können sich die Kommunikationen gegenseitig stören.\
Geben Sie im ersten Feld einen beliebigen Wert ein. Ich empfehle eine kurze Bezeichnung, die an die Funktion Ihres Geräts erinnert. Verwenden Sie jedoch eine kurze Zeichenfolge (5/6 Zeichen sind ausreichend), da dieses Feld nur einen kleinen Teil des vollständigen Topic-Strings bildet und ToM+ eine Begrenzung von 50 Zeichen für das Feld **„Auxilliary MQTT command"** besitzt (siehe Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"}).\
Beim zweiten Feld ist es wichtig, zwischen zwei Optionen zu unterscheiden, abhängig davon, welchen Broker Sie verwenden. Wenn Sie einen eigenen Broker verwenden (also *nicht Maqiatto*), lassen Sie die Standardzeichenfolge **%prefix%/%topic%/** unverändert.\
Wenn Sie stattdessen Maqiatto verwenden, das gemäß Abschnitt [4.2.3](#sec:free_broker){reference-type="ref" reference="sec:free_broker"} konfiguriert wurde, oder einen anderen Broker, der *Ihre E-Mail-Adresse als Präfix* des Topic-Namens hinzufügt, bearbeiten Sie das Feld **„Full Topic"** entsprechend. Die Felder sehen dann wie im zweiten Bild oben aus, sodass **myemail@gmail.com/%prefix%/%topic%/** eingetragen wird, wobei Ihre Benutzer-ID (E-Mail-Adresse) als Präfix hinzugefügt wird.

Drücken Sie abschließend die grüne Schaltfläche **„Save"** und warten Sie, bis das Gerät neu startet.\
**NICHT VERGESSEN!** Wenn Sie den Maqiatto-Broker verwenden, müssen Sie möglicherweise das neue Topic zu Ihrem Konto hinzufügen, wie in Abbildung [4.2](#sec:free_broker_add_topics){reference-type="ref" reference="sec:free_broker_add_topics"} erklärt.

In diesem Fall müssen Sie **cmnd/\<your Tasmota topic name\>/Power** als neuen Topic-Namen hinzufügen. Wenn Sie dem Beispielbild gefolgt sind, lautet dieser *cmnd/charge/Power*.

## ToM+-Tasmota-Konfiguration

Öffnen Sie den ToM+-Webserver wie in Abschnitt [4.4.2](#sec:web_server_access){reference-type="ref" reference="sec:web_server_access"} beschrieben und gehen Sie zur Seite **„Alarm triggers"**. Fügen Sie nun einen neuen Alarm zur Liste hinzu, entsprechend dem Wert, der Ihr Tasmota-Gerät steuern soll, wie in Abschnitt [4.4.8](#sec:web_alarm_triggers){reference-type="ref" reference="sec:web_alarm_triggers"} beschrieben.

In meinem Fall habe ich den Wert **„Battery SOC"** gewählt, der einen Alarm auslöst, wenn sein Wert *97%* erreicht, um den fast abgeschlossenen Ladevorgang zu melden.

<figure data-latex-placement="H">
<img src="figures/Tom01.PNG" style="width:70.0%" />
<figcaption>Hinzufügen des Tasmota-Triggers in ToM+.</figcaption>
</figure>

Wie Sie sehen können, ist der wichtigste Teil die korrekte Konfiguration des Feldes **„Aux Cmd"**, da es den MQTT-Steuerbefehl enthält, den ToM+ an das Tasmota-Gerät senden wird.

Wenn Sie einen eigenen MQTT-Broker verwenden (also *nicht Maqiatto*), hat **Aux Cmd** folgende Syntax:

- *cmnd/\<your Tasmota topic name\>/Power 1*, wenn das Gerät eingeschaltet werden soll.

- *cmnd/\<your Tasmota topic name\>/Power 0*, wenn das Gerät ausgeschaltet werden soll.

In unserem Beispiel lautet der Befehl zum Einschalten der Lampe **cmnd/charge/Power 1**.\
Wenn Sie hingegen den Maqiatto-Broker oder einen anderen Broker verwenden, der Ihre Benutzer-ID (E-Mail-Adresse) als Präfix im Topic-Namen verwendet, sieht die Syntax für **Aux Cmd** folgendermaßen aus:

- *myemail@gmail.com/cmnd/\<your Tasmota topic name\>/Power 1*, um das Gerät einzuschalten.

- *myemail@gmail.com/cmnd/\<your Tasmota topic name\>/Power 0*, um das Gerät auszuschalten.

In unserem Fall lautet der Befehl **myemail@gmail.com/cmnd/charge/Power 1**.\
Wenn Sie den Ladevorgang stoppen und anschließend unter bestimmten Bedingungen wieder starten möchten, müssen Sie zwei Alarme hinzufügen: einen für die Power-ON- und einen für die Power-OFF-Bedingung, jeweils mit der oben beschriebenen Syntax.\
Bitte beachten Sie, dass Sie bei einem Gerät mit mehreren Relais die oben beschriebene Syntax anpassen müssen, um festzulegen, welches Relais Sie steuern möchten: Verwenden Sie **„Power1"** für das erste Relais, **„Power2"** für das zweite und so weiter. Dies ergibt:

- *cmnd/\<your Tasmota topic name\>/Power1 1*, um das erste Relais einzuschalten.

- *cmnd/\<your Tasmota topic name\>/Power1 0*, um es auszuschalten.

Die gleiche Unterscheidung bezüglich Maqiatto und eigenen Brokern gilt auch hier.

## Häufige Probleme und Lösungen

Einige Tasmota-Firmwares kommen mit dem *Maqiatto*-Topic-Format nicht gut zurecht. Wenn Sie ein Tasmota-Gerät mit ToM+ steuern möchten, müssen Sie daher einen anderen MQTT-Broker verwenden. Nach einigen Tests habe ich festgestellt, dass Sie erfolgreich [mqtt.dealgate.ru](https://dealgate.ru/) verwenden können, einen kostenlosen und funktionsreicheren Broker.

Der Nachteil ist, dass Sie bei der Erstellung des Kontos mit einigen russischen Übersetzungen konfrontiert werden. Aber dafür reicht ein Online-Übersetzer problemlos aus.
