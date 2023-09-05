select
    ta.CommunityAgentId,
    COUNT(*)
from
    dbo.AgentToken token
    inner join dbo.TopsAgent ta on token.AgentId = ta.TopsAgentID
    and ta.TopsAgentTypeID = 2
    and token.BankAccountId IS NOT NULL
group by
    ta.CommunityAgentId