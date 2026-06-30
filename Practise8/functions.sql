-- find by pattern (name, number)
create or replace function find_by_pattern_name(name varchar)
returns varchar
as $$
begin
    return '%' || name || '%';
end;
$$ language plpgsql;

create or replace function find_by_pattern_number(number varchar)
returns varchar
as $$
begin
    return '%' || number || '%';
end;
$$ language plpgsql;

-- pagination function

create or replace function get_contacts_paginated(p_limit integer, p_offset integer)
returns table(id integer, name varchar, phone varchar)
as $$
begin
    return query
    select p.id, p.name, p.phone
    from phonebook p
    order by p.id
    limit p_limit offset p_offset;
end;
$$ language plpgsql;
