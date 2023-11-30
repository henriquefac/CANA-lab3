import 'dart:math';

void main() {
  List<List<int>> grafo = gerarGrafo(8);

  CaixeiroViajante caixeiro = CaixeiroViajante();
  List<int> melhorRota = caixeiro.encontrarMenorRota(grafo);

  print("Melhor rota final: $melhorRota");
  print(
      "Distância mínima final: ${caixeiro.calcularDistancia(grafo, melhorRota)}");
}

List<List<int>> gerarGrafo(int n) {
  Random random = Random();
  List<List<int>> grafo = List.generate(n, (index) => List<int>.filled(n, 0));

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (i != j) {
        grafo[i][j] = random.nextInt(20) + 1;
      }
    }
  }

  return grafo;
}

class CaixeiroViajante {
  List<int> encontrarMenorRota(List<List<int>> grafo) {
    int n = grafo.length;
    List<int> cidades = List.generate(n, (index) => index);
    List<int> melhorRota = List.from(cidades);
    int menorDistancia = calcularDistancia(grafo, melhorRota);

    int interacao = 1;
    do {
      int distanciaAtual = calcularDistancia(grafo, cidades);
      print("Interação $interacao: Rota = $cidades, Distância = $distanciaAtual");

      if (distanciaAtual < menorDistancia) {
        menorDistancia = distanciaAtual;
        melhorRota.setAll(0, cidades);
      }
      interacao++;
    } while (proxPermut(cidades));

    return melhorRota;
  }

  int calcularDistancia(List<List<int>> grafo, List<int> rota) {
    int distancia = 0;
    for (int i = 0; i < rota.length - 1; i++) {
      distancia += grafo[rota[i]][rota[i + 1]];
    }
    distancia += grafo[rota.last][rota.first];
    return distancia;
  }

  bool proxPermut(List<int> array) {
    int i = array.length - 1;
    while (i > 0 && array[i - 1] >= array[i]) {
      i--;
    }

    if (i <= 0) {
      return false;
    }

    int j = array.length - 1;
    while (array[j] <= array[i - 1]) {
      j--;
    }

    array[i - 1] ^= array[j];
    array[j] ^= array[i - 1];
    array[i - 1] ^= array[j];

    j = array.length - 1;
    while (i < j) {
      array[i] ^= array[j];
      array[j] ^= array[i];
      array[i] ^= array[j];
      i++;
      j--;
    }

    return true;
  }
}