from superhero_api import SuperHeroAPI, API_KEY

class SuperHeroApp():
    def __init__(self):
        self._s = SuperHeroAPI(API=API_KEY)
        self._status = True
        self._prelude_text = '''Ну привет странник. че забрел? либо иди отседа либо используй команды.
        help - список команд
        compare name name - сравнить по силе двух челиков
        exit -  иди отседа'''
    
    def _set_status(self):
        self._status = False
    
    def run(self):
        print(self._prelude_text)
        while self._status:
            _input = input('Пиши команды либо go отсуда, help для команд: ')
            command = self._parse_command(_input)
            self._command_dispathcer(command)
            
    def _parse_command(self, _input):
        print(_input.strip().split(sep='-', maxsplit=2))
        return _input.strip().lower().split()
    
    def _command_dispathcer(self, command):
        if len(command) <= 1:
            if not command or command[0] == 'exit':
                self._change_status()
            elif command[0] == 'help':
                print(self._prelude_text)
        else:
            action, *arguments = command
            if action == 'compare':
                self._compare_heroes(arguments)

    def _compare_heroes(self, heroes):
        hero_one = self._s.get_hero_stats(heroes[0])
        hero_two = self._s.get_hero_stats(heroes[1])
        power_one, hp_one = int(hero_one['power']), int(hero_one['durability'])
        power_two, hp_two = int(hero_two['power']), int(hero_two['durability'])
        if hp_two - power_one > hp_one - power_two:
            print(f'{heroes[1].title()} победил! Осталось здоровья: {hp_two - power_one}')
        else:
            print(f'{heroes[0].title()} победил! Осталось здоровья: {hp_two - power_one}')
            
if __name__ == '__main__':
    app = SuperHeroApp()
    app.run()
        
