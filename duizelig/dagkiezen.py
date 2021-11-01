#Alwin Wezenbeek 99060433

dag1 = 'maandag'
dag2 = 'dinsdag'
dag3 = 'woensdag'
dag4 = 'donderdag'
dag5 = 'vrijdag'
dag6 = 'zaterdag'
dag7 = 'zondag'

dag_kiezen = input('welke dag kies je? ')
if dag_kiezen == 'maandag':
    print(dag1)
elif dag_kiezen == 'dinsdag':
    print(dag1, dag2)
elif dag_kiezen == 'woensdag':
    print(dag1, dag2, dag3)
elif dag_kiezen == 'donderdag':
    print(dag1, dag2, dag3, dag4)
elif dag_kiezen == 'vrijdag':
    print(dag1, dag2, dag3, dag4, dag5)
elif dag_kiezen == 'zaterdag':
    print(dag1, dag2, dag3, dag4, dag5, dag6)
elif dag_kiezen == 'zondag':
    print(dag1, dag2, dag3, dag4, dag5, dag6, dag7)
