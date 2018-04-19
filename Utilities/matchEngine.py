class matchEngine:
    '''Handler class for a match engine.
    static, singletone.
    handles all matching shit'''

    def getMatch(matchRequester: str):
        return "match for {matchRequester} is {matchedUser}".format(matchRequester, "shahar")
