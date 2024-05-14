
--
-- Name: cities_chart_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities_chart_data (
    id integer NOT NULL,
    "Date" date NOT NULL,
    "Cities" character varying NOT NULL,
    "CityName" character varying,
    "Views" integer
);


ALTER TABLE public.cities_chart_data OWNER TO postgres;

--
-- Name: cities_chart_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cities_chart_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cities_chart_data_id_seq OWNER TO postgres;

--
-- Name: cities_chart_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cities_chart_data_id_seq OWNED BY public.cities_chart_data.id;


--
-- Name: cities_table_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities_table_data (
    id integer NOT NULL,
    "Cities" character varying NOT NULL,
    "CityName" character varying,
    "Geography1" character varying,
    "Geography2" character varying,
    "Views" integer,
    "WatchTime" double precision,
    "AverageViewDuration" time without time zone
);


ALTER TABLE public.cities_table_data OWNER TO postgres;

--
-- Name: cities_table_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cities_table_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cities_table_data_id_seq OWNER TO postgres;

--
-- Name: cities_table_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cities_table_data_id_seq OWNED BY public.cities_table_data.id;


--
-- Name: cities_totals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cities_totals (
    id integer NOT NULL,
    "Date" date NOT NULL,
    "Views" integer
);


ALTER TABLE public.cities_totals OWNER TO postgres;

--
-- Name: cities_totals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cities_totals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cities_totals_id_seq OWNER TO postgres;

--
-- Name: cities_totals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cities_totals_id_seq OWNED BY public.cities_totals.id;


--
-- Name: content_type_chart_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content_type_chart_data (
    id integer NOT NULL,
    "Date" date,
    "Content_Type" character varying,
    "Views" integer
);


ALTER TABLE public.content_type_chart_data OWNER TO postgres;

--
-- Name: content_type_chart_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.content_type_chart_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.content_type_chart_data_id_seq OWNER TO postgres;

--
-- Name: content_type_chart_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.content_type_chart_data_id_seq OWNED BY public.content_type_chart_data.id;


--
-- Name: content_type_table_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content_type_table_data (
    id integer NOT NULL,
    "Content_Type" character varying,
    "Views" integer,
    "Watch_Time" double precision,
    "Average_View_Duration" time without time zone
);


ALTER TABLE public.content_type_table_data OWNER TO postgres;

--
-- Name: content_type_table_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.content_type_table_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.content_type_table_data_id_seq OWNER TO postgres;

--
-- Name: content_type_table_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.content_type_table_data_id_seq OWNED BY public.content_type_table_data.id;


--
-- Name: content_type_totals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content_type_totals (
    id integer NOT NULL,
    "Date" date,
    "Views" integer
);


ALTER TABLE public.content_type_totals OWNER TO postgres;

--
-- Name: content_type_totals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.content_type_totals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.content_type_totals_id_seq OWNER TO postgres;

--
-- Name: content_type_totals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.content_type_totals_id_seq OWNED BY public.content_type_totals.id;


--
-- Name: device_type_chart_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.device_type_chart_data (
    id integer NOT NULL,
    "Date" date,
    "Device_Type" character varying,
    "Views" integer
);


ALTER TABLE public.device_type_chart_data OWNER TO postgres;

--
-- Name: device_type_chart_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.device_type_chart_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.device_type_chart_data_id_seq OWNER TO postgres;

--
-- Name: device_type_chart_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.device_type_chart_data_id_seq OWNED BY public.device_type_chart_data.id;


--
-- Name: device_type_table_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.device_type_table_data (
    id integer NOT NULL,
    "Device_Type" character varying,
    "Views" integer,
    "Watch_Time" double precision,
    "Average_View_Duration" time without time zone
);


ALTER TABLE public.device_type_table_data OWNER TO postgres;

--
-- Name: device_type_table_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.device_type_table_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.device_type_table_data_id_seq OWNER TO postgres;

--
-- Name: device_type_table_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.device_type_table_data_id_seq OWNED BY public.device_type_table_data.id;


--
-- Name: device_type_totals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.device_type_totals (
    id integer NOT NULL,
    "Date" date,
    "Views" integer
);


ALTER TABLE public.device_type_totals OWNER TO postgres;

--
-- Name: device_type_totals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.device_type_totals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.device_type_totals_id_seq OWNER TO postgres;

--
-- Name: device_type_totals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.device_type_totals_id_seq OWNED BY public.device_type_totals.id;


--
-- Name: geography_chart_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geography_chart_data (
    id integer NOT NULL,
    "Date" date,
    "Geography" character varying,
    "Views" integer
);


ALTER TABLE public.geography_chart_data OWNER TO postgres;

--
-- Name: geography_chart_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.geography_chart_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.geography_chart_data_id_seq OWNER TO postgres;

--
-- Name: geography_chart_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.geography_chart_data_id_seq OWNED BY public.geography_chart_data.id;


--
-- Name: geography_table_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geography_table_data (
    id integer NOT NULL,
    "Date" date,
    "Geography" character varying,
    "Views" integer
);


ALTER TABLE public.geography_table_data OWNER TO postgres;

--
-- Name: geography_table_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.geography_table_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.geography_table_data_id_seq OWNER TO postgres;

--
-- Name: geography_table_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.geography_table_data_id_seq OWNED BY public.geography_table_data.id;


--
-- Name: geography_totals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geography_totals (
    id integer NOT NULL,
    "Date" date,
    "Geography" character varying,
    "Views" integer
);


ALTER TABLE public.geography_totals OWNER TO postgres;

--
-- Name: geography_totals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.geography_totals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.geography_totals_id_seq OWNER TO postgres;

--
-- Name: geography_totals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.geography_totals_id_seq OWNED BY public.geography_totals.id;


--
-- Name: new_returning_viewers_chart_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_returning_viewers_chart_data (
    id integer NOT NULL,
    "Date" date,
    "New_Returning_Viewers" character varying,
    "Views" integer
);


ALTER TABLE public.new_returning_viewers_chart_data OWNER TO postgres;

--
-- Name: new_returning_viewers_chart_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.new_returning_viewers_chart_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.new_returning_viewers_chart_data_id_seq OWNER TO postgres;

--
-- Name: new_returning_viewers_chart_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.new_returning_viewers_chart_data_id_seq OWNED BY public.new_returning_viewers_chart_data.id;


--
-- Name: new_returning_viewers_table_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_returning_viewers_table_data (
    id integer NOT NULL,
    "New_Returning_Viewers" character varying,
    "Views" integer,
    "Watch_Time" double precision,
    "Average_View_Duration" time without time zone
);


ALTER TABLE public.new_returning_viewers_table_data OWNER TO postgres;

--
-- Name: new_returning_viewers_table_data_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.new_returning_viewers_table_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.new_returning_viewers_table_data_id_seq OWNER TO postgres;

--
-- Name: new_returning_viewers_table_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.new_returning_viewers_table_data_id_seq OWNED BY public.new_returning_viewers_table_data.id;


--
-- Name: new_returning_viewers_totals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_returning_viewers_totals (
    id integer NOT NULL,
    "Date" date,
    "Views" integer
);


ALTER TABLE public.new_returning_viewers_totals OWNER TO postgres;

--
-- Name: new_returning_viewers_totals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.new_returning_viewers_totals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.new_returning_viewers_totals_id_seq OWNER TO postgres;

--
-- Name: new_returning_viewers_totals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--