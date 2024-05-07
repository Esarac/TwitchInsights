-- ===========================================================================
-- Create Databases
-- ===========================================================================
-- Create DataAnalytics database
CREATE DATABASE DataAnalytics
GO

-- Use DataAnalytics database
USE DataAnalytics
GO

-- ===========================================================================
-- Create Schemas
-- ===========================================================================
-- Create Twitch schema
CREATE SCHEMA [Twitch]
GO

-- ===========================================================================
-- Create Tables
-- ===========================================================================
-- Create Twitch.MessagesStg table
CREATE TABLE [Twitch].[MessagesStg](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Date] [datetime] NOT NULL,
	[MsgResponse] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

-- Create Twitch.MessagesRef table
CREATE TABLE [Twitch].[MessagesRef](
	[Id] [bigint] NOT NULL,
	[Date] [datetime] NULL,
	[Username] [nvarchar](max) NULL,
	[Command] [nvarchar](max) NULL,
	[Channel] [nvarchar](max) NULL,
	[Message] [nvarchar](max) NOT NULL,
	[SentimentScore] [real] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [Twitch].[MessagesStg](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Date] [datetime] NOT NULL,
	[MsgResponse] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

-- ===========================================================================
-- Create Users
-- ===========================================================================
-- Create KafkaConsumer login (change to use env variables)
CREATE LOGIN [KafkaConsumer] WITH PASSWORD="$(KafkaPassword)", DEFAULT_DATABASE=[DataAnalytics], DEFAULT_LANGUAGE=[us_english], CHECK_EXPIRATION=ON, CHECK_POLICY=ON
GO

-- Create KafkaConsumer user
CREATE USER [KafkaConsumer] FOR LOGIN [KafkaConsumer] WITH DEFAULT_SCHEMA=[dbo]
GO

-- Grant permissions to KafkaConsumer user
GRANT
	ALTER
	,CONTROL
	,INSERT
	,DELETE
	,SELECT
	,EXECUTE
ON SCHEMA :: Twitch TO KafkaConsumer
GO

GRANT
	CREATE TABLE
TO KafkaConsumer;
GO