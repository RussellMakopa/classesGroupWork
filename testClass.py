import pytest
#imports here

class TestYourClass:
    def setup_method(self, method):

        self.yourClass = YourClass()
    
    def test_multiply(self):
    
        assert self.yourClass.yourMethod() == 
        assert self.yourClass.yourMethod() ==
        assert self.yourClass.yourMethod() ==

    def test_divide(self):
            
        assert self.yourClass.yourMethod() == 
        assert self.yourClass.yourMethod() ==
        assert self.yourClass.yourMethod() ==

    def test_divByZero(self):
        
        with pytest.raises(ZeroDivisionError):
            self.yourClass.yourMethod()
