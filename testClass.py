import pytest
from class2 import Division, Muliplication

class TestYourClass:
    def setup_method(self, method):
        
        self.Division = Division(10, 2)  
        self.Multiplication = Muliplication(3, 4)  

    def test_multiply(self):
        
        assert self.Multiplication.multiply() == 12  
        assert Muliplication(5, 0).multiply() == 0  
        assert Muliplication(-2, 3).multiply() == -6  

    def test_divide(self):
        
        assert self.Division.divide() == 5 
        assert Division(0, 5).divide() == 0  
        assert Division(-10, 2).divide() == -5  

    def test_divide_by_zero(self):
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Division(10, 0).divide()