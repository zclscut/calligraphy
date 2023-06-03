-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-02-03 19:20:54
-- 服务器版本： 5.7.40-log
-- PHP 版本： 7.3.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `online_learning`
--

-- --------------------------------------------------------

--
-- 表的结构 `original_event`
--

CREATE TABLE `original_event` (
  `counter` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `event_key` varchar(3) NOT NULL,
  `event_value` varchar(3) NOT NULL,
  `record_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

-- --------------------------------------------------------

--
-- 表的结构 `original_event_key`
--

CREATE TABLE `original_event_key` (
  `event_type` varchar(45) DEFAULT NULL,
  `event_key` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `original_event_key`
--

INSERT INTO `original_event_key` (`event_type`, `event_key`) VALUES
('emotion', '1'),
('is_pitch', '2'),
('is_yaw', '3'),
('is_roll', '4'),
('is_z_gap', '5'),
('is_y_gap_sh', '6'),
('is_y_head_gap', '7'),
('is_per', '8'),
('is_blink', '9'),
('is_yawn', '10'),
('is_close', '11');

-- --------------------------------------------------------

--
-- 表的结构 `original_event_value`
--

CREATE TABLE `original_event_value` (
  `event_key` varchar(3) DEFAULT NULL,
  `event_value` varchar(3) DEFAULT NULL,
  `event_value_type` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `original_event_value`
--

INSERT INTO `original_event_value` (`event_key`, `event_value`, `event_value_type`) VALUES
('1', '1', 'not_found'),
('1', '2', 'hate'),
('1', '3', 'angry'),
('1', '4', 'sad'),
('1', '5', 'fear'),
('1', '6', 'neutral'),
('1', '7', 'surprise'),
('1', '8', 'happy'),
('2', '0', 'le'),
('2', '1', 'ge'),
('3', '0', 'le'),
('3', '1', 'ge'),
('4', '0', 'le'),
('4', '1', 'ge'),
('5', '0', 'le'),
('5', '1', 'ge'),
('6', '0', 'le'),
('6', '1', 'ge'),
('7', '0', 'le'),
('7', '1', 'ge'),
('8', '0', 'le'),
('8', '1', 'ge'),
('9', '0', 'le'),
('9', '1', 'ge'),
('10', '0', 'le'),
('10', '1', 'ge'),
('11', '0', 'le'),
('11', '1', 'ge');

-- --------------------------------------------------------

--
-- 表的结构 `parent_info`
--

CREATE TABLE `parent_info` (
  `parent_id` int(11) NOT NULL,
  `parent_name` varchar(20) NOT NULL,
  `parent_sex` varchar(6) NOT NULL,
  `parent_tel` varchar(20) NOT NULL,
  `parent_email` varchar(50) NOT NULL,
  `parent_pswd` varchar(20) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `parent_info`
--

INSERT INTO `parent_info` (`parent_id`, `parent_name`, `parent_sex`, `parent_tel`, `parent_email`, `parent_pswd`, `student_id`) VALUES
(1, 'Nancy', 'woman', '12345678901', '123456@gmail.com', '123456', 1);

-- --------------------------------------------------------

--
-- 表的结构 `student_info`
--

CREATE TABLE `student_info` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(20) NOT NULL,
  `student_sex` varchar(6) NOT NULL,
  `student_pswd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `student_info`
--

INSERT INTO `student_info` (`student_id`, `student_name`, `student_sex`, `student_pswd`) VALUES
(1, 'Fancy', 'woman', '123456');

-- --------------------------------------------------------

--
-- 表的结构 `study_state`
--

CREATE TABLE `study_state` (
  `counter` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `state_key` varchar(3) NOT NULL,
  `state_value` varchar(3) NOT NULL,
  `record_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `study_state`
--

INSERT INTO `study_state` (`counter`, `student_id`, `state_key`, `state_value`, `record_time`) VALUES
(1, 1, '1', '2', '2022-12-28 12:32:23'),
(2, 1, '2', '1', '2022-12-28 12:32:23'),
(3, 1, '3', '4', '2022-12-28 12:32:23'),
(4, 1, '4', '3', '2022-12-28 12:32:23');

-- --------------------------------------------------------

--
-- 表的结构 `study_state_key`
--

CREATE TABLE `study_state_key` (
  `state_type` varchar(45) DEFAULT NULL,
  `state_key` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `study_state_key`
--

INSERT INTO `study_state_key` (`state_type`, `state_key`) VALUES
('emotion', '1'),
('fatigue', '2'),
('posture', '3'),
('focus', '4');

-- --------------------------------------------------------

--
-- 表的结构 `study_state_value`
--

CREATE TABLE `study_state_value` (
  `state_key` varchar(3) DEFAULT NULL,
  `state_value` varchar(3) DEFAULT NULL,
  `state_value_type` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- 转存表中的数据 `study_state_value`
--

INSERT INTO `study_state_value` (`state_key`, `state_value`, `state_value_type`) VALUES
('1', '1', 'optimistic'),
('1', '2', 'neutral'),
('1', '3', 'negative'),
('2', '1', 'clear'),
('2', '2', 'critical_state'),
('2', '3', 'mild_fatigue'),
('2', '4', 'moderate_fatigue'),
('2', '5', 'severe_fatigue'),
('3', '1', 'normal'),
('3', '2', 'head_up'),
('3', '3', 'head_ahead'),
('3', '4', 'body_lean'),
('4', '1', 'extreme_more_focus'),
('4', '2', 'more_focus'),
('4', '3', 'less_focus'),
('4', '4', 'extreme_less_focus');

--
-- 转储表的索引
--

--
-- 表的索引 `original_event`
--
ALTER TABLE `original_event`
  ADD PRIMARY KEY (`counter`) USING BTREE;

--
-- 表的索引 `parent_info`
--
ALTER TABLE `parent_info`
  ADD PRIMARY KEY (`parent_id`) USING BTREE,
  ADD KEY `student_id_idx` (`student_id`) USING BTREE;

--
-- 表的索引 `student_info`
--
ALTER TABLE `student_info`
  ADD PRIMARY KEY (`student_id`) USING BTREE;

--
-- 表的索引 `study_state`
--
ALTER TABLE `study_state`
  ADD PRIMARY KEY (`counter`) USING BTREE;

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `original_event`
--
ALTER TABLE `original_event`
  MODIFY `counter` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=397;

--
-- 使用表AUTO_INCREMENT `study_state`
--
ALTER TABLE `study_state`
  MODIFY `counter` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- 限制导出的表
--

--
-- 限制表 `parent_info`
--
ALTER TABLE `parent_info`
  ADD CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `student_info` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
