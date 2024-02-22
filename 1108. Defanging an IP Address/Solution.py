class Solution:
    def defangIPaddr(self, address: str) -> str:
        # for i in range(len(address)):
        #     if address[i] == '.':
        #         new_string = address.replace('.', '[.]')
        # return new_string

        return address.replace('.', '[.]')