create schema if not exists dbcontent;

create table if not exists news
(
	id BIGINT(19) auto_increment
		primary key,
	title VARCHAR(50) default '' null comment '标题',
	from_url VARCHAR(200) default '' null comment '来源地址',
	from_source VARCHAR(50) default '' null comment '来源',
	summary VARCHAR(200) default '' null comment '简介',
	create_date VARCHAR(50) default '0' null comment '创建日期',
	md5 VARCHAR(32) null,
	keyword VARCHAR(100) default '' null comment '关键字',
	ver INT(10) default 0 null
);

