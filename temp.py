def add_array(A):
    bot = 0
    for x in A:
        bot = bot + x
    return bot
 
A = [1, 2, 3, 4, 5]
total = add_array(A)
print(total)





# for x in range(1, 10):
#     bot = 2 * x
#     print(bot)




def percentage(marks, total_marks):
    percentage = (marks / total_marks) * 100
    return percentage


ans = percentage(85, 100)
print(ans)
