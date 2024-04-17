USE DataAnalytics
GO

-- Get latest requests
select *
from Twitch.MessagesStg as tw
order by tw.Date DESC

-- Get duplicates
select tw1.*
from Twitch.MessagesRef as tw1
	inner join Twitch.MessagesRef as tw2
		on tw1.Username = tw2.Username
			and tw1.Message = tw2.Message
			and tw1.Date = tw2.Date
			and tw1.Id > tw2.Id

-- Get chat from Esarac channel
SELECT *
FROM Twitch.MessagesRef as tw
WHERE tw.Channel = 'Esarac567'

-- Get all tags on each of the chat messages
WITH TwUsers AS (
	select tw.Username
	from Twitch.MessagesRef as tw
	group by tw.Username
)

select c.*, u.Username as Tag
from Twitch.MessagesRef as c
	cross join TwUsers as u
where c.Message like '%@'+u.Username+'%'
order by u.Username