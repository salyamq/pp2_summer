-- upserting data
create or replace procedure upsert_data(p_name varchar, p_number varchar)
as $$
begin
    if exists (select 1 from phonebook where name = p_name) then
        update phonebook set phone = p_number where name = p_name;
    else
        insert into phonebook (name, phone) values (p_name, p_number);
    end if;
end;
$$ language plpgsql;

-- insert many values
create or replace procedure insert_many_contacts(names varchar[], phones varchar[])
as $$
declare
    i integer;
begin
    for i in 1..array_length(names, 1) loop
        if phones[i] ~ '^[0-9]{10,15}$' then
            insert into phonebook (name, phone) values (names[i], phones[i]);
        else
            raise notice 'invalid data: % - %', names[i], phones[i];
        end if;
    end loop;
end;
$$ language plpgsql;

-- deleting by number or phone
create or replace procedure delete_contact(p_name varchar, p_number varchar)
as $$
begin
    delete from phonebook p where p_name = p.name or p_number = p.phone;
end;
$$ language plpgsql;