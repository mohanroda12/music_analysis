import { useState} from "react";
import type { Song } from "./types/Song";
import SongCard from "./SongCard.tsx";

const URL = "http://localhost:8000/songs"

function SearchBar() {

    const[songs, setSongs] = useState<Song[]>([])
    const[query, setQuery] = useState("")

    async function fetchSongs() {
            const result = await fetch(`${URL}/?query=${encodeURIComponent(query)}`)

            const song_list = await result.json();

            setSongs(song_list.songs)
        }

    function searchSongs(event: React.FormEvent) {
        event.preventDefault()
        fetchSongs()
    }

    return (
        <div className="song-search-container">
            <form onSubmit={searchSongs}>
                <input
                    className="song-search-bar"
                    type="search"
                    id="search-input"
                    placeholder="Search Songs..."
                    value={query}
                    onChange={(event) => setQuery(event.target.value)}
                />
                <button type="submit">Search</button>
            </form>
            <div className="song-card-grid">
                {songs.map((song) => (
                    <SongCard title={song.title} artist={song.artist} image_url={song.album_cover_url}/>
                ))}
            </div>

        </div>

    )
}

export default SearchBar;