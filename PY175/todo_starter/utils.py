def error_for_list_title(title, lists):
    if any([lst['title'] == title for lst in lists]):
        return "List Titles Should be Unique"
    elif not 1 <= len(title) <= 100:
        return "Title length should be between 1 and 100 characters"
    return None

def error_for_todo(title):
    if not 1 <= len(title) <= 100:
        return "Todo length should be between 1 and 100 characters"
    return None

def find_list(list_id, session):
    #print(list_id, session['lists'])
    print("The items are", [lst for lst in session['lists'] if lst['id'] == list_id])
    return next((lst for lst in session['lists'] if lst['id'] == list_id), None)

def find_todo(todo_id, lst):
    return next((todo for todo in lst['todos'] if todo['id'] == todo_id), None)

def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]
    return None

def mark_all_completed(lst):
    for todo in lst['todos']:
        todo['completed'] = True
    return None