Feature: Transformar números com algarismos romanos em números com algarismos arábicos

Scenario: Entender o número I
    Given o número romano "I"
    When quero converter em um número arábico
    Then o resultado é 1

Scenario: Entender o número V
    Given o número romano "V"
    When quero converter em um número arábico
    Then o resultado é 5

Scenario: Entender o número com mais de um simbolo II
    Given o número romano "II"
    When quero converter em um número arábico
    Then o resultado é 2

Scenario: Entender o número com mais de um simbolo VII
    Given o número romano "VII"
    When quero converter em um número arábico
    Then o resultado é 7