USE DataAnalytics
GO

DROP TABLE IF EXISTS Twitch.Messages
;CREATE TABLE Twitch.Messages (
	Id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	Date DATETIME NOT NULL,
	MsgResponse VARCHAR(1000) NOT NULL
)

SELECT * FROM Twitch.Messages