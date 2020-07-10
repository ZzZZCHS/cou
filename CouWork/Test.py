from Player import Player

def main():
    stu = Player('王大锤' )
    stu.nameOut()
    stu._name='hhf'
    stu.nameOut()
    stu.rename('zzf')
    t = Player('骆昊' )
    t.nameOut()

if __name__ == '__main__':
    main()