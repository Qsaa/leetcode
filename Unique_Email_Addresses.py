# ["test.email+alex@leetcode.com",
#  "test.e.mail+bob.cathy@leetcode.com",
#  "testemail+david@lee.tcode.com"]

testList1 = ["test.email+alex@leetcode.com",  "test.e.mail+bob.cathy@leetcode.com",  "testemail+david@lee.tcode.com"]
testList2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]


class Solution(object):
    def numUniqueEmails(self, emails):
        mySet = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            mySet.add(local + '@' + domain)
        return len(mySet)


solution = Solution()
print(solution.numUniqueEmails(testList2))


print("qwq.wqw.qw".replace('.', ''))
