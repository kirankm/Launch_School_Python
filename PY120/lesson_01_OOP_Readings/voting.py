class Election():
    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        for candidate in self.candidates:
            print(candidate)

        curr_winner = list(self.candidates)[0]
        total_votes = 0 
        for candidate in self.candidates:
            total_votes += candidate.vote
            if candidate > curr_winner:
                curr_winner = candidate
        
        winner_votes = curr_winner.vote
        winner_perc = 100 * (winner_votes / total_votes)

        print(f"{curr_winner.name} won: {winner_perc}% of votes")

class Candidate():
    def __init__(self, name):
        self.name = name
        self.vote = 0

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def vote(self):
        return self._vote

    @vote.setter
    def vote(self, value):
        self._vote = value

    def __add__(self, vote_cnt):
        if not isinstance(vote_cnt, int):
            return NotImplemented
        
        vote = self.vote + vote_cnt
        new_candidate = Candidate(self.name)
        new_candidate.vote = self.vote_cnt
        return new_candidate

    def __iadd__(self, vote_cnt):
        if not isinstance(vote_cnt, int):
            return NotImplemented
        
        self.vote += vote_cnt

    def __str__(self):
        return f"{self.name}: {self.vote} votes"
    
    def __gt__(self, other):
        if not isinstance(other, candidate):
            return NotImplemented
        return self.vote > other.vote
    
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1


election = Election(candidates)
election.results()