-- Creates index of table names and first letters
CREATE INDEX idx_name_first ON names(name(1));
