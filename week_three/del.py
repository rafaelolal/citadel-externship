class Solution:
    def calculate(self, s: str) -> int:
        s = "(" + s.replace(" ", "") + ")"
        l = self.to_array(s)
        post_fix = self.shunting_yard(l)
        result = self.eval_post_fix(post_fix)
        return result

    def eval_post_fix(self, l):
        stack = []
        for item in l:
            if isinstance(item, int):
                stack.append(item)
                continue

            num1 = stack.pop()
            num2 = None
            if stack:
                num2 = stack.pop()
            if num2:
                if item == "-":
                    stack.append(num2-num1)
                else:
                    stack.append(num2+num1)
            else:
                assert item == "-"
                stack.append(-num1)

        return stack[0]

    def shunting_yard(self, l):
        stack = []
        queue = []

        for i in range(len(l)):
            item = l[i]

            if item.isnumeric():
                queue.append(int(item))
                continue

            elif item == "(":
                stack.append(item)

            elif item == ")":
                while stack[-1] != "(":
                    queue.append(stack.pop())

                stack.pop()  # remove extra "("

            else:
                stack.append(item)

        while stack:
            queue.append(stack.pop())

        return queue

    def to_array(self, s):
        items = []
        found_numeric = False
        cur_item = ""
        for char in s:
            if not found_numeric and not char.isnumeric():
                items.append(char)

            elif found_numeric and not char.isnumeric():
                found_numeric = False
                items.append(cur_item)
                cur_item = ""
                items.append(char)

            elif found_numeric and char.isnumeric():
                cur_item += char

            elif char.isnumeric():
                found_numeric = True
                cur_item += char

        if cur_item:
            items.append(cur_item)

        return items


s = Solution()
print(s.calculate("1-(-2)"))
print(s.calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))"))
