-- Creates index on table names and first letter of name
CREATE INDEX idx_name_first_score ON names(name(1), score);
