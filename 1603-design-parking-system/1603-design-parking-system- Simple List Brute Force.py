class ParkingSystem:
    # Brute Force Solution
    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        if self.space[carType-1] > 0:
            self.space[carType-1] -= 1
            return True
        else:
            return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)