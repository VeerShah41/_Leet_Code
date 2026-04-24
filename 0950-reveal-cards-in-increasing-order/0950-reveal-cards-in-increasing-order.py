class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        dq = deque()

        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())  # reverse step
            dq.appendleft(card)

        return list(dq)