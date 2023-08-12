CREATE TABLE rep (
    RID  INTEGER,
    repName varchar(64),

    PRIMARY KEY (RID)
);

CREATE TABLE repContact (
    RID          INTEGER,
    contact      VARCHAR(128), --Email,Phone,Address,etc.
    description VARCHAR(32),

    PRIMARY KEY (RID,contact),
    FOREIGN KEY (RID) REFERENCES rep(RID)
);

CREATE TABLE committee(
    CID     INTEGER,
    name    VARCHAR(30),
    chamber CHAR,

    PRIMARY KEY CID
);

CREATE TABLE committeeMember(
    RID   INTEGER,
    CID   INTEGER,
    chair BOOLEAN,

    PRIMARY KEY (RID,CID)
    FOREIGN KEY (RID) REFERENCES rep(RID),
    FOREIGN KEY (CID) REFERENCES committee(CID)
);

CREATE TABLE bill (
    billNum         INTEGER,
    billSession     INTEGER,
    chamberOfOrigin CHAR,
    statusHouse     CHAR,                   -- (I)ntroduced, In (C)ommitte, (P)assed
    statusSenate    CHAR,
    HCID            INTEGER,
    SCID            INTEGER,
    
    PRIMARY KEY (billNum,billSession),
    FOREIGN KEY (HCID) REFERENCES committee(CID),
    FOREIGN KEY (SCID) REFERENCES committee(CID)
)

CREATE TABLE voteDescription(
    VID     INTEGER,
    session INTEGER,
    billNum INTEGER,
    vote    CHAR,

    PRIMARY KEY (VID,session,billNum),
    FOREIGN KEY (session,billNum) REFERENCES bill(session,number)
)

CREATE TABLE repVote (
    VID         INTEGER,
    RID         INTEGER,
    type        CHAR,

    PRIMARY KEY (VID,RID),
    FOREIGN KEY (VID) REFERENCES voteDescription(VID),
    FOREIGN KEY (RID) REFERENCES rep(RID)
)

create table sponsor (
    RID     INTEGER,
    billNo  INTEGER,
    session INTEGER,

    FOREIGN KEY (RID) REFERENCES rep(RID),
    FOREIGN KEY (billNo,session) REFERENCES bill(number,session)
)

CREATE TABLE billSubscriber (
    channel     VARCHAR(128) --the channel or DM subscribed
    billSession INTEGER
    billNum     INTEGER

    FOREIGN KEY (billSession,billNum) REFERENCES bill(billSession,billNum)
);

CREATE TABLE meeting (
    ID      INTEGER, --lifted from HTML
    starts  CHAR(20),            --YYYY-MM-DD HH:MM:SS. 
    room    varchar(32),
    comment varchar(128),
    --- We should probably link this to bills and/or committees. ---

    PRIMARY KEY ID
)