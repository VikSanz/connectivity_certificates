# Algoritmos que generan certificados de k-conexidad

Esta es una implementación desde 0 en Python de los algoritmos:
1) NI-Search de Nagamochi e Ibaraki en [2]
2) Scan-first Search de Cheriyan, Kao y Thurimella en [1]

Estos algoritmos generan certificados de $k$-conexidad en la gráfica que reciben como entrada. Generar certificados de $k$-conexidad permite disminuir la complejidad de tiempo de otros algoritmos en gráficas/redes toda vez que estas gráficas se caracterizan por ser ralas, i. e. tienen un menor número de aristas que la gráfica original, pero prerservan la $k$-conexidad de la misma. 

Grafica.py puede ser importado como modulo para ser usado con la biblioteca de Networkx[https://networkx.org]. Además, se incluye un script que muestra la visualización paso a paso de cada uno de estos algoritmos en una gráfica que el usuario ingrese. 

Este proyecto forma parte de mi tesis de maestría, una vez que presente mi examen, subiré el código completamente comentado.

---

This is an implementation from scratch in Python of the algorithms:
1) NI-Serch by Nagamochi and Ibaraki in [2]
2) Scan-first Search by Cheriyan, Kao and Thurimella in [1]

These algorithms generate $k$-connectivity certificates on the input graph. Generating $ k $-connectivity certificates allows reducing the time complexity of other algorithms in graphs / networks since these graphs are characterized by being sparse, i.e they have fewer edges than the original graph, but preserve its $k$ -connectivity.

Graph.py can be imported as a module to be used with Networkx library [https://networkx.org]. In addition, a script is included that shows the step-by-step visualization of each of these algorithms in a graph that the user enters.

This project is part of my master's thesis, once I present my exam, I will upload the fully commented code.

---
Dies ist eine Implementierung von Grund auf der Algorithmen:
1) NI-Search von Nagamochi und Ibaraki in [2]
2) Scan-first Search von Cheriyan, Kao und Thurimella in [1]

Diese Algorithmen erzeugen $k$-konnektivitäts Zertifikate auf dem Eingabegraphen. Durch die Generierung von $k$-konnektivitäts Zertifikaten kann die Zeitkomplexität anderer Algorithmen in Graphen / Netzwerken reduziert werden, da diese Graphen dadurch gekennzeichnet sind, dass sie dünn besetzt sind, d.h. weniger Kanten haben als der Originalgraph, aber ihre $k$-Konnektivität beibehalten.

Graph.py kann als Modul zur Verwendung mit der Networkx-Bibliothek [https://networkx.org] importiert werden. Darüber hinaus ist ein Skript enthalten, das die schrittweise Visualisierung jedes dieser Algorithmen in einem Diagramm zeigt, das der Benutzer eingibt.
  
Dieses Projekt ist Teil meiner Masterarbeit, sobald ich meine Prüfung vorlege, werde ich den vollständig kommentierten Code hochladen.


[1] Cheriyan, J., Kao, M. Y., & Thurimella, R. (1993). Scan-first search and sparse certificates: an improved parallel algorithm for k-vertex connectivity. SIAM Journal on Computing, 22(1), 157-174.
[2] Nagamochi, H., & Ibaraki, T. (1992). A linear-time algorithm for finding a sparse k-connected spanning subgraph of a k-connected graph. Algorithmica, 7(1), 583-596.
