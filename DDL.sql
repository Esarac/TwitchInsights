USE DataAnalytics
GO

DROP TABLE IF EXISTS Twitch.MessagesStg
;CREATE TABLE Twitch.MessagesStg (
	Id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	Date DATETIME NOT NULL,
	MsgResponse VARCHAR(1000) NOT NULL
)

DROP TABLE IF EXISTS Twitch.MessagesRef
;CREATE TABLE Twitch.MessagesRef (
	Id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	Date DATETIME NOT NULL,
	Username VARCHAR(1000) NOT NULL,
	Command VARCHAR(1000) NOT NULL,
	Channel VARCHAR(1000) NOT NULL,
	Message VARCHAR(1000) NOT NULL
)