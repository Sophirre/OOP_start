from Calculator import Calculator, ScientificCalculator, AccountingCalculator

common = Calculator('common')
science = ScientificCalculator('science')
accounting = AccountingCalculator('accounting')
print('----CommonCalculator----')
print(f"Addiction: {common.operation_chooser('+', 100, 25, 25, 50)}")  # 200
print(f"Subtraction: {common.operation_chooser('-', 340, 20, 40, 80)}")  # 200
print(f"Multiply:  {common.operation_chooser('*', 20, 10)}")  # 200
print(f"Division: {common.operation_chooser('/', 400, 2)}")  # 200

print('----ScientificCalculator----')
print(f"Sin: {science.operation_chooser('sin', 360)}")
print(f"Cos: {science.operation_chooser('cos', 520)}")
print(f"Tan: {science.operation_chooser('tg', 60)}")

print('----AccountingCalculator----')

print(f'Addition: {accounting.operation_chooser("+", 100, 25, 25, 50)}')
print(f'Subtraction: {accounting.operation_chooser("-", 100, 15, 25, 50)}')
print(f'Multiply: {accounting.operation_chooser("*", 100, 25, 25, 50)}')
print(f'Division: {accounting.operation_chooser("/", 100, 25, 25, 50)}')
print(f'Memory: {accounting.results}')
print('----------------------------')