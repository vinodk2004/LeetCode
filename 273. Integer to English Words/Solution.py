class Solution:
    def numberToWords(self, num: int) -> str:
        word = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
            10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
            20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
        }

        if num == 0:
            return 'Zero'

        elif num < 20:
            return word[num]

        elif num < 100:
            i = num // 10
            return word[i*10] + ('' if num % 10 == 0 else ' ' + self.numberToWords(num%10))
 
        elif num < 1000:
            i = num // 100
            return word[i] + ' Hundred' +  ('' if num % 100 == 0 else ' '  + self.numberToWords(num%100))

        elif num < 1000000:
            i = num // 1000
            return self.numberToWords(i) + ' Thousand' + ('' if num % 1000 == 0 else ' '  + self.numberToWords(num%1000))

        elif num < 1000000000:
            i = num // 1000000
            return self.numberToWords(i) + ' Million' + ('' if num % 1000000 == 0 else ' '  + self.numberToWords(num%1000000))
        
        else:
            i = num // 1000000000
            return self.numberToWords(i) + ' Billion' + ('' if num % 1000000000 == 0 else ' '  + self.numberToWords(num%1000000000))
        