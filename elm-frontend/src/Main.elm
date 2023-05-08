module Main exposing (Model, main)

import Browser exposing (..)
import Html exposing (..)
import Html.Attributes exposing (target)
import Task
import Time



-- MAIN


main =
    Browser.element
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }



-- MODEL


type alias Flags =
    { now : Int
    , target : Int
    }


type alias Model =
    { zone : Time.Zone
    , target : Time.Posix
    , time : Time.Posix
    , remaining : Time.Posix
    }


init : Flags -> ( Model, Cmd Msg )
init flags =
    ( Model Time.utc
        (Time.millisToPosix flags.target)
        (Time.millisToPosix flags.now)
        (timeLeft (Time.millisToPosix flags.target) (Time.millisToPosix flags.now))
    , Task.perform AdjustTimeZone Time.here
    )



-- UPDATE


type Msg
    = Tick Time.Posix
    | AdjustTimeZone Time.Zone


timeLeft : Time.Posix -> Time.Posix -> Time.Posix
timeLeft target now =
    Time.millisToPosix (Time.posixToMillis target - Time.posixToMillis now)


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Tick newTime ->
            ( { model
                | time = newTime
                , remaining =
                    timeLeft model.target newTime
              }
            , Cmd.none
            )

        AdjustTimeZone newZone ->
            ( { model | zone = newZone }
            , Cmd.none
            )



-- SUBSCRIPTIONS


subscriptions : Model -> Sub Msg
subscriptions _ =
    Time.every 1000 Tick



-- VIEW


timePart : Int -> String
timePart time =
    String.padLeft 2 '0' (String.fromInt time)


timeRemaining : Model -> String
timeRemaining model =
    let
        timeleftD =
            timePart (Time.posixToMillis model.remaining // (60 * 60 * 24 * 1000))

        timeleftH =
            timePart (Time.toHour model.zone model.remaining)

        timeleftM =
            timePart (Time.toMinute model.zone model.remaining)

        timeleftS =
            timePart (Time.toSecond model.zone model.remaining)
    in
    timeleftD ++ ":" ++ timeleftH ++ ":" ++ timeleftM ++ ":" ++ timeleftS


view : Model -> Html Msg
view model =
    let
        hour =
            String.fromInt (Time.toHour model.zone model.time)

        minute =
            String.fromInt (Time.toMinute model.zone model.time)

        second =
            String.fromInt (Time.toSecond model.zone model.time)
    in
    div []
        [ h1 []
            [ text (hour ++ ":" ++ minute ++ ":" ++ second) ]
        , h2 [] [ text (timeRemaining model) ]
        ]
