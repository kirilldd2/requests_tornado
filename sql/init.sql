CREATE TABLE requests(  
    id LONGTEXT NOT NULL PRIMARY KEY COMMENT 'Primary Key',
    body LONGTEXT NOT NULL COMMENT '',
    duplicates INT UNSIGNED NOT NULL DEFAULT 0
);