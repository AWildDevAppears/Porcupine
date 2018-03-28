Feature: Model Parser
  In order to add entries to my database
  As a user
  I need to ba able to see a form that I can fill in

  Scenario: Input - string
    Given I have an input type of "string"
    Then it should evaluate to
      | field | modifier  | optional | reference | multiple |
      | text  |           | False    |           | False    |

  Scenario: Input - integer
    Given I have an input type of "int"
    Then it should evaluate to
      | field       | modifier  | optional | reference | multiple |
      | numerical   |           | False    |           | False    |

  Scenario: Input - float
    Given I have an input type of "float"
    Then it should evaluate to
      | field       | modifier  | optional | reference | multiple |
      | numerical   | decimal   | False    |           | False    |


  Scenario: Input - boolean
    Given I have an input type of "boolean"
    Then it should evaluate to
      | field   | modifier      | optional | reference | multiple |
      | toggle  |               | False    |           | False    |

  Scenario: Input - boolean optional
    Given I have an input type of "boolean?"
    Then it should evaluate to
      | field   | modifier      | optional  | reference | multiple |
      | toggle  |               | True      |           | False    |

  Scenario: Input - defA reference
    Given I have an input type of "~A"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | reference |               | False     | A         | False    |

  Scenario: Input - defA reference optional
    Given I have an input type of "~A?"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | reference |               | True      | A         | False    |

  Scenario: Input - Array of strings
    Given I have an input type of "array<string>"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | text      |               | False     |           | True     |

  Scenario: Input - Array of relations
    Given I have an input type of "array<~A>"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | reference |               | False     | A         | True     |

  Scenario: Input - Array of floats, optional
    Given I have an input type of "array<float?>"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | numerical | decimal       | True      |           | True     |

  Scenario: Input - radio buttons
    Given I have an input type of "radio<a, b, c>"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | radio     | a, b, c       | False     |           | False    |

  Scenario: Input - radio buttons -optional
    Given I have an input type of "radio<a, b, c>?"
    Then it should evaluate to
      | field     | modifier      | optional  | reference | multiple |
      | radio     | a, b, c       | True      |           | False    |
