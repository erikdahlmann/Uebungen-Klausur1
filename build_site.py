# -*- coding: utf-8 -*-
"""Baut index.html: 24 aussortierte Klausuraufgaben mit ausklappbarer Musterlösung.
Quellen: klausur1/aufgaben aussotiert.docx (Aufgabentexte), Klausur1_Vorschlaege.docx
und Ergaenzende_Aufgaben_mit_Loesungen.docx (Erwartungshorizonte, hier zu
ausführlichen Lösungen ausgebaut)."""
import html, json

V = lambda a, b, c: r"\begin{pmatrix}%s\\%s\\%s\end{pmatrix}" % (a, b, c)

AUFGABEN = []
def A(block, kennung, titel, be, kontext, teile, weg, loesung, fehler=None):
    AUFGABEN.append(dict(block=block, kennung=kennung, titel=titel, be=be,
                         kontext=kontext, teile=teile, weg=weg,
                         loesung=loesung, fehler=fehler))

# ══════════════════════════════════════════════════ A1 · Abstand Punkt–Ebene
A("A1", "A1 V2", "Abstand Punkt–Ebene, parallele Ebenen", 6,
  r"Gegeben sind die Ebene \(E:\; x_1+2x_2-2x_3=3\) und der Punkt \(P(2\,|\,4\,|\,-1)\).",
  [("a", r"Berechne den Abstand von \(P\) zu \(E\).", 3),
   ("b", r"Bestimme die Gleichungen der beiden zu \(E\) parallelen Ebenen, die von \(E\) den Abstand 3 haben.", 3)],
  r"""Beide Teile laufen über die Hessesche Normalform. Der Trick in b): Parallele Ebenen haben
  <em>denselben</em> Normalenvektor, es ändert sich nur die Zahl auf der rechten Seite.""",
  [("a", r"""Normalenvektor ablesen und Länge bestimmen:
   \[\vec n=""" + V("1","2","-2") + r""",\qquad |\vec n|=\sqrt{1+4+4}=3.\]
   Damit lautet die Hessesche Normalform \(\dfrac{x_1+2x_2-2x_3-3}{3}=0\).
   Jetzt \(P\) einsetzen und den Betrag nehmen:
   \[d(P,E)=\frac{|2+8+2-3|}{3}=\frac{9}{3}=3.\]"""),
   ("b", r"""Eine parallele Ebene hat die Form \(x_1+2x_2-2x_3=c\). Ihr Abstand zu \(E\) ist
   \[\frac{|c-3|}{3}=3\quad\Longleftrightarrow\quad |c-3|=9.\]
   Also \(c-3=9\) oder \(c-3=-9\), das heißt \(c=12\) oder \(c=-6\):
   \[E_1:\; x_1+2x_2-2x_3=12,\qquad E_2:\; x_1+2x_2-2x_3=-6.\]
   Kontrolle: \(P\) erfüllt \(2+8+2=12\), liegt also auf \(E_1\) — passend zum Abstand 3 aus a).""")],
  r"In a) den Betrag vergessen. Bei anderen Zahlen kommt dann ein negativer „Abstand“ heraus."),

A("A1", "A1 V3", "Abstand und zwei mögliche Punkte", 6,
  r"Gegeben sind die Ebene \(E:\; 2x_1+2x_2+x_3=9\) und der Ursprung \(O(0\,|\,0\,|\,0)\).",
  [("a", r"Bestimme den Abstand von \(O\) zu \(E\) mithilfe der Hesseschen Normalform.", 3),
   ("b", r"Bestimme alle Punkte auf der \(x_3\)-Achse, die von \(E\) den Abstand 3 besitzen.", 3)],
  r"""In b) ist der gesuchte Punkt \(Q(0\,|\,0\,|\,z)\) — auf der \(x_3\)-Achse sind die ersten beiden
  Koordinaten null. Die Abstandsgleichung wird dann zu einer Betragsgleichung in \(z\), und die hat
  <strong>zwei</strong> Lösungen: eine ober- und eine unterhalb der Ebene.""",
  [("a", r"""\[\vec n=""" + V("2","2","1") + r""",\qquad |\vec n|=\sqrt{4+4+1}=3.\]
   HNF: \(\dfrac{2x_1+2x_2+x_3-9}{3}=0\). Einsetzen von \(O(0|0|0)\):
   \[d(O,E)=\frac{|0+0+0-9|}{3}=\frac{9}{3}=3.\]"""),
   ("b", r"""Ansatz \(Q(0\,|\,0\,|\,z)\) und einsetzen:
   \[\frac{|2\cdot 0+2\cdot 0+z-9|}{3}=3\quad\Longleftrightarrow\quad |z-9|=9.\]
   Der Betrag wird aufgespalten:
   \[z-9=9\;\Rightarrow\;z=18,\qquad z-9=-9\;\Rightarrow\;z=0.\]
   Also \(Q_1(0\,|\,0\,|\,18)\) und \(Q_2(0\,|\,0\,|\,0)=O\).
   Das \(O\) dabei ist, passt genau zu a): \(O\) hat ja schon den Abstand 3.""")],
  r"Nur eine Lösung angeben. Der Betrag liefert immer zwei Fälle, solange der Abstand nicht null ist."),

# ══════════════════════════════════════════════════ A2 · Abstand Punkt–Gerade
A("A2", "A2 V1", "Abstand Punkt–Gerade", 5,
  r"Gegeben sind die Gerade \(g:\;\vec x=" + V("1","2","0") + r"+t\cdot" + V("2","1","2") + r"\) und der Punkt \(P(5\,|\,1\,|\,1)\).",
  [("", r"Berechne den Abstand von \(P\) zu \(g\) und bestimme den Lotfußpunkt. Wähle ein geeignetes Verfahren.", 5)],
  r"""Weil auch der <strong>Lotfußpunkt</strong> gefragt ist, führt die Hilfsebene am schnellsten zum Ziel:
  Man legt durch \(P\) eine Ebene senkrecht zu \(g\) und schneidet sie mit \(g\).
  Das Kreuzprodukt liefert zwar den Abstand, aber nicht den Fußpunkt.""",
  [("", r"""<strong>Schritt 1 — Hilfsebene.</strong> Sie steht senkrecht auf \(g\), also ist der
   Richtungsvektor von \(g\) ihr Normalenvektor:
   \[H:\; 2x_1+x_2+2x_3=2\cdot 5+1\cdot 1+2\cdot 1=13.\]
   <strong>Schritt 2 — Gerade einsetzen.</strong>
   \[2(1+2t)+(2+t)+2\cdot 2t=2+4t+2+t+4t=4+9t=13\;\Rightarrow\;t=1.\]
   <strong>Schritt 3 — Fußpunkt.</strong> \(t=1\) in \(g\) einsetzen: \(F(3\,|\,3\,|\,2)\).
   <strong>Schritt 4 — Abstand.</strong>
   \[\vec{PF}=""" + V("3-5","3-1","2-1") + r"""=""" + V("-2","2","1") + r""",\qquad
   d=|\vec{PF}|=\sqrt{4+4+1}=3.\]
   <strong>Kontrolle mit der Flächenformel.</strong> Mit \(\vec{AP}=""" + V("4","-1","1") + r"""\):
   \[\vec u\times\vec{AP}=""" + V("3","6","-6") + r""",\qquad
   d=\frac{|\vec u\times\vec{AP}|}{|\vec u|}=\frac{9}{3}=3.\;\checkmark\]""")],
  r"Die Hilfsebene mit dem falschen Normalenvektor aufstellen. Er ist immer der Richtungsvektor der Geraden."),

A("A2", "A2 V3", "Lotfußpunkt mit Orthogonalitätsbedingung", 5,
  r"Gegeben sind die Gerade \(g:\;\vec x=" + V("1","-1","2") + r"+t\cdot" + V("1","2","2") + r"\) und der Punkt \(P(4\,|\,2\,|\,2)\).",
  [("a", r"Bestimme den Lotfußpunkt \(F\) von \(P\) auf \(g\).", 3),
   ("b", r"Berechne den Abstand von \(P\) zu \(g\).", 2)],
  r"""Hier wird das <strong>Laufpunktverfahren</strong> gezeigt: Man schreibt den allgemeinen
  Geradenpunkt \(F_t\) hin und verlangt, dass \(\vec{F_tP}\) senkrecht auf der Geraden steht.
  Eine Lösung über die Hilfsebene ist gleichwertig.""",
  [("a", r"""Allgemeiner Geradenpunkt:
   \[F_t\,(1+t\;|\;-1+2t\;|\;2+2t).\]
   Verbindungsvektor zu \(P\):
   \[\vec{F_tP}=""" + V("4-(1+t)","2-(-1+2t)","2-(2+2t)") + r"""=""" + V("3-t","3-2t","-2t") + r""".\]
   Orthogonalität zum Richtungsvektor:
   \[""" + V("3-t","3-2t","-2t") + r"""\cdot""" + V("1","2","2") + r"""
   =(3-t)+2(3-2t)-4t=9-9t=0\;\Rightarrow\;t=1.\]
   Einsetzen: \(F(2\,|\,1\,|\,4)\)."""),
   ("b", r"""\[\vec{FP}=""" + V("4-2","2-1","2-4") + r"""=""" + V("2","1","-2") + r""",\qquad
   d=\sqrt{4+1+4}=\sqrt9=3.\]""")],
  r"Beim Skalarprodukt das Minuszeichen in \(-2t\cdot 2=-4t\) verlieren."),

A("A2", "A2 V4", "Einen vermeintlichen Lotfußpunkt prüfen", 5,
  r"""Gegeben sind die Gerade \(g:\;\vec x=t\cdot""" + V("2","1","2") + r"""\) und der Punkt \(P(0\,|\,3\,|\,3)\).
  Eine Schülerin behauptet: „Der Ursprung liegt auf \(g\), also ist er der Lotfußpunkt von \(P\).“""",
  [("a", r"Widerlege die Begründung durch eine Rechnung.", 2),
   ("b", r"Bestimme den tatsächlichen Lotfußpunkt und den Abstand von \(P\) zu \(g\).", 3)],
  r"""Ein Lotfußpunkt braucht <strong>zwei</strong> Eigenschaften: Er liegt auf der Geraden
  <em>und</em> die Verbindung zu \(P\) steht senkrecht auf der Geraden. Die Schülerin prüft nur die erste.""",
  [("a", r"""Der Ursprung liegt tatsächlich auf \(g\) (für \(t=0\)). Das allein reicht aber nicht.
   Zu prüfen ist, ob \(\vec{OP}\) senkrecht auf dem Richtungsvektor steht:
   \[\vec{OP}\cdot\vec u=""" + V("0","3","3") + r"""\cdot""" + V("2","1","2") + r"""=0+3+6=9\neq 0.\]
   Das Skalarprodukt ist nicht null, die Verbindung steht also nicht senkrecht.
   Der Ursprung ist damit <strong>nicht</strong> der Lotfußpunkt."""),
   ("b", r"""Laufpunkt \(F_t\,(2t\,|\,t\,|\,2t)\), Bedingung \(\vec{F_tP}\cdot\vec u=0\):
   \[\left(""" + V("0","3","3") + r"""-t""" + V("2","1","2") + r"""\right)\cdot""" + V("2","1","2") + r"""
   =9-9t=0\;\Rightarrow\;t=1.\]
   Also \(F(2\,|\,1\,|\,2)\) und
   \[\vec{FP}=""" + V("-2","2","1") + r""",\qquad d=\sqrt{4+4+1}=3.\]""")],
  None),

# ══════════════════════════════════════════════════ A3 · Zwei Geraden
A("A3", "A3 V1", "Lage und Abstand zweier Geraden", 5,
  r"Gegeben sind \(g:\;\vec x=" + V("1","0","2") + r"+r\cdot" + V("1","1","0") + r"\) und \(h:\;\vec x=" + V("3","1","4") + r"+s\cdot" + V("0","1","1") + r"\).",
  [("a", r"Untersuche die gegenseitige Lage von \(g\) und \(h\).", 2),
   ("b", r"Berechne den Abstand von \(g\) und \(h\).", 3)],
  r"""Erst Richtungsvektoren vergleichen (parallel?), dann gleichsetzen (Schnittpunkt?).
  Bleibt beides übrig, sind die Geraden windschief. Für den Abstand nimmt man das
  gemeinsame Lot \(\vec n=\vec u\times\vec v\).""",
  [("a", r"""\(\vec u=""" + V("1","1","0") + r"""\) und \(\vec v=""" + V("0","1","1") + r"""\) sind keine
   Vielfachen voneinander, also nicht parallel.<br>
   Gleichsetzen: \(1+r=3\Rightarrow r=2\); \(r=1+s\Rightarrow s=1\); dritte Zeile \(2=4+s\Rightarrow s=-2\).
   Widerspruch — kein Schnittpunkt. Die Geraden sind <strong>windschief</strong>."""),
   ("b", r"""Gemeinsames Lot:
   \[\vec n=\vec u\times\vec v=""" + V("1\\cdot 1-0\\cdot 1","0\\cdot 0-1\\cdot 1","1\\cdot 1-1\\cdot 0") + r"""
   =""" + V("1","-1","1") + r""",\qquad |\vec n|=\sqrt3.\]
   Verbindung der Stützpunkte: \(\vec{AB}=""" + V("2","1","2") + r"""\). Damit
   \[d=\frac{|\vec n\cdot\vec{AB}|}{|\vec n|}=\frac{|2-1+2|}{\sqrt3}=\frac{3}{\sqrt3}=\sqrt3\approx 1{,}73.\]
   Weil \(d\neq 0\) ist, bestätigt sich auch rechnerisch: windschief, nicht schneidend.""")],
  r"Den Betrag im Zähler vergessen — je nach Reihenfolge der Stützpunkte wird das Skalarprodukt negativ."),

A("A3", "A3 V2", "Lage und Abstand zweier Geraden", 6,
  r"Gegeben sind \(g:\;\vec x=" + V("2","1","0") + r"+r\cdot" + V("1","0","1") + r"\) und \(h:\;\vec x=" + V("0","1","1") + r"+s\cdot" + V("1","2","0") + r"\).",
  [("a", r"Untersuche die gegenseitige Lage von \(g\) und \(h\).", 3),
   ("b", r"Berechne den Abstand von \(g\) und \(h\).", 3)],
  r"Gleiches Vorgehen wie in A3 V1, hier gehen die Zahlen glatt auf.",
  [("a", r"""Die Richtungsvektoren \(""" + V("1","0","1") + r"""\) und \(""" + V("1","2","0") + r"""\)
   sind keine Vielfachen, also nicht parallel.<br>
   Gleichsetzen liefert das System
   \[2+r=s,\qquad 1=1+2s,\qquad r=1.\]
   Aus der zweiten Zeile folgt \(s=0\), damit aus der ersten \(r=-2\).
   Die dritte Zeile verlangt aber \(r=1\). Widerspruch, kein Schnittpunkt.
   Die Geraden sind <strong>windschief</strong>."""),
   ("b", r"""\[\vec n=\vec u\times\vec v=""" + V("-2","1","2") + r""",\qquad |\vec n|=\sqrt{4+1+4}=3.\]
   \[\vec{AB}=""" + V("0-2","1-1","1-0") + r"""=""" + V("-2","0","1") + r""",\qquad
   \vec n\cdot\vec{AB}=4+0+2=6.\]
   \[d=\frac{6}{3}=2.\]""")],
  None),

A("A3", "A3 V4", "Windschiefe Geraden und beide Lotpunkte", 6,
  r"Gegeben sind \(g:\;\vec x=r\cdot" + V("1","1","0") + r"\) und \(h:\;\vec x=" + V("2","0","1") + r"+s\cdot" + V("0","1","1") + r"\).",
  [("a", r"Untersuche die gegenseitige Lage der Geraden.", 2),
   ("b", r"Bestimme die Endpunkte ihrer kürzesten Verbindungsstrecke und ihren Abstand.", 4)],
  r"""Wenn nicht nur die <em>Zahl</em> (der Abstand), sondern auch die <em>Orte</em> gefragt sind,
  reicht das Spatprodukt nicht. Man braucht den Vektorzug: allgemeiner Punkt auf \(g\),
  allgemeiner Punkt auf \(h\), und die Verbindung muss auf <strong>beiden</strong> Richtungen senkrecht stehen.
  Das sind zwei Gleichungen für zwei Unbekannte.""",
  [("a", r"""Die Richtungen \(""" + V("1","1","0") + r"""\) und \(""" + V("0","1","1") + r"""\) sind nicht parallel.
   Ein Schnittpunkt verlangte \(r=2\) (erste Zeile), \(r=s\) (zweite) und \(0=1+s\) (dritte).
   Aus der dritten folgt \(s=-1\), aus der zweiten also \(r=-1\) — Widerspruch zu \(r=2\).
   Kein Schnittpunkt, also <strong>windschief</strong>."""),
   ("b", r"""Allgemeine Punkte:
   \[G(r\,|\,r\,|\,0)\ \text{auf } g,\qquad H(2\,|\,s\,|\,1+s)\ \text{auf } h.\]
   \[\vec{GH}=""" + V("2-r","s-r","1+s") + r""".\]
   Zwei Orthogonalitätsbedingungen:
   \[\vec{GH}\cdot""" + V("1","1","0") + r"""=(2-r)+(s-r)=2+s-2r=0,\]
   \[\vec{GH}\cdot""" + V("0","1","1") + r"""=(s-r)+(1+s)=1+2s-r=0.\]
   Aus der zweiten Gleichung \(r=1+2s\); eingesetzt in die erste:
   \(2+s-2(1+2s)=-3s=0\), also \(s=0\) und \(r=1\).
   \[G(1\,|\,1\,|\,0),\qquad H(2\,|\,0\,|\,1),\qquad
   \vec{GH}=""" + V("1","-1","1") + r""",\quad d=\sqrt3.\]
   Probe: \(\vec{GH}\) steht wirklich senkrecht auf beiden Richtungsvektoren. \(\checkmark\)""")],
  r"Nur eine der beiden Bedingungen aufstellen. Für zwei Unbekannte braucht man zwei Gleichungen."),

# ══════════════════════════════════════════════════ A4 · Lot und Spiegelung
A("A4", "A4 V1", "Lotfußpunkt und Spiegelpunkt", 6,
  r"Gegeben sind die Ebene \(E:\; x_1+2x_2+2x_3=1\) und der Punkt \(P(3\,|\,4\,|\,4)\).",
  [("a", r"Bestimme den Lotfußpunkt \(F\) von \(P\) auf \(E\).", 3),
   ("b", r"Bestimme den Spiegelpunkt \(P'\) von \(P\) bezüglich \(E\) und gib den Abstand von \(P\) zu \(E\) an.", 3)],
  r"""Standardverfahren: Lotgerade durch \(P\) in Richtung \(\vec n\) aufstellen, in die Ebenengleichung
  einsetzen, Parameter bestimmen. Der Spiegelpunkt liegt genau doppelt so weit —
  am elegantesten über \(\vec{OP'}=2\vec{OF}-\vec{OP}\).""",
  [("a", r"""Lotgerade: \(\vec x=""" + V("3","4","4") + r"""+t\cdot""" + V("1","2","2") + r"""\).
   Einsetzen in \(E\):
   \[(3+t)+2(4+2t)+2(4+2t)=3+t+8+4t+8+4t=19+9t=1\;\Rightarrow\;t=-2.\]
   \[F=""" + V("3","4","4") + r"""-2\cdot""" + V("1","2","2") + r"""=""" + V("1","0","0") + r"""\;\Rightarrow\;F(1\,|\,0\,|\,0).\]"""),
   ("b", r"""\[\vec{OP'}=2\vec{OF}-\vec{OP}=""" + V("2","0","0") + r"""-""" + V("3","4","4") + r"""
   =""" + V("-1","-4","-4") + r"""\;\Rightarrow\;P'(-1\,|\,-4\,|\,-4).\]
   Abstand: \(|\vec n|=\sqrt{1+4+4}=3\), also
   \[d=|t|\cdot|\vec n|=2\cdot 3=6.\]
   Kontrolle über die HNF: \(\dfrac{|3+8+8-1|}{3}=\dfrac{18}{3}=6\). \(\checkmark\)""")],
  r"Den Spiegelpunkt als \(F+\vec{PF}\) statt \(P+2\vec{PF}\) berechnen. Die Formel \(\vec{OP'}=2\vec{OF}-\vec{OP}\) ist sicherer."),

A("A4", "A4 V2", "Lotfußpunkt und Spiegelpunkt", 6,
  r"Gegeben sind die Ebene \(E:\; 2x_1-2x_2+x_3=4\) und der Punkt \(P(8\,|\,-6\,|\,3)\).",
  [("a", r"Bestimme den Lotfußpunkt \(F\) von \(P\) auf \(E\).", 3),
   ("b", r"Bestimme den Spiegelpunkt \(P'\) von \(P\) bezüglich \(E\) und gib den Abstand von \(P\) zu \(E\) an.", 3)],
  r"Gleiches Verfahren wie A4 V1, nur mit negativen Koordinaten.",
  [("a", r"""Lotgerade: \(\vec x=""" + V("8","-6","3") + r"""+t\cdot""" + V("2","-2","1") + r"""\).
   \[2(8+2t)-2(-6-2t)+(3+t)=16+4t+12+4t+3+t=31+9t=4\;\Rightarrow\;t=-3.\]
   \[F=""" + V("8","-6","3") + r"""-3\cdot""" + V("2","-2","1") + r"""=""" + V("2","0","0") + r"""\;\Rightarrow\;F(2\,|\,0\,|\,0).\]"""),
   ("b", r"""\[\vec{OP'}=2\vec{OF}-\vec{OP}=""" + V("4","0","0") + r"""-""" + V("8","-6","3") + r"""
   =""" + V("-4","6","-3") + r"""\;\Rightarrow\;P'(-4\,|\,6\,|\,-3).\]
   \(|\vec n|=\sqrt{4+4+1}=3\), also \(d=|{-3}|\cdot 3=9\).""")],
  r"Bei \(-2\cdot(-6-2t)\) ein Vorzeichen verlieren. Klammern konsequent setzen."),

A("A4", "A4 V3", "Spiegelebene rekonstruieren", 6,
  r"Der Punkt \(P(5\,|\,1\,|\,2)\) wird an einer Ebene \(E\) auf \(P'(-3\,|\,5\,|\,2)\) gespiegelt.",
  [("a", r"Bestimme eine Koordinatengleichung von \(E\). Erläutere dabei die geometrischen Eigenschaften, die du verwendest.", 4),
   ("b", r"Berechne den Abstand von \(P\) zu \(E\).", 2)],
  r"""Das ist eine <strong>Umkehraufgabe</strong>. Zwei Eigenschaften der Spiegelung reichen aus:
  <strong>(1)</strong> \(E\) steht senkrecht auf der Strecke \(PP'\) — der Verbindungsvektor ist also ein
  Normalenvektor. <strong>(2)</strong> \(E\) halbiert die Strecke — der Mittelpunkt liegt in \(E\).
  \(E\) ist genau die Mittelsenkrechtenebene von \(PP'\).""",
  [("a", r"""<strong>Normalenvektor.</strong>
   \[\vec{PP'}=""" + V("-3-5","5-1","2-2") + r"""=""" + V("-8","4","0") + r"""\;\parallel\;""" + V("2","-1","0") + r""".\]
   (Gekürzt durch \(-4\); jedes Vielfache ist als Normalenvektor erlaubt.)<br>
   <strong>Punkt in der Ebene.</strong> Der Mittelpunkt von \(PP'\):
   \[M=\tfrac12\left(""" + V("5","1","2") + r"""+""" + V("-3","5","2") + r"""\right)=""" + V("1","3","2") + r"""\;\Rightarrow\;M(1\,|\,3\,|\,2).\]
   <strong>Gleichung.</strong> Ansatz \(2x_1-x_2=c\), \(M\) einsetzen: \(2\cdot 1-3=-1\).
   \[E:\; 2x_1-x_2=-1.\]
   Probe: \(P\) liefert \(10-1=9\), \(P'\) liefert \(-6-5=-11\) — beide gleich weit von \(-1\) entfernt
   (je 10), und auf entgegengesetzten Seiten. \(\checkmark\)"""),
   ("b", r"""Der Abstand ist die halbe Strecke \(PP'\):
   \[d=\tfrac12\left|""" + V("-8","4","0") + r"""\right|=\tfrac12\sqrt{64+16}=\tfrac12\sqrt{80}=2\sqrt5\approx 4{,}47.\]
   Kontrolle über die HNF mit \(|\vec n|=\sqrt{4+1+0}=\sqrt5\):
   \[d=\frac{|2\cdot 5-1+1|}{\sqrt5}=\frac{10}{\sqrt5}=2\sqrt5.\;\checkmark\]""")],
  r"Die dritte Koordinate: Sie ändert sich nicht, deshalb ist die dritte Komponente des Normalenvektors null und \(x_3\) kommt in der Gleichung gar nicht vor."),

# ══════════════════════════════════════════════════ A5 · Vierfeldertafel
A("A5", "A5 V2", "Vierfeldertafel und Unabhängigkeit", 6,
  r"""In einem Fahrradverleih sind 40 % der Räder E-Bikes (Ereignis \(E\)). 25 % aller Räder haben
  einen Bremsdefekt (Ereignis \(D\)). Von den E-Bikes haben 10 % einen Bremsdefekt.
  Ein Rad wird zufällig aus dem Bestand ausgewählt.""",
  [("a", r"Stelle die vollständige Vierfeldertafel auf.", 2),
   ("b", r"Aus allen Rädern mit Bremsdefekt wird eines zufällig ausgewählt. Berechne die Wahrscheinlichkeit, dass es ein E-Bike ist.", 2),
   ("c", r"Prüfe, ob \(E\) und \(D\) stochastisch unabhängig sind.", 2)],
  r"""Aufpassen bei „Von den E-Bikes haben 10 % …“ — das ist eine <strong>bedingte</strong>
  Wahrscheinlichkeit \(P_E(D)=0{,}10\), kein Feld der Tafel. Das Innenfeld bekommt man erst
  durch Multiplikation: \(P(E\cap D)=P(E)\cdot P_E(D)\).""",
  [("a", r"""\[P(E\cap D)=0{,}4\cdot 0{,}10=0{,}04.\]
   Der Rest ergibt sich durch Ergänzen auf die Ränder \(P(E)=0{,}4\) und \(P(D)=0{,}25\):
   <table class="vft"><tr><th></th><th>\(D\)</th><th>\(\bar D\)</th><th>Summe</th></tr>
   <tr><th>\(E\)</th><td>0,04</td><td>0,36</td><td>0,40</td></tr>
   <tr><th>\(\bar E\)</th><td>0,21</td><td>0,39</td><td>0,60</td></tr>
   <tr><th>Summe</th><td>0,25</td><td>0,75</td><td>1,00</td></tr></table>"""),
   ("b", r"""Gefragt ist \(P_D(E)\) — die Bedingung ist „hat Bremsdefekt“:
   \[P_D(E)=\frac{P(E\cap D)}{P(D)}=\frac{0{,}04}{0{,}25}=0{,}16.\]
   In Worten: 16 % der defekten Räder sind E-Bikes."""),
   ("c", r"""Unabhängigkeitsprobe:
   \[P(E)\cdot P(D)=0{,}4\cdot 0{,}25=0{,}10\neq 0{,}04=P(E\cap D).\]
   Die Ereignisse sind also <strong>abhängig</strong>.<br>
   Gleichwertig: \(P_E(D)=0{,}10\neq 0{,}25=P(D)\) — zu wissen, dass es ein E-Bike ist,
   verändert die Defektwahrscheinlichkeit.""")],
  r"\(P_D(E)\) und \(P_E(D)\) verwechseln. Hier sind es 0,16 gegen 0,10 — zwei verschiedene Fragen."),

A("A5", "A5 V3", "Unabhängigkeit als Bedingung", 6,
  r"""Aus 100 Personen wird eine zufällig ausgewählt. 40 Personen nutzen den Bus (\(B\)),
  30 besuchen die Musikschule (\(M\)). Genau \(a\) Personen gehören zu beiden Gruppen.""",
  [("a", r"Bestimme \(a\) so, dass \(B\) und \(M\) stochastisch unabhängig sind.", 2),
   ("b", r"Stelle für diesen Fall die vollständige Vierfeldertafel mit absoluten Häufigkeiten auf.", 2),
   ("c", r"Tatsächlich gehören 18 Personen zu beiden Gruppen. Berechne die bedingte Wahrscheinlichkeit \(P_M(B)\) und entscheide über die Unabhängigkeit.", 2)],
  r"""Die Aufgabe dreht die übliche Richtung um: Statt Unabhängigkeit zu <em>prüfen</em>,
  wird sie erst <em>hergestellt</em> und danach am echten Wert geprüft.""",
  [("a", r"""Unabhängigkeit bedeutet \(P(B\cap M)=P(B)\cdot P(M)\):
   \[\frac{a}{100}=0{,}4\cdot 0{,}3=0{,}12\;\Rightarrow\;a=12.\]"""),
   ("b", r"""<table class="vft"><tr><th></th><th>\(M\)</th><th>\(\bar M\)</th><th>Summe</th></tr>
   <tr><th>\(B\)</th><td>12</td><td>28</td><td>40</td></tr>
   <tr><th>\(\bar B\)</th><td>18</td><td>42</td><td>60</td></tr>
   <tr><th>Summe</th><td>30</td><td>70</td><td>100</td></tr></table>"""),
   ("c", r"""Mit \(a=18\):
   \[P_M(B)=\frac{18}{30}=0{,}6.\]
   Vergleich mit \(P(B)=0{,}4\): Die beiden Werte sind verschieden, also sind \(B\) und \(M\)
   <strong>abhängig</strong>. Unter den Musikschülern ist der Busanteil deutlich höher
   als in der Gesamtgruppe.""")],
  None),

A("A5", "A5 V4", "Vertauschte Bedingungen beim Ticketverkauf", 6,
  r"""Von 200 verkauften Tickets wurden 120 online gebucht (\(O\)). 80 Tickets sind ermäßigt (\(R\)).
  60 Tickets sind sowohl online gebucht als auch ermäßigt. Ein verkauftes Ticket wird zufällig ausgewählt.""",
  [("a", r"Erstelle eine vollständige Vierfeldertafel mit absoluten Häufigkeiten.", 2),
   ("b", r"Berechne \(P_R(O)\) und \(P_O(R)\). Erläutere, auf welche Gruppe sich jeweils die Wahrscheinlichkeit bezieht.", 2),
   ("c", r"Prüfe \(O\) und \(R\) auf stochastische Unabhängigkeit.", 2)],
  r"""Kernpunkt der Aufgabe: \(P_R(O)\) und \(P_O(R)\) haben denselben Zähler, aber verschiedene Nenner.
  Der Nenner ist immer die <strong>Bedingung</strong> — also die Gruppe, über die geredet wird.""",
  [("a", r"""<table class="vft"><tr><th></th><th>\(R\)</th><th>\(\bar R\)</th><th>Summe</th></tr>
   <tr><th>\(O\)</th><td>60</td><td>60</td><td>120</td></tr>
   <tr><th>\(\bar O\)</th><td>20</td><td>60</td><td>80</td></tr>
   <tr><th>Summe</th><td>80</td><td>120</td><td>200</td></tr></table>"""),
   ("b", r"""\[P_R(O)=\frac{60}{80}=0{,}75,\qquad P_O(R)=\frac{60}{120}=0{,}5.\]
   <strong>Bezug:</strong> \(P_R(O)=0{,}75\) — von den <em>ermäßigten</em> Tickets wurden 75 % online gebucht.<br>
   \(P_O(R)=0{,}5\) — von den <em>online gebuchten</em> Tickets sind 50 % ermäßigt.
   Gleicher Schnitt, verschiedene Grundgesamtheit."""),
   ("c", r"""\[P(O\cap R)=\frac{60}{200}=0{,}3,\qquad
   P(O)\cdot P(R)=0{,}6\cdot 0{,}4=0{,}24.\]
   \(0{,}3\neq 0{,}24\), also <strong>abhängig</strong>.""")],
  None),

# ══════════════════════════════════════════════════ A6 · Kenngrößen
A("A6", "A6 V1", "Empirische Kenngrößen", 6,
  r"Gegeben ist die Urliste 2; 4; 5; 6; 8.",
  [("a", r"Berechne Mittelwert, empirische Varianz und empirische Standardabweichung.", 3),
   ("b", r"Welcher Anteil der Werte liegt im Intervall \([\bar x-s;\;\bar x+s]\)?", 1),
   ("c", r"Alle Werte werden um 10 erhöht. Gib Mittelwert und Standardabweichung der neuen Liste an und begründe kurz.", 2)],
  r"""Hier wird die empirische Varianz mit Divisor \(n\) verwendet (nicht \(n-1\)).
  Teil c) prüft das Grundverständnis: Verschieben bewegt den Mittelwert mit, lässt die Streuung aber in Ruhe.""",
  [("a", r"""\[\bar x=\frac{2+4+5+6+8}{5}=\frac{25}{5}=5.\]
   Abweichungen: \(-3,\,-1,\,0,\,1,\,3\); Quadrate: \(9,\,1,\,0,\,1,\,9\).
   \[v=\frac{9+1+0+1+9}{5}=\frac{20}{5}=4,\qquad s=\sqrt4=2.\]"""),
   ("b", r"""Intervall \([5-2;\;5+2]=[3;\,7]\). Darin liegen 4, 5 und 6 — also 3 von 5 Werten:
   \[\frac{3}{5}=60\,\%.\]"""),
   ("c", r"""\[\bar x_{\text{neu}}=15,\qquad s_{\text{neu}}=2.\]
   <strong>Begründung:</strong> Wird jeder Wert um 10 erhöht, wächst auch der Mittelwert um 10.
   Die Abstände \(x_i-\bar x\) bleiben dabei unverändert — und nur die gehen in die Varianz ein.
   Deshalb ändert sich die Streuung nicht.""")],
  r"Die Wurzel am Schluss vergessen und \(v\) und \(s\) gleichsetzen."),

A("A6", "A6 V3", "Gleicher Mittelwert, verschiedene Streuung", 6,
  r"""Gegeben sind die Messreihen \(A\): 2; 2; 6; 6 und \(B\): 0; 4; 4; 8.
  Verwende für die empirische Varianz den Divisor \(n\).""",
  [("a", r"Berechne Mittelwert, empirische Varianz und Standardabweichung von \(A\).", 3),
   ("b", r"Berechne Mittelwert und Varianz von \(B\) und vergleiche die Streuung der Messreihen.", 2),
   ("c", r"Beurteile die Aussage: „Bei gleichem Mittelwert müssen auch die Standardabweichungen gleich sein.“", 1)],
  r"""Die beiden Reihen sind mit Absicht so gebaut, dass sie denselben Mittelwert haben.
  Sie sind damit ein fertiges <strong>Gegenbeispiel</strong> für die Behauptung in c).""",
  [("a", r"""\[\bar x_A=\frac{2+2+6+6}{4}=4.\]
   Abweichungen: \(-2,\,-2,\,2,\,2\); Quadrate je 4.
   \[v_A=\frac{4+4+4+4}{4}=4,\qquad s_A=2.\]"""),
   ("b", r"""\[\bar x_B=\frac{0+4+4+8}{4}=4.\]
   Abweichungen: \(-4,\,0,\,0,\,4\); Quadrate: \(16,\,0,\,0,\,16\).
   \[v_B=\frac{32}{4}=8,\qquad s_B=\sqrt8=2\sqrt2\approx 2{,}83.\]
   <strong>Vergleich:</strong> Gleicher Mittelwert 4, aber \(s_B>s_A\). Die Reihe \(B\) streut stärker
   — ihre Werte liegen weiter vom Mittelwert entfernt."""),
   ("c", r"""Die Aussage ist <strong>falsch</strong>. \(A\) und \(B\) haben denselben Mittelwert 4,
   aber verschiedene Standardabweichungen (2 gegen \(2\sqrt2\)).
   Mittelwert und Streuung beschreiben zwei verschiedene Eigenschaften einer Datenreihe:
   der eine die Lage, die andere die Breite.""")],
  None),

A("A6", "A6 V4", "Fehlender Messwert und lineare Umrechnung", 6,
  r"Die Messreihe 2; 4; 6; \(k\) besitzt den Mittelwert 5. Für die Varianz wird durch \(n\) geteilt.",
  [("a", r"Bestimme \(k\).", 1),
   ("b", r"Berechne die empirische Varianz und Standardabweichung der vollständigen Messreihe.", 3),
   ("c", r"Jeder Messwert \(x\) wird durch \(y=1-2x\) ersetzt. Bestimme den neuen Mittelwert und die neue Standardabweichung. Begründe ohne erneute Berechnung aller Abweichungsquadrate.", 2)],
  r"""Teil c) ist die allgemeine Regel hinter A6 V1 c): Bei \(y=mx+b\) gilt
  \(\bar y=m\bar x+b\) und \(s_y=|m|\cdot s_x\). Der <strong>Betrag</strong> ist wichtig —
  eine Standardabweichung kann nie negativ sein.""",
  [("a", r"""\[\bar x=\frac{2+4+6+k}{4}=5\;\Rightarrow\;12+k=20\;\Rightarrow\;k=8.\]"""),
   ("b", r"""Messreihe 2; 4; 6; 8 mit \(\bar x=5\).
   Abweichungen: \(-3,\,-1,\,1,\,3\); Quadrate: \(9,\,1,\,1,\,9\).
   \[v=\frac{9+1+1+9}{4}=\frac{20}{4}=5,\qquad s=\sqrt5\approx 2{,}24.\]"""),
   ("c", r"""\[\bar y=1-2\cdot 5=-9.\]
   \[s_y=|-2|\cdot s_x=2\sqrt5\approx 4{,}47.\]
   <strong>Begründung:</strong> Die Verschiebung um \(+1\) bewegt alle Werte und den Mittelwert
   gleich weit, ändert also keine Abweichung. Der Faktor \(-2\) verdoppelt jede Abweichung
   dem Betrag nach; das Vorzeichen spiegelt nur die Reihenfolge und fällt beim Quadrieren weg.""")],
  r"In c) \(s_y=-2\sqrt5\) angeben. Eine Standardabweichung ist immer \(\ge 0\)."),

# ══════════════════════════════════════════════════ A7 · Simulation
A("A7", "A7 V1", "Simulation beschreiben", 6,
  r"""Eine Basketballspielerin trifft beim Freiwurf mit der Wahrscheinlichkeit 75 %. Die zehn Würfe
  werden als unabhängig betrachtet, die Trefferwahrscheinlichkeit ist bei jedem Wurf gleich.
  Gesucht ist die Wahrscheinlichkeit, bei zehn Würfen mindestens acht Treffer zu erzielen.""",
  [("a", r"Beschreibe eine Simulation mit einem Zufallszahlengenerator, mit der man diese Wahrscheinlichkeit schätzen kann. Nenne Zufallsgerät, Zuordnung, einen Durchgang und die Auswertung.", 4),
   ("b", r"Erkläre, warum ein normaler Spielwürfel für 75 % nicht direkt geeignet ist, und wie man ihn trotzdem nutzen könnte.", 2)],
  r"""Jede Simulationsbeschreibung besteht aus denselben <strong>vier Zeilen</strong>:
  Zufallsgerät — Zuordnung — ein Durchgang — Wiederholung und Auswertung.
  Wichtig ist der Unterschied zwischen einem <em>Durchgang</em> (hier: 10 Würfe) und einer
  <em>Wiederholung</em> (der ganze Durchgang noch einmal).""",
  [("a", r"""<strong>1. Zufallsgerät.</strong> Gleichverteilte ganze Zufallszahlen von 1 bis 4
   (am WTR z. B. <code>RanInt#(1,4)</code>), unabhängig erzeugt.<br>
   <strong>2. Zuordnung.</strong> 1, 2, 3 bedeuten „Treffer“, 4 bedeutet „daneben“.
   Damit ist die Trefferwahrscheinlichkeit \(\tfrac34=75\,\%\).<br>
   <strong>3. Ein Durchgang.</strong> Zehn Zufallszahlen erzeugen und die Treffer zählen.
   Ein Durchgang entspricht einer Serie von zehn Freiwürfen.<br>
   <strong>4. Wiederholung und Auswertung.</strong> Viele Durchgänge, z. B. 100.
   Zählen, in wie vielen Durchgängen mindestens 8 Treffer auftraten.
   Der Schätzwert ist
   \[\hat p=\frac{\text{Anzahl der Durchgänge mit mindestens 8 Treffern}}{\text{Anzahl aller Durchgänge}}.\]"""),
   ("b", r"""Ein Würfel liefert sechs gleich wahrscheinliche Ergebnisse. Jede damit direkt
   darstellbare Wahrscheinlichkeit hat die Form \(\tfrac k6\). Aber
   \[\tfrac34\neq\tfrac k6\quad\text{für jedes ganze }k,\]
   denn \(\tfrac34\cdot 6=4{,}5\) ist keine ganze Zahl.<br>
   <strong>Weg 1 (Verwerfen).</strong> Würfeln; bei 5 oder 6 wird der Wurf verworfen und neu gewürfelt.
   Von den verbleibenden Zahlen 1 bis 4 zählen 1, 2, 3 als Treffer — das ergibt genau \(\tfrac34\).<br>
   <strong>Weg 2 (zwei Würfe).</strong> Zweimal würfeln und nur auf gerade/ungerade achten.
   Die vier Kombinationen gg, gu, ug, uu haben je die Wahrscheinlichkeit \(\tfrac14\).
   Man erklärt gg zum Fehlwurf und die anderen drei zum Treffer.""")],
  r"Einen Durchgang mit einer Wiederholung verwechseln: „10 Durchgänge“ statt „ein Durchgang aus 10 Zahlen“."),

A("A7", "A7 V2", "Simulation beschreiben und auswerten", 6,
  r"""In einem Kurs sind 25 Personen. Gesucht ist die Wahrscheinlichkeit, dass mindestens zwei am
  selben Tag Geburtstag haben. Modellannahme: 365 Tage, jeder Tag gleich wahrscheinlich,
  die Geburtstage sind voneinander unabhängig.""",
  [("a", r"Beschreibe eine Simulation mit einem Zufallszahlengenerator, mit der man diese Wahrscheinlichkeit schätzen kann.", 4),
   ("b", r"Eine Simulation mit 100 Durchgängen lieferte 54 Durchgänge mit mindestens einem doppelten Geburtstag. Gib den Schätzwert an und erläutere, was sich mit 1000 Durchgängen ändert und was nicht.", 2)],
  r"""Klassisches Geburtstagsproblem. Auch hier gilt das Vier-Zeilen-Schema.
  Teil b) prüft, ob man versteht, was mehr Durchgänge bewirken — und was nicht.""",
  [("a", r"""<strong>1. Zufallsgerät.</strong> Gleichverteilte ganze Zufallszahlen von 1 bis 365,
   unabhängig erzeugt. Jede Zahl steht für einen Kalendertag.<br>
   <strong>2. Zuordnung.</strong> Eine Zufallszahl ist der Geburtstag einer Person.<br>
   <strong>3. Ein Durchgang.</strong> 25 Zufallszahlen erzeugen (ein Kurs).
   Der Durchgang gilt als <em>Treffer</em>, wenn mindestens eine Zahl mindestens zweimal vorkommt.<br>
   <strong>4. Wiederholung und Auswertung.</strong> Viele Durchgänge, den Anteil der Treffer bilden."""),
   ("b", r"""\[\hat p=\frac{54}{100}=0{,}54.\]
   <strong>Was sich ändert:</strong> Mit 1000 Durchgängen wird die typische Schwankung des
   Schätzwerts kleiner. Wiederholt man die Simulation mehrfach, liegen die Ergebnisse enger beieinander.<br>
   <strong>Was sich nicht ändert:</strong> Es ist nicht garantiert, dass eine einzelne neue Schätzung
   näher am wahren Wert liegt. Eine Simulation bleibt zufällig. Der exakte Wert beträgt
   \[p=1-\frac{365}{365}\cdot\frac{364}{365}\cdot\ldots\cdot\frac{341}{365}\approx 0{,}569.\]""")],
  r"„Doppelt“ zu eng lesen. Auch drei gleiche Geburtstage sind ein Treffer — deshalb „mindestens zweimal“."),

A("A7", "A7 V3", "Eine Simulation passend auswerten", 6,
  r"""Ein elektronisches Bauteil ist mit Wahrscheinlichkeit 0,3 defekt. Die Zustände verschiedener
  Bauteile werden als unabhängig modelliert. Gesucht ist die Wahrscheinlichkeit, dass in einer
  Gruppe aus vier Bauteilen mindestens eines defekt ist.""",
  [("a", r"Beschreibe eine passende Simulation mit gleichverteilten ganzzahligen Zufallszahlen. Lege Zuordnung, einen Durchgang und die Auswertung fest.", 3),
   ("b", r"Gib einen Term für die exakte Wahrscheinlichkeit an; berechne keinen Dezimalwert.", 1),
   ("c", r"Ein Schüler simuliert 1000 einzelne Bauteile und verwendet den Anteil defekter Bauteile als Antwort auf die Frage. Erläutere seinen Fehler und korrigiere die Auswertung.", 2)],
  r"""Der Kern der Aufgabe steckt in c): Der Schüler schätzt eine richtige Zahl —
  nur leider die falsche. Er schätzt \(P(\text{Bauteil defekt})=0{,}3\), gefragt war aber
  eine Aussage über <strong>Vierergruppen</strong>.""",
  [("a", r"""<strong>Zufallsgerät und Zuordnung.</strong> Zahlen 1 bis 10, unabhängig erzeugt.
   1, 2, 3 bedeuten „defekt“ (das sind \(\tfrac{3}{10}=0{,}3\)), 4 bis 10 „in Ordnung“.<br>
   <strong>Ein Durchgang.</strong> Vier Zufallszahlen — eine Vierergruppe.
   Treffer, wenn mindestens eine Zahl aus \(\{1;2;3\}\) dabei ist.<br>
   <strong>Auswertung.</strong> Viele Durchgänge, Schätzwert
   \(\hat p=\dfrac{\text{Trefferzahl}}{\text{Anzahl der Durchgänge}}\)."""),
   ("b", r"""Über das Gegenereignis „kein Bauteil defekt“:
   \[P(\text{mindestens eines defekt})=1-0{,}7^4.\]"""),
   ("c", r"""<strong>Der Fehler.</strong> Der Anteil defekter Einzelteile unter 1000 Bauteilen schätzt
   \(P(\text{ein Bauteil ist defekt})=0{,}3\). Gefragt war aber die Wahrscheinlichkeit, dass in einer
   <em>Gruppe aus vier</em> Bauteilen mindestens eines defekt ist — ein Ereignis auf der Ebene der Gruppe,
   nicht des Einzelteils.<br>
   <strong>Korrektur.</strong> Seine 1000 Zahlen sind nicht verloren: Er fasst sie zu 250 Vierergruppen
   zusammen und zählt, in wie vielen Gruppen mindestens ein defektes Teil vorkommt.
   Der Anteil dieser Gruppen an den 250 ist der gesuchte Schätzwert (rund 0,76).""")],
  None),

A("A7", "A7 V4", "Ziehen ohne Zurücklegen simulieren", 6,
  r"""Eine Urne enthält drei rote und zwei blaue Kugeln. Zwei Kugeln werden zufällig ohne Zurücklegen
  gezogen. Gesucht ist die Wahrscheinlichkeit für zwei rote Kugeln.""",
  [("a", r"Beschreibe eine Simulation mit gleichverteilten ganzzahligen Zufallszahlen, die das Ziehen ohne Zurücklegen korrekt nachbildet.", 4),
   ("b", r"Ein Schüler erzeugt pro Durchgang zwei unabhängige Zahlen aus 1 bis 5 und wertet 1, 2 und 3 als rot. Erkläre, welches andere Experiment er simuliert, und berechne die korrekte Wahrscheinlichkeit für die ursprüngliche Aufgabe.", 2)],
  r"""Der entscheidende Punkt: Ein Zufallszahlengenerator zieht immer <em>mit</em> Zurücklegen.
  „Ohne Zurücklegen“ muss man von Hand erzwingen — indem man dieselbe <strong>Kugelnummer</strong>
  ausschließt. Nicht dieselbe Farbe! Zwei rote Kugeln nacheinander sind ja gerade erlaubt.""",
  [("a", r"""<strong>Kennzeichnung.</strong> Die fünf Kugeln einzeln nummerieren:
   1, 2, 3 sind die roten, 4 und 5 die blauen.<br>
   <strong>Erste Ziehung.</strong> Eine Zufallszahl aus 1 bis 5.<br>
   <strong>Zweite Ziehung.</strong> Wieder eine Zufallszahl aus 1 bis 5. Ist es dieselbe
   <em>Nummer</em> wie eben, wird sie verworfen und neu gezogen — solange, bis eine andere Nummer erscheint.
   Damit ist die erste Kugel wirklich aus der Urne.<br>
   <strong>Treffer und Auswertung.</strong> Ein Durchgang besteht aus zwei verschiedenen Nummern.
   Treffer, wenn beide höchstens 3 sind. Viele Durchgänge, Anteil der Treffer bilden."""),
   ("b", r"""<strong>Was er simuliert.</strong> Ohne den Ausschluss kann dieselbe Kugel zweimal kommen.
   Er simuliert also Ziehen <strong>mit</strong> Zurücklegen, mit der Wahrscheinlichkeit
   \[\left(\tfrac35\right)^2=\tfrac{9}{25}=0{,}36.\]
   <strong>Richtiger Wert.</strong> Ohne Zurücklegen ändert sich die Urne nach der ersten Ziehung:
   \[P(\text{zwei rote})=\frac35\cdot\frac24=\frac{6}{20}=\frac{3}{10}=0{,}3.\]""")],
  r"Dieselbe <em>Farbe</em> statt derselben <em>Nummer</em> ausschließen. Dann wäre „zwei rote“ unmöglich."),

# ══════════════════════════════════════════════════ A8 · Ereignismengen
A("A8", "A8 V1", "Ereignisse verknüpfen", 5,
  r"""Ein fairer Würfel wird einmal geworfen, \(\Omega=\{1;2;3;4;5;6\}\).
  \(E\): „gerade Augenzahl“, \(F\): „Augenzahl größer als 3“, \(G\): „Primzahl“.""",
  [("a", r"Gib \(E\cap F\), \(E\cup G\) und \(E\setminus F\) als Mengen an.", 2),
   ("b", r"Beschreibe das Ereignis \(\bar F\cap G\) in Worten und berechne seine Wahrscheinlichkeit.", 2),
   ("c", r"Berechne \(P(E\cup F)\) mit dem Additionssatz.", 1)],
  r"""Erst die drei Mengen konkret hinschreiben, dann wird alles Weitere zum Abzählen:
  \(E=\{2;4;6\}\), \(F=\{4;5;6\}\), \(G=\{2;3;5\}\).""",
  [("a", r"""\[E\cap F=\{4;6\}\quad\text{(gerade und größer als 3)}\]
   \[E\cup G=\{2;3;4;5;6\}\quad\text{(gerade oder prim)}\]
   \[E\setminus F=\{2\}\quad\text{(gerade, aber nicht größer als 3)}\]"""),
   ("b", r"""\(\bar F=\{1;2;3\}\) sind die Augenzahlen höchstens 3. Also
   \[\bar F\cap G=\{2;3\}.\]
   <strong>In Worten:</strong> „Die Augenzahl ist eine Primzahl, die höchstens 3 ist.“
   \[P(\bar F\cap G)=\frac{2}{6}=\frac13.\]"""),
   ("c", r"""\[P(E\cup F)=P(E)+P(F)-P(E\cap F)=\frac36+\frac36-\frac26=\frac46=\frac23.\]
   Der Abzug ist nötig, weil 4 und 6 sonst doppelt gezählt würden.""")],
  r"Bei \(E\setminus F\) die Reihenfolge verwechseln: \(F\setminus E=\{5\}\) ist etwas anderes."),

A("A8", "A8 V2", "Ereignisse verknüpfen und darstellen", 5,
  r"""Aus acht Karten mit den Zahlen 1 bis 8 wird eine gezogen, jede Karte mit derselben
  Wahrscheinlichkeit. \(E=\{1;2;3;4\}\), \(F=\{2;4;6;8\}\), \(G=\{3;4;5\}\).""",
  [("a", r"Gib alle Elemente an von (1) \(E\cup F\), (2) \(E\cap(F\cup G)\), (3) \(E\setminus(F\cup G)\).", 2),
   ("b", r"Stelle die Mengen \(\{4\}\) und \(\{6;8\}\) mit \(E\), \(F\), \(G\) und den Zeichen \(\cup\), \(\cap\), \(\setminus\) dar.", 2),
   ("c", r"Berechne \(P(E\cup F)\).", 1)],
  r"""Teil b) geht in die umgekehrte Richtung: nicht Mengen ausrechnen, sondern einen
  passenden Ausdruck <em>konstruieren</em>. Dabei sind mehrere richtige Antworten möglich.""",
  [("a", r"""Zuerst \(F\cup G=\{2;3;4;5;6;8\}\).
   \[(1)\;E\cup F=\{1;2;3;4;6;8\}\]
   \[(2)\;E\cap(F\cup G)=\{2;3;4\}\]
   \[(3)\;E\setminus(F\cup G)=\{1\}\]"""),
   ("b", r"""\[\{4\}=E\cap F\cap G\]
   Die 4 ist die einzige Zahl, die in allen drei Mengen vorkommt.
   Gleichwertig ist auch \(F\cap G\), denn \(F\cap G=\{4\}\) bereits allein.
   \[\{6;8\}=F\setminus E\]
   Die geraden Zahlen, die nicht zu \(E\) gehören."""),
   ("c", r"""\(E\cup F\) hat 6 Elemente:
   \[P(E\cup F)=\frac68=\frac34.\]""")],
  None),

A("A8", "A8 V3", "Teilbarkeit und Ereignismengen", 5,
  r"""Aus zwölf Karten mit den Zahlen 1 bis 12 wird eine zufällig gezogen; jede Karte ist gleich
  wahrscheinlich. \(E\): „Die Zahl ist gerade“, \(F\): „Die Zahl ist durch 3 teilbar“,
  \(G\): „Die Zahl ist größer als 8“.""",
  [("a", r"Gib \(E\cap F\) und \(E\setminus(F\cup G)\) als Mengen an.", 2),
   ("b", r"Bestimme die Wahrscheinlichkeit, dass genau eines der Ereignisse \(E\) und \(F\) eintritt. Gib die zugehörige Ergebnismenge an.", 2),
   ("c", r"Beschreibe \(\bar E\cap\bar F\) in Worten.", 1)],
  r"""Das Wort <strong>„genau eines“</strong> ist der Knackpunkt: gemeint ist
  \((E\setminus F)\cup(F\setminus E)\) — das eine ohne das andere, in beide Richtungen.
  Das ist <em>nicht</em> \(E\cup F\) (da wäre der Schnitt dabei).""",
  [("a", r"""Die Mengen: \(E=\{2;4;6;8;10;12\}\), \(F=\{3;6;9;12\}\), \(G=\{9;10;11;12\}\).
   \[E\cap F=\{6;12\}\]
   \(F\cup G=\{3;6;9;10;11;12\}\), also
   \[E\setminus(F\cup G)=\{2;4;8\}.\]"""),
   ("b", r"""„Genau eines“ bedeutet \((E\setminus F)\cup(F\setminus E)\):
   \[E\setminus F=\{2;4;8;10\},\qquad F\setminus E=\{3;9\}.\]
   \[\text{Ergebnismenge}=\{2;3;4;8;9;10\},\qquad P=\frac{6}{12}=\frac12.\]"""),
   ("c", r"""\(\bar E\cap\bar F\) heißt: weder gerade noch durch 3 teilbar.
   <strong>In Worten:</strong> „Die gezogene Zahl ist weder durch 2 noch durch 3 teilbar.“
   Konkret sind das \(\{1;5;7;11\}\).""")],
  r"„Genau eines“ als \(E\cup F\) lesen. Dann kämen 6 und 12 fälschlich dazu."),

print(f"{len(AUFGABEN)} Aufgaben")
json.dump(AUFGABEN, open('aufgaben.json','w'), ensure_ascii=False, indent=1)

# ═════════════════════════════════════════════════════════════════ HTML-Ausgabe
BLOECKE = {
    "A1": "Abstand Punkt–Ebene",
    "A2": "Abstand Punkt–Gerade",
    "A3": "Lage und Abstand zweier Geraden",
    "A4": "Lot und Spiegelung",
    "A5": "Vierfeldertafel und Unabhängigkeit",
    "A6": "Empirische Kenngrößen",
    "A7": "Simulationen beschreiben",
    "A8": "Ereignisse als Mengen",
}

CSS = r"""
:root{
  --bg:#f4f1ea; --paper:#fffdf8; --ink:#23201c; --mute:#6d675e;
  --line:#ddd6c9; --accent:#3a5a78; --amber:#c9821a; --ok:#2e8b57;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--serif);
     font-size:17px;line-height:1.6;-webkit-text-size-adjust:100%}
.wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}

header.top{background:var(--accent);color:#fff;padding:38px 0 30px;margin-bottom:26px}
header.top .wrap{padding-bottom:0}
header.top h1{font-size:1.85rem;line-height:1.2;margin:0 0 6px;font-weight:600}
header.top p{margin:0;opacity:.88;font-size:.98rem}
header.top .kurs{font-family:var(--sans);font-size:.78rem;letter-spacing:.09em;
     text-transform:uppercase;opacity:.75;margin-bottom:10px}

nav.blocks{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 30px}
nav.blocks a{font-family:var(--sans);font-size:.8rem;text-decoration:none;
     background:var(--paper);border:1px solid var(--line);border-radius:999px;
     padding:5px 13px;color:var(--accent)}
nav.blocks a:hover{background:var(--accent);color:#fff;border-color:var(--accent)}

.intro{background:var(--paper);border:1px solid var(--line);border-radius:10px;
     padding:16px 20px;margin-bottom:34px;font-size:.96rem;color:var(--mute)}
.intro strong{color:var(--ink)}

h2.block{font-size:1.18rem;margin:44px 0 4px;padding-bottom:7px;
     border-bottom:2px solid var(--accent);scroll-margin-top:14px}
h2.block .kuerzel{font-family:var(--sans);font-size:.72rem;letter-spacing:.1em;
     color:var(--accent);display:block;margin-bottom:3px}

article.aufgabe{background:var(--paper);border:1px solid var(--line);border-radius:10px;
     padding:20px 22px;margin:18px 0}
.kopf{display:flex;flex-wrap:wrap;align-items:baseline;gap:9px;margin-bottom:11px}
.kopf .id{font-family:var(--sans);font-size:.7rem;letter-spacing:.09em;font-weight:700;
     background:var(--accent);color:#fff;border-radius:4px;padding:3px 8px}
.kopf .titel{font-weight:600}
.kopf .be{font-family:var(--sans);font-size:.75rem;color:var(--mute);margin-left:auto}
.kontext{margin:0 0 12px}
ol.teile{margin:0;padding-left:0;list-style:none;counter-reset:t}
ol.teile li{margin:0 0 9px;padding-left:2.1em;position:relative}
ol.teile li .marke{position:absolute;left:0;font-weight:600}
ol.teile li .be{font-family:var(--sans);font-size:.74rem;color:var(--mute);white-space:nowrap}

details.loesung{margin-top:16px;border-top:1px solid var(--line);padding-top:12px}
details.loesung summary{font-family:var(--sans);font-size:.85rem;font-weight:600;
     color:var(--accent);cursor:pointer;list-style:none;display:inline-flex;
     align-items:center;gap:7px;padding:5px 11px;border:1px solid var(--line);
     border-radius:999px;background:var(--bg)}
details.loesung summary::-webkit-details-marker{display:none}
details.loesung summary::before{content:"▸";font-size:.9em;transition:transform .15s}
details[open].loesung summary::before{transform:rotate(90deg)}
details.loesung summary:hover{border-color:var(--accent)}
.lsg{margin-top:14px}
.weg{background:#eef3f7;border-left:3px solid var(--accent);border-radius:0 6px 6px 0;
     padding:11px 15px;margin-bottom:16px;font-size:.95rem}
.weg b{font-family:var(--sans);font-size:.72rem;letter-spacing:.09em;
     text-transform:uppercase;color:var(--accent);display:block;margin-bottom:4px}
.schritt{margin-bottom:15px}
.schritt > .marke{font-weight:600;margin-right:.4em}
.fehler{background:#fdf4e6;border-left:3px solid var(--amber);border-radius:0 6px 6px 0;
     padding:11px 15px;margin-top:16px;font-size:.93rem}
.fehler b{font-family:var(--sans);font-size:.72rem;letter-spacing:.09em;
     text-transform:uppercase;color:var(--amber);display:block;margin-bottom:4px}

table.vft{border-collapse:collapse;margin:10px 0;font-size:.95rem}
table.vft th,table.vft td{border:1px solid var(--line);padding:5px 13px;text-align:center}
table.vft th{background:#eef3f7;font-weight:600}

code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.9em;
     background:#eee9dd;border-radius:3px;padding:1px 5px}
.katex-display{margin:.7em 0;overflow-x:auto;overflow-y:hidden;padding:2px 0}
.katex{font-size:1.04em}

footer{margin-top:60px;padding-top:18px;border-top:1px solid var(--line);
     font-family:var(--sans);font-size:.8rem;color:var(--mute)}
footer a{color:var(--accent)}

@media (max-width:560px){
  body{font-size:16px}
  header.top h1{font-size:1.45rem}
  .kopf .be{margin-left:0;width:100%}
}
@media print{
  body{background:#fff}
  header.top{background:none;color:var(--ink);border-bottom:2px solid var(--accent)}
  nav.blocks,.intro{display:none}
  article.aufgabe{break-inside:avoid;border-color:#bbb}
  details.loesung{display:none}
}
"""

def esc(t):
    return t

def render():
    out = []
    out.append('<!doctype html><html lang="de"><head><meta charset="utf-8">')
    out.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    out.append('<title>Übungen zur 1. Klausur · Mathematik LK Q2.1</title>')
    out.append('<meta name="description" content="24 Übungsaufgaben zu Abständen, '
               'Vierfeldertafel, Kenngrößen, Simulationen und Ereignismengen – mit '
               'ausklappbaren Musterlösungen.">')
    out.append('<link rel="stylesheet" href="vendor/katex/katex.min.css">')
    out.append(f'<style>{CSS}</style></head><body>')

    out.append('<header class="top"><div class="wrap">'
               '<div class="kurs">Mathematik Leistungskurs · Q2.1 · Abitur 2027</div>'
               '<h1>Übungen zur 1. Klausur</h1>'
               '<p>Aufgaben aus dem Aufgabenpool, die es nicht in die Klausur geschafft haben. '
               'Mit vollständigen Musterlösungen zum Ausklappen.</p>'
               '</div></header>')

    out.append('<div class="wrap">')
    out.append('<nav class="blocks">')
    for k, t in BLOECKE.items():
        out.append(f'<a href="#{k}">{k} · {t}</a>')
    out.append('</nav>')

    out.append('<div class="intro"><strong>So arbeitest du damit:</strong> '
               'Aufgabe erst vollständig selbst rechnen, dann die Musterlösung aufklappen. '
               'Die Lösung nennt zuerst den Weg und den Grund für die Verfahrenswahl, '
               'danach die Rechnung Schritt für Schritt. '
               'Der gelbe Kasten am Ende zeigt den Fehler, der bei dieser Aufgabe am häufigsten passiert.<br><br>'
               'Für die empirische Varianz gilt durchgehend der Divisor '
               r'\(n\): \(v=\frac1n\sum (x_i-\bar x)^2\) und \(s=\sqrt v\). '
               'Hilfsmittel sind nicht nötig — alle Ergebnisse sind exakte Brüche oder Wurzeln.'
               '</div>')

    for kuerzel, titel in BLOECKE.items():
        liste = [a for a in AUFGABEN if a["block"] == kuerzel]
        if not liste:
            continue
        out.append(f'<h2 class="block" id="{kuerzel}">'
                   f'<span class="kuerzel">Block {kuerzel}</span>{titel}</h2>')
        for a in liste:
            out.append('<article class="aufgabe">')
            out.append(f'<div class="kopf"><span class="id">{a["kennung"]}</span>'
                       f'<span class="titel">{a["titel"]}</span>'
                       f'<span class="be">{a["be"]} BE</span></div>')
            out.append(f'<p class="kontext">{a["kontext"]}</p>')
            out.append('<ol class="teile">')
            for marke, text, be in a["teile"]:
                m = f'<span class="marke">{marke})</span>' if marke else ''
                pad = '' if marke else ' style="padding-left:0"'
                out.append(f'<li{pad}>{m}{text} <span class="be">({be} BE)</span></li>')
            out.append('</ol>')

            out.append('<details class="loesung"><summary>Musterlösung anzeigen</summary>'
                       '<div class="lsg">')
            out.append(f'<div class="weg"><b>Der Weg</b>{a["weg"]}</div>')
            for marke, text in a["loesung"]:
                m = f'<span class="marke">{marke})</span>' if marke else ''
                out.append(f'<div class="schritt">{m}{text}</div>')
            if a["fehler"]:
                out.append(f'<div class="fehler"><b>Typischer Fehler</b>{a["fehler"]}</div>')
            out.append('</div></details>')
            out.append('</article>')

    gesamt = sum(a["be"] for a in AUFGABEN)
    out.append(f'<footer>{len(AUFGABEN)} Aufgaben · {gesamt} BE · '
               'Mathematik LK Q2.1, Paul-Klee-Gymnasium Overath · '
               'Alle Aufgaben sind eigene Konstruktionen.</footer>')
    out.append('</div>')

    out.append('<script defer src="vendor/katex/katex.min.js"></script>')
    out.append('<script defer src="vendor/katex/contrib/auto-render.min.js"></script>')
    out.append('''<script>
document.addEventListener("DOMContentLoaded",function(){
  renderMathInElement(document.body,{
    delimiters:[
      {left:"\\\\[",right:"\\\\]",display:true},
      {left:"\\\\(",right:"\\\\)",display:false}
    ],
    throwOnError:false
  });
});
</script>''')
    out.append('</body></html>')
    return "\n".join(out)

open('index.html','w').write(render())
print("index.html geschrieben")
