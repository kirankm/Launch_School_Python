from to_do_item import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Can only add Todo objects')

        self._todos.append(todo)

    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)

    def __len__(self):
        return len(self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos.copy()

    def todo_at(self, index):
        return self._todos[index]

    def mark_done_at(self, index):
        self.todo_at(index).done = True

    def mark_undone_at(self, index):
        self.todo_at(index).done = False

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, index):
        self._todos.pop(index)

    def for_each(self, call_back_fn):
        for todo in self._todos:
            call_back_fn(todo)

    def select(self, filter_fn):
        new_to_do = TodoList(self.title)
        selected_todos = [todo for todo in self._todos if filter_fn(todo)]
        for todo in selected_todos:
            new_to_do.add(todo)
        return new_to_do
    
    def find_by_title(self, search_term):
        search_fn = lambda to_do: to_do.title == search_term
        selected_todo = self.select(search_fn)
        return selected_todo.todo_at(0)
    
    def done_todos(self):
        return self.select(lambda x:x.done)
    
    def undone_todos(self):
        return self.select(lambda x:not(x.done))
    
    def mark_done(self, title):
        selected_todo = self.find_by_title(title)
        selected_todo.done = True

    def mark_all_done(self):
        def mark_done(to_do):
            to_do.done = True
        self.for_each(mark_done)

    def mark_all_undone(self):
        def mark_not_done(to_do):
            to_do.done = False
        self.for_each(mark_not_done)
