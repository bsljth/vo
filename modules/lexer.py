from enum import Enum

arithmeticOperators: list[str] = ["+", "-", "*", "/", "//", "mod", "+=", "-="]

comparisonOperators: list[str] = ["<", ">", "<=", ">=", "=="]

logicalOperators: list[str] = ["and", "or"]

class TokenType(Enum):
    ADD: str
    MINUS: str
    MULTIPLY: str
    DIVIDE: str
    FLOOR: str
    MOD: str
    LTHAN: str
    GTHAN: str
    
class Token():
    type: TokenType
    value: str
    line: int
    at: int
    
class Literal:
    def __init__(self, value):
        self.value = value

eight = Literal(8)

class UnaryOp:
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    
class USub:
    def __init__(self, op):
        self.op = op
    
neg_eight = UnaryOp(USub(), eight)

class Call:
    def __init__(self, func: function, args: list[str]):
        self.func = func
        self.args = args

class Name:
    def __int__(self, id):
        self.id = id

read = Call(Name("input_int"), [])

class BinOp:
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right
        
class Add:
    def __init__(self, op):
        self.op = op